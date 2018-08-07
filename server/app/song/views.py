from __future__ import print_function
from flask import Blueprint, request, render_template, jsonify
from flask_restful import Resource, Api
from sqlalchemy.exc import SQLAlchemyError

from server.app.basemodels import db
from server.app.song.models import Song
import sys

song = Blueprint('song', __name__, template_folder='../../../static')
api = Api(song)


@song.route("/", methods=['GET', 'POST'])
def index():
    if request.form:
        print(request.form)

    return render_template("index.html")


@song.route("/hello")
def hello():
    return "Hello World!"


class SongList(Resource):

    # def get(self):

    @staticmethod
    def post():
        print('HELLO STEPHEN', file=sys.stdout)
        raw_data = request.get_json(force=True)

        try:
            name = raw_data['name']
            artist_name = raw_data['artist_name']
            description = raw_data['description']

            print(raw_data, file=sys.stdout)
            print(name, file=sys.stdout)
            print(artist_name, file=sys.stdout)
            print(description, file=sys.stdout)

            song_new = Song(name, artist_name, description)
            song_new.add(song_new)

            resp = jsonify({"message": "success"})
            resp.status_code = 201
            return resp

        except SQLAlchemyError as err:
            db.session.rollback()
            resp = jsonify({"error": str(err)})
            resp.status_code = 403
            return resp


api.add_resource(SongList, '/add')
