from pyarcsoftface.struct_info import *

c_ubyte_p = POINTER(c_ubyte)

# 激活
ASFOnlineActivation = libarcsoft_face_engine.ASFOnlineActivation
ASFOnlineActivation.restype = c_int32
ASFOnlineActivation.argtypes = (c_char_p, c_char_p)

# 获取激活文件信息
ASFGetActiveFileInfo = libarcsoft_face_engine.ASFGetActiveFileInfo
ASFGetActiveFileInfo.restype = c_int32
ASFGetActiveFileInfo.argtypes = (POINTER(ASF_ActiveFileInfo),)

# 初始化
ASFInitEngine = libarcsoft_face_engine.ASFInitEngine
ASFInitEngine.restype = c_int32
ASFInitEngine.argtypes = (c_long, c_int32, c_int32, c_int32, c_int32, POINTER(c_void_p))

# 人脸识别
ASFDetectFaces = libarcsoft_face_engine.ASFDetectFaces
ASFDetectFaces.restype = c_int32
ASFDetectFaces.argtypes = (c_void_p, c_int32, c_int32, c_int32, POINTER(c_ubyte), POINTER(ASF_MultiFaceInfo))

# 特征提取
ASFFaceFeatureExtract = libarcsoft_face_engine.ASFFaceFeatureExtract
ASFFaceFeatureExtract.restype = c_int32
ASFFaceFeatureExtract.argtypes = (
    c_void_p, c_int32, c_int32, c_int32, POINTER(c_ubyte), POINTER(ASF_SingleFaceInfo), POINTER(ASF_FaceFeature))

# 特征比对
ASFFaceFeatureCompare = libarcsoft_face_engine.ASFFaceFeatureCompare
ASFFaceFeatureCompare.restype = c_int32
ASFFaceFeatureCompare.argtypes = (c_void_p, POINTER(ASF_FaceFeature), POINTER(ASF_FaceFeature), POINTER(c_float))

#  RGB图像属性检测
ASFProcess = libarcsoft_face_engine.ASFProcess
ASFProcess.restype = c_int32
ASFProcess.argtypes = (c_void_p, c_int32, c_int32, c_int32, POINTER(c_ubyte), POINTER(ASF_MultiFaceInfo), c_int32)

# 获取3d角度信息
ASFGetFace3DAngle = libarcsoft_face_engine.ASFGetFace3DAngle
ASFGetFace3DAngle.restype = c_int32
ASFGetFace3DAngle.argtypes = (c_void_p, POINTER(ASF_Face3DAngle))

# 获取rgb活体信息
ASFGetLivenessScore = libarcsoft_face_engine.ASFGetLivenessScore
ASFGetLivenessScore.restype = c_int32
ASFGetLivenessScore.argtypes = (c_void_p, POINTER(ASF_LivenessInfo))

# 获取性别信息
ASFGetGender = libarcsoft_face_engine.ASFGetGender

ASFGetGender.restype = c_int32
ASFGetGender.argtypes = (c_void_p, POINTER(ASF_GenderInfo))

# 获取年龄
ASFGetAge = libarcsoft_face_engine.ASFGetAge
ASFGetAge.restype = c_int32
ASFGetAge.argtypes = (c_void_p, POINTER(ASF_AgeInfo))

# 获取ir信息
ASFGetLivenessScore_IR = libarcsoft_face_engine.ASFGetLivenessScore_IR
ASFGetLivenessScore_IR.restype = c_int32
ASFGetLivenessScore_IR.argtypes = (c_void_p, POINTER(ASF_LivenessInfo))

# 设置活体检测阈值
ASFSetLivenessParam = libarcsoft_face_engine.ASFSetLivenessParam
ASFSetLivenessParam.restype = c_int32
ASFSetLivenessParam.argtypes = (c_void_p, POINTER(ASF_LivenessThreshold))

# IR 活体单人脸检测
ASFProcess_IR = libarcsoft_face_engine.ASFProcess_IR
ASFProcess_IR.restype = c_int32
ASFProcess_IR.argtypes = (c_void_p, c_int32, c_int32, c_int32, POINTER(c_ubyte), POINTER(ASF_MultiFaceInfo), c_int32)

# 销毁引擎
ASFUninitEngine = libarcsoft_face_engine.ASFUninitEngine
ASFUninitEngine.argtypes = (c_void_p,)

malloc = libc.malloc
malloc.restype = c_void_p
malloc.argtypes = (c_size_t,)

free = libc.free
free.restype = None
free.argtypes = (c_void_p,)

memcpy = libc.memcpy
memcpy.restype = c_void_p
memcpy.argtypes = (c_void_p, c_void_p, c_size_t)
