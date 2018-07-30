from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="../static/dist",
            template_folder="../static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://stephenlow@localhost/karaoke-manager-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    artist_name = db.Column(db.String(80), unique = True)

    def __init__(self, name, artist_name):
        self.name = name
        self.artist_name = artist_name

    def __repr__(self):
        return '<Song %r>' % self.name


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
