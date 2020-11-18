import sys
from twisted.internet import endpoints
from twisted.internet import protocol
from twisted.internet import defer
from twisted.internet import stdio
from twisted.mail import imap4
from twisted.protocols import basic
import re
import base64


class TrivialPrompter(basic.LineReceiver):
    from os import linesep as delimiter
    delimiter = delimiter.encode('utf-8')

    promptDeferred = None

    def prompt(self, msg):
        assert self.promptDeferred is None
        self.display(msg)
        self.promptDeferred = defer.Deferred()
        return self.promptDeferred

    def display(self, msg):
        self.transport.write(msg.encode('utf-8'))

    def lineReceived(self, line):
        if self.promptDeferred is None:
            return
        d, self.promptDeferred = self.promptDeferred, None
        d.callback(line.decode('utf-8'))


class SimpleIMAP4Client(imap4.IMAP4Client):
    """
    A client with callbacks for greeting messages from an IMAP server.
    """
    greetDeferred = None

    def serverGreeting(self, caps):
        self.serverCapabilities = caps
        if self.greetDeferred is not None:
            d, self.greetDeferred = self.greetDeferred, None
            d.callback(self)


class SimpleIMAP4ClientFactory(protocol.ClientFactory):
    usedUp = False

    protocol = SimpleIMAP4Client

    def __init__(self, username, onConn):
        self.username = username
        self.onConn = onConn

    def buildProtocol(self, addr):
        """
        Initiate the protocol instance. Since we are building a simple IMAP
        client, we don't bother checking what capabilities the server has. We
        just add all the authenticators twisted.mail has.  Note: Gmail no
        longer uses any of the methods below, it's been using XOAUTH since
        2010.
        """
        assert not self.usedUp
        self.usedUp = True

        p = self.protocol()
        p.factory = self
        p.greetDeferred = self.onConn

        p.registerAuthenticator(imap4.PLAINAuthenticator(self.username))
        p.registerAuthenticator(imap4.LOGINAuthenticator(self.username))
        p.registerAuthenticator(
            imap4.CramMD5ClientAuthenticator(self.username))

        return p

    def clientConnectionFailed(self, connector, reason):
        d, self.onConn = self.onConn, None
        d.errback(reason)


# 初始化回调函数
def cbServerGreeting(proto, username, password):
    """
    Initial callback - invoked after the server sends us its greet message.
    """
    # Hook up stdio
    tp = TrivialPrompter()
    stdio.StandardIO(tp)

    proto.prompt = tp.prompt
    proto.display = tp.display

    return proto.login(username, password
                       ).addCallback(cbAuthentication, proto
                                     )


# 发生错误时回调这个函数
def ebConnection(reason):
    """
    Fallback error-handler. If anything goes wrong, log it and quit.
    """
    log.startLogging(sys.stdout)
    log.err(reason)
    return reason


# 在登录成功后，回调这个函数
def cbAuthentication(result, proto):
    return proto.list("", "*"
                      ).addCallback(cbMailboxList, proto
                                    )


#  当邮箱列表被获取时调用该函数
def cbMailboxList(result, proto):
    result = [e[2] for e in result]
    s = '\n'.join(['%d. %s' % (n + 1, m) for (n, m) in zip(range(len(result)), result)])
    if not s:
        return defer.fail(Exception("No mailboxes exist on server!"))
    return proto.prompt(s + "\nWhich mailbox? [1] "
                        ).addCallback(cbPickMailbox, proto, result
                                      )


# 当用户选择一个邮箱时，检测这个邮箱
def cbPickMailbox(result, proto, mboxes):
    mbox = mboxes[int(result or '1') - 1]
    return proto.examine(mbox
                         ).addCallback(cbExamineMbox, proto
                                       )


# 返回每封邮件的标题
def cbExamineMbox(result, proto):
    return proto.fetchSpecific('1:*',
                               headerType='HEADER.FIELDS',
                               headerArgs=['SUBJECT'],
                               ).addCallback(cbFetch, proto
                                             )


# 获取邮箱信息后，输出邮件标题
def cbFetch(result, proto):
    if result:
        keys = sorted(result)
        for k in keys:
            subject = result[k][0][2]
            print(subject)
            matchResult = re.match('[^\?]*\?([^\?]*)\?.{1}\?(.*)', subject)
            encoding = matchResult.group(1)
            base64Str = matchResult.group(2)
            subject = base64.b64decode(base64Str).decode(encoding)
            proto.display('%s %s\n' % (k, subject))
    else:
        print("邮箱为空!")

    return proto.logout()


def cbClose(result):
    # 当完成任务时关闭连接.
    from twisted.internet import reactor
    reactor.stop()


def main():
    hostname = 'imap.126.com'
    port = 143

    username = '邮箱用户名'.encode('ascii')
    password = '邮箱密码'.encode('ascii')

    onConn = defer.Deferred(
    ).addCallback(cbServerGreeting, username, password
                  ).addErrback(ebConnection
                               ).addBoth(cbClose)

    factory = SimpleIMAP4ClientFactory(username, onConn)

    port = int(port)

    from twisted.internet import reactor

    endpoint = endpoints.HostnameEndpoint(reactor, hostname, port)

    endpoint.connect(factory)
    reactor.run()


if __name__ == '__main__':
    main()
