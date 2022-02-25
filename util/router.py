from flask import Blueprint, request

from util import db
from util.face import getFaceFeature, getComparison

router = Blueprint('router', __name__)


@router.route("/")
def init():
    return "Server is running..."


@router.route('/api/v1/pictures', methods=['POST'])
def pictures():
    try:
        if request.method == 'POST':
            picture = request.files['file']
            name = request.form.to_dict()['name']
            picture_bytes = picture.stream.read()
            db.insert(name, picture_bytes, getFaceFeature(picture_bytes)[0]['face_feature'])
            return {
                'code': 1,
                'msg': '上传成功！',
                'data': ''
            }
    except KeyError:
        return {
            'code': -1,
            'message': '参数错误',
        }


@router.route('/api/v1/face', methods=['POST'])
def face():
    try:
        if request.method == 'POST':
            picture = request.files['file']
            picture_bytes = picture.stream.read()
            features = getFaceFeature(picture_bytes)
            data = db.get_all()
            results = []
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
            return {
                'code': 1,
                'msg': '操作成功！',
                'data': results
            }
    except KeyError:
        return {
            'code': -1,
            'message': '参数错误',
        }
