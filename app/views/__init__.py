from .main import main

blueprint = [(main, "")]


def blueprint_register(app):
    for blue, prefix in blueprint:
        app.register_blueprint(blue, url_prefix=prefix)
