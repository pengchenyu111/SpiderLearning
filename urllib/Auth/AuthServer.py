from flask import Flask
from flask import request
import base64

app = Flask(__name__)


def hasAuth(auth, response):
    if auth == None or auth.strip() == "":
        response.status_code = 401
        response.headers["WWW-Authenticate"] = 'Basic realm="localhost"'
        return False
    return True


@app.route("/")
def index():
    response = app.make_response('username or password error')
    print(request.headers)
    auth = request.headers.get('Authorization')
    if hasAuth(auth, response):
        auth = str(base64.b64decode(auth.split(' ')[1]), 'utf-8')
        values = auth.split(':')
        username = values[0]
        password = values[1]
        print('username:', username)
        print('password:', password)
        if username == 'bill' and password == '1234':
            return "success"
    return response


if __name__ == '__main__':
    app.run()
