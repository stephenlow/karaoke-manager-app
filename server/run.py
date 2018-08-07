from app import create_app
from flask import request, render_template

app = create_app('config')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.form:
        print(request.form)

    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
