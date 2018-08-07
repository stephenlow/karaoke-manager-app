from server.app.basemodels import db, CRUD
from sqlalchemy import Integer, String, Column, Boolean, DateTime, func


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


