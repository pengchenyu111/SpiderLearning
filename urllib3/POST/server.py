# 支持HTTP POST请求的服务端程序
from flask import Flask, request

# 创建Flask对象，任何基于flask模块的服务端应用都必须创建Flask对象
app = Flask(__name__)


# 设置/register路由，该路由可以处理HTTP POST请求
@app.route('/register', methods=['POST'])
def register():
    # 输出名为name的请求字字段的值
    print(request.form.get('name'))
    # 输出名为age的请求字段的值
    print(request.form.get('age'))
    # 向客户端返回“注册成功”消息
    return '注册成功'


if __name__ == '__main__':
    # 开始运行服务端程序，默认端口号是5000
    app.run()
