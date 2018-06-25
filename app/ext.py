from flask_caching import Cache
from flask_login import LoginManager
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads

db = SQLAlchemy()

migrate = Migrate()


def init_ext(app: Flask):
    init_db_config(app)
    init_cache_config(app)
    init_login_config(app)


def init_db_config(app):
    app.config['SECRET'] = '12213213421'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_ext?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    migrate.init_app(app, db)


cache = Cache()


# 缓存配置
def init_cache_config(app):
    cache.init_app(app, config={
        'CACHE_DEFAULT_TIMEOUT': 60,
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_HOST': '127.0.0.1',
        'CACHE_REDIS_PORT': 6379,
        'CACHE_REDIS_DB': 1,
        'CACHE_KEY_PREFIX': 'view_'

    })


login_manager = LoginManager()


def init_login_config(app):
    login_manager.login_view = 'user.login'
    login_manager.login_message = '登录才能访问'
    login_manager.init_app(app)


"""
文件上传相关配置:
name 保存文件的字目录,默认是files
extensions 设置允许上传的文件的类型 默认类型
default_dest 设置文件上传的根路径
"""
image = UploadSet(name='images', extensions=IMAGES, default_dest=None)
import os

"""
配置信息:
1. 配饰文件上传的根目录
2. 
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT_PATH = os.path.join(BASE_DIR, 'media/upload')


def init_upload_config(app):
    # 配置上传目录
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_ROOT_PATH
    # 生成文件的访问的url地址
    # app.config['UPLOADS_DEFAULT_URL'] = ''
    configure_uploads(app=app, upload_set=images)












