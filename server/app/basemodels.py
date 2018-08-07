from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()


class CRUD:

    def __init__(self):
        pass

    @staticmethod
    def session_commit():
        try:
            db.session.commit()
        except SQLAlchemyError as error:
            db.session.rollback()
            message = str(error)
            return message

    def add(self, resource):
        db.session.add(resource)
        return self.session_commit()

    def read(self):
        return self.query.all()
