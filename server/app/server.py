from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, Boolean, DateTime, func

app = Flask(__name__, static_folder="../../static/dist",
            template_folder="../../static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stephenlow@localhost/karaoke-manager-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Song(db.Model):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    artist_name = Column(String(80), unique=True)
    description = Column(String(200))
    created_at = Column(DateTime, default=func.current_timestamp())
    deleted = Column(Boolean(), default=False)

    def __init__(self, name, artist_name, description):
        self.name = name
        self.artist_name = artist_name
        self.description = description

    def __repr__(self):
        return '<Song %r by %r>' % (self.name, self.artist_name)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.form:
        print(request.form)

    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
