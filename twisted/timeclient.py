# 导入protocol模块和reactor模块
from twisted.internet import protocol, reactor

host = 'localhost'
port = 9876


# 定义回调类
class MyProtocol(protocol.Protocol):
    # 从Console中采集要发送给服务器的数据，按回车键后，会见数据发送给服务器
    def sendData(self):
        data = input('>')
        if data:
            print('...正在发送 %s' % data)
            # 将数据发送给服务器
            self.transport.write(data.encode(encoding='utf_8'))
        else:
            # 发生异常后，关闭连接
            self.transport.loseConnection()

    # 发送数据
    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        # 输出接收到的数据
        print(data.decode('utf-8'))
        # 调用sendData函数，从Console采集要发送的数据
        self.sendData()


# 工厂类
class MyFactory(protocol.ClientFactory):
    protocol = MyProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


# 连接host和port，以及MyFactory类的实例
reactor.connectTCP(host, port, MyFactory())
reactor.run()
