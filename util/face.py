import cv2
import numpy as np

from pyarcsoftface.engine import *
from util.Key import APPID, SDKKey


def activate():
    """联网激活"""
    res = ASFOnlineActivation(APPID, SDKKey)
    if MOK != res and MERR_ASF_ALREADY_ACTIVATED != res:
        print("接口激活失败！代码: {}".format(res))


def initEngine():
    """初始化引擎并返回"""

    # 获取人脸识别引擎
    face_engine = ArcFace()

    # 人脸检测 | 人脸特征
    mask = ASF_FACE_DETECT | ASF_FACERECOGNITION

    # 初始化接口
    res = face_engine.ASFInitEngine(ASF_DETECT_MODE_IMAGE, ASF_OP_0_ONLY, 30, 10, mask)
    if res != MOK:
        print("初始化接口失败！代码: {}".format(res))
    return face_engine


def unInitEngine(face_engine):
    """反初始化"""
    face_engine.ASFUninitEngine()


def getFaceFeature(picture):
    activate()
    face_engine = initEngine()

    np_picture = np.frombuffer(picture, np.uint8)
    img = cv2.imdecode(np_picture, cv2.IMREAD_ANYCOLOR)

    face_feature = b''
    res, detectedFaces1 = face_engine.ASFDetectFaces(img)
    # print("人脸数据: {}".format(detectedFaces1))
    if res == MOK:
        single_detected_face1 = ASF_SingleFaceInfo()
        single_detected_face1.faceRect = detectedFaces1.faceRect[0]
        single_detected_face1.faceOrient = detectedFaces1.faceOrient[0]
        res, face_feature1 = face_engine.ASFFaceFeatureExtract(img, single_detected_face1)
        face_feature = face_feature1.get_feature_bytes()
        if res != MOK:
            print("人脸特征提取失败！代码: {}".format(res))
    else:
        print("人脸检测失败！代码: {}".format(res))

    unInitEngine(face_engine)
    return face_feature


def getComparison(face_feature1, face_feature2):
    """返回相似度"""
    activate()
    face_engine = initEngine()
    feature1 = ASF_FaceFeature()
    feature1.set_feature(face_feature1)
    feature2 = ASF_FaceFeature()
    feature2.set_feature(face_feature2)
    res, score = face_engine.ASFFaceFeatureCompare(feature1, feature2)
    unInitEngine(face_engine)
    return score
