import flask, flask_bootstrap, flask_moment
from datetime import datetime

app = flask.Flask(__name__)
bootstrap = flask_bootstrap.Bootstrap(app)
moment = flask_moment.Moment(app)


@app.route('/')
def index():
    return flask.render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return flask.render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return flask.render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
