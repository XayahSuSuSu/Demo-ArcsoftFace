import datetime

import pymysql

HOST = '127.0.0.1'  # 宿主机地址
USER = 'root'  # 用户名
PASSWORD = '123456'  # 密码
DB = 'App'  # 数据库名

TABLE_DATA = 'data'
FIELD_DATA = [
    "name text,",
    "picture mediumblob,",
    "face_feature mediumblob",
]


def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_all():
    """返回表中所有数据"""
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("use {};".format(DB))
    cursor.execute("SELECT * from {}".format(TABLE_DATA))
    data = cursor.fetchall()
    return data


def init():
    """创建数据库和数据表"""
    global db
    db = pymysql.connect(host=HOST, user=USER, password=PASSWORD, charset='utf8')
    cursor = db.cursor()
    # 创建数据库
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARSET utf8 COLLATE utf8_general_ci;".format(DB))
    # 选择数据库
    cursor.execute("use {};".format(DB))
    # 创建数据表(DATA)
    field_data = "".join(FIELD_DATA)
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS {}(id int primary key not null auto_increment,".format(TABLE_DATA)
        + "created_at timestamp,updated_at timestamp,"
        + field_data
        + ");")


def insert(name, picture, face_feature):
    """插入一条记录"""
    cursor = db.cursor()
    cursor.execute("use {};".format(DB))
    insert_data = "INSERT INTO data VALUES (0,%s,%s,%s,%s,%s)"
    args = (timestamp(), timestamp(), name, picture, face_feature)
    cursor.execute(insert_data, args)
    db.commit()
