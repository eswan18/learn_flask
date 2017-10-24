import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return flask.render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
