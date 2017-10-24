import flask, flask_bootstrap

app = flask.Flask(__name__)
bootstrap = flask_bootstrap.Bootstrap(app)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return flask.render_template('user.html', name=name)

@app.route('/user2/<name>')
def user2(name):
    return flask.render_template('user2.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
