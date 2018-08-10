from server.app.basemodels import db, CRUD
from sqlalchemy import Integer, String, Column, Boolean, DateTime, func
from marshmallow_jsonapi import Schema, fields


class Song(db.Model, CRUD):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    artist_name = Column(String(250), unique=True)
    description = Column(String(250))
    created_at = Column(DateTime, default=func.current_timestamp())
    deleted = Column(Boolean(), default=False)

    def __init__(self, name, artist_name, description):
        self.name = name
        self.artist_name = artist_name
        self.description = description

    def __repr__(self):
        return '<Song %r by %r>' % (self.name, self.artist_name)


class SongSchema(Schema):
    id = fields.Str(dump_only=True)  # Required
    name = fields.String(required=True)
    artist_name = fields.String(required=True)
    description = fields.String(required=True)
    created_at = fields.DateTime()
    deleted = fields.Boolean()

    class Meta:
        type_ = 'song'
        # fields = ('id', 'name', 'artist_name', 'description', 'created_at', 'deleted)
