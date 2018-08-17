from flask import Flask
from flask_cors import CORS


def create_app(config_filename):
    app = Flask(__name__ )
    CORS(app)
    app.config.from_object(config_filename)

    from basemodels import db
    db.init_app(app)

    from song.views import song
    app.register_blueprint(song, url_prefix='/song')

    return app
