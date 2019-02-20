from flask import Flask
from .settings import configDict
from .extensions import config_extension
from .views import blueprint_register
def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configDict[configName])
    config_extension(app)
    blueprint_register(app)
    return app