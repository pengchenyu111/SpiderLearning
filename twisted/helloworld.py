def hello():
    print('Hello,How are you?')


from twisted.internet import reactor

# 执行回调函数
reactor.callWhenRunning(hello)
print('Starting the reactor.')
reactor.run()
