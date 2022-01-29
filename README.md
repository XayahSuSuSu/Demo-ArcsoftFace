# 虹软人脸识别Linux Demo

> 平台：Linux
>
> 工具：Cmake、Make

## 环境配置及编译

### 一、OpenCV配置
1. 安装libgtk2.0-dev
```
sudo apt-get install libgtk2.0-dev
```

2. 下载[OpenCV源码](https://opencv.org/releases/)（以4.5.5为例）

3. 解压至任意文件夹
```
unzip opencv-4.5.5.zip
```

4. 进入解压后的文件夹，创建build文件夹并进入
```
cd opencv-4.5.5
mkdir build && cd build
```

5. Cmake生成Makefile
```
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local/ ..
```

6. 编译OpenCV（-j为线程数）
```
make -j8
```

7. 安装
```
sudo make install
```

8. 验证（运行opencv_example后弹出Hello OpenCV即为成功）
```
cd ../samples/cpp/example_cmake
cmake .
make
./opencv_example
```

### 二、项目配置及编译
1. 打开项目根目录下inc/key.h，填写[虹软开发者中心](https://ai.arcsoft.com.cn/ucenter/resource/build/index.html#/application)获取到的APPID和SDKKEY

2. 在项目根目录下，创建build目录并进入
```
mkdir build && cd build
```

3. Cmake生成Makefile
```
cmake ..
```

4. 编译（产物即为build/arcsoft_face_engine_test）
```
make
```

5. 复制libarcsoft_face.so至/usr/lib
```
sudo cp ../linux_so/libarcsoft_face.so /usr/lib
```

6. 运行
```
./arcsoft_face_engine_test
```

## 许可证
本项目遵循 [GNU General Public License v3.0](./LICENSE) 协议。