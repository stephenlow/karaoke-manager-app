from __future__ import print_function
from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy.exc import SQLAlchemyError

from server.app.basemodels import db
from server.app.song.models import Song, SongSchema
from marshmallow import ValidationError
import sys

song = Blueprint('song', __name__)
api = Api(song)
schema = SongSchema(strict=True)


class SongList(Resource):
    @staticmethod
    def get():
        song_query = Song.query.all()
        results = schema.dump(song_query, many=True).data
        return jsonify(results)


class SongCreate(Resource):
    @staticmethod
    def post():
        raw_data = request.get_json(force=True)

        try:
            # validate request
            schema.validate(raw_data)
            song_data = raw_data['data']['attributes']

            name = song_data['name']
            artist_name = song_data['artist_name']
            description = song_data['description']

            print(song_data, file=sys.stdout)
            print(name, file=sys.stdout)
            print(artist_name, file=sys.stdout)
            print(description, file=sys.stdout)

            song_new = Song(name, artist_name, description)
            song_new.add(song_new)

            resp = jsonify({"message": "success"})
            resp.status_code = 201
            return resp

        except ValidationError as err:
            resp = jsonify({"error": str(err)})
            resp.status_code = 403
            return resp

        except SQLAlchemyError as err:
            db.session.rollback()
            resp = jsonify({"error": str(err)})
            resp.status_code = 403
            return resp


api.add_resource(SongList, '/')
api.add_resource(SongCreate, '/add')
