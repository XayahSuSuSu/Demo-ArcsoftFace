# 虹软人脸识别后端

> 平台：Linux
>
> 环境：Python3
> 
> SDK：V3.0

## 环境配置

### 一、Python
```
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 二、MySql
#### 完全卸载（有意外情况时选用）
##### 查看MySQL依赖项
```
dpkg --list|grep mysql
```
##### 卸载
```
sudo rm -rf /var/lib/mysql
sudo rm -rf /etc/mysql
sudo apt-get autoremove mysql* --purge
```


#### 重启服务（有意外情况时选用）
```
sudo service mysql restart
```

#### 安装及配置
1. 安装
```
sudo apt-get install mysql-server
```

2. 查看自动生成的debian-sys-maint账号及密码
```
sudo cat /etc/mysql/debian.cnf
```

3. 登录debian-sys-maint账号
```
mysql -udebian-sys-maint -p
```

4. 为root账号设置密码（123456）
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '123456';
```

5. 退出
```
quit
```

### 三、配置APPID及SDKKEY
打开项目根目录下Key.py，填写[虹软开发者中心](https://ai.arcsoft.com.cn/ucenter/resource/build/index.html#/application)获取到的APPID和SDKKEY

### 四、运行
```
gunicorn -k gevent App:app
```

## 许可证
本项目遵循 [GNU General Public License v3.0](./LICENSE) 协议。

