from flask import Flask
from app.ext import init_ext
from app.settings import envs
from app.views import init_blue


def creat_app():
    app = Flask(__name__,template_folder="../templates",static_folder="../static")
    app.config.from_object(envs.get("develop"))
    # 调试信息，如果不开会报错，true会占用内存
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    init_blue(app)
    init_ext(app)
    return app