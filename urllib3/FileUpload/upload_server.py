import os
from flask import Flask, request

# 定义服务端保存上传文件的位置
UPLOAD_FOLDER = 'Files'
app = Flask(__name__)


# 用于接收上传文件的路由需要使用POST方法
@app.route('/', methods=['POST'])
def upload_file():
    # 获取上传文件的内容
    file = request.files['file']
    if file:
        # 将上传的文件保存到uploads子目录中
        print('**********' + os.path.basename(file.filename))
        print('**********' + os.path.join(UPLOAD_FOLDER, os.path.basename(file.filename)))
        file.save(os.path.join(UPLOAD_FOLDER, os.path.basename(file.filename)))
        return "文件上传成功"


if __name__ == '__main__':
    app.run()
