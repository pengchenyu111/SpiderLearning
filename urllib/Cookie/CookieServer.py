from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/readCookie")
def readCookie():
    print(request.cookies)
    print(request.cookies.get('MyCookie'))
    return "hello world"


@app.route("/writeCookie")
def writeCookie():
    response = app.make_response('write cookie')
    response.set_cookie("id", value="12345678")
    return response


if __name__ == '__main__':
    app.run()
