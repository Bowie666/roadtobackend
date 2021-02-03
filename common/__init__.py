from flask import Flask


def create_app(default_config):
    app = Flask(__name__)
    app.config.from_object(default_config)

    # 日志
    from .logging import flask_file_handle
    app.logger.addHandler(flask_file_handle)
    app.logger.setLevel('DEBUG')

    # 蓝图
    from api import func_bp
    app.register_blueprint(func_bp)

    return app
