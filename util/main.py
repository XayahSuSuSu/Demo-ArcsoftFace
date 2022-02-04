import cv2

from Key import APPID, SDKKey
from pyarcsoftface.engine import *

# 联网激活
res = ASFOnlineActivation(APPID, SDKKey)
if MOK != res and MERR_ASF_ALREADY_ACTIVATED != res:
    print("接口激活失败！代码: {}".format(res))

# 获取人脸识别引擎
face_engine = ArcFace()

# 人脸检测 | 人脸特征
mask = ASF_FACE_DETECT | ASF_FACERECOGNITION

# 初始化接口
res = face_engine.ASFInitEngine(ASF_DETECT_MODE_IMAGE, ASF_OP_0_ONLY, 30, 10, mask)
if res != MOK:
    print("初始化接口失败！代码: {}".format(res))

# RGB图像
img1 = cv2.imread("../asserts/1.jpg")
img2 = cv2.imread("../asserts/2.jpg")

# 检测第一张图中的人脸
res, detectedFaces1 = face_engine.ASFDetectFaces(img1)
print("人脸数据: {}".format(detectedFaces1))
if res == MOK:
    single_detected_face1 = ASF_SingleFaceInfo()
    single_detected_face1.faceRect = detectedFaces1.faceRect[0]
    single_detected_face1.faceOrient = detectedFaces1.faceOrient[0]
    res, face_feature1 = face_engine.ASFFaceFeatureExtract(img1, single_detected_face1)
    if res != MOK:
        print("人脸特征提取失败！代码: {}".format(res))
else:
    print("人脸检测失败！代码: {}".format(res))

# 检测第二张图中的人脸
res, detectedFaces2 = face_engine.ASFDetectFaces(img2)
if res == MOK:
    single_detected_face2 = ASF_SingleFaceInfo()
    single_detected_face2.faceRect = detectedFaces2.faceRect[0]
    single_detected_face2.faceOrient = detectedFaces2.faceOrient[0]
    res, face_feature2 = face_engine.ASFFaceFeatureExtract(img2, single_detected_face2)
    if res == MOK:
        pass
    else:
        print("人脸特征提取失败！代码: {}".format(res))
else:
    print("人脸检测失败！代码: {}".format(res))

# 比较两个人脸的相似度
res, score = face_engine.ASFFaceFeatureCompare(face_feature1, face_feature2)
print("相似度:", score)

# 反初始化
face_engine.ASFUninitEngine()
