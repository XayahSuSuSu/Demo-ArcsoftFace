from flask import Flask
from flask_cors import CORS

from util import db
from util.face import activate, initEngine
from util.router import router

app = Flask(__name__)

# 避免返回值乱码
app.config['JSON_AS_ASCII'] = False

# 允许跨域
CORS(app, supports_credentials=True)

app.register_blueprint(router, url_prefix="/")

# 初始化MySQL数据库
db.init()

# 初始化虹软引擎
activate()
initEngine()

if __name__ == '__main__':
    app.run()
