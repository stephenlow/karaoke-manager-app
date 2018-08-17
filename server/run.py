from app import create_app

app = create_app('config')


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
