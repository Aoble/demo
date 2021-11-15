from flask import Flask, render_template
from app.view import config_blueprint
from app.config import config
from app.extensions import init_ext


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get("development"))
    config_blueprint(app)
    config[config_name].init_app(app)
    init_ext(app)
    config_errorhandler(app)
    return app


def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')
