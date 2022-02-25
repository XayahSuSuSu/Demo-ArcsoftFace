import os

import tornado.ioloop
import tornado.web

from util import db
from util.face import activate, initEngine, getFaceFeature, getComparison


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # 允许跨域
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


class pictures(BaseHandler):
    def post(self):
        files = self.request.files
        name = self.request.body_arguments['name'][0].decode()
        for i in files['file']:
            picture_bytes = i['body']
            db.insert(name, picture_bytes, getFaceFeature(picture_bytes)[0]['face_feature'])
        self.write({
            'code': 1,
            'msg': '上传成功！',
            'data': ''
        })


class face(BaseHandler):
    def post(self):
        files = self.request.files
        results = []
        for i in files['file']:
            picture_bytes = i['body']
            features = getFaceFeature(picture_bytes)
            data = db.get_all()
            for i in data:
                record = {'name': i['name'], 'data': []}
                for j in features:
                    face_info = {
                        'face_rect': j['face_rect'],
                        'face_orient': j['face_orient'],
                        'face_score': getComparison(j['face_feature'], i['face_feature'])
                    }
                    record['data'].append(face_info)
                results.append(record)
        self.write({
            'code': 1,
            'msg': '操作成功！',
            'data': results
        })


def make_app():
    return tornado.web.Application([
        (r'/api/v1/pictures', pictures),
        (r'/api/v1/face', face),
    ], static_path=os.path.join(os.path.dirname(__file__), "asserts"), static_url_prefix="/asserts/")


if __name__ == "__main__":
    # 初始化MySQL数据库
    db.init()
    # 初始化虹软引擎
    activate()
    initEngine()
    # 判断是否存在asserts文件夹，没有则创建
    if not os.path.exists("asserts"):
        os.mkdir("asserts")
    app = make_app()
    app.listen(3308)
    tornado.ioloop.IOLoop.current().start()
