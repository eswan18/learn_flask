import flask, flask_bootstrap, flask_moment, flask_wtf, wtforms
from flask import Flask, session, redirect, url_for, render_template, flash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dummy_key'
bootstrap = flask_bootstrap.Bootstrap(app)
moment = flask_moment.Moment(app)

# Name Form
class NameForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('What is your name?',
                                validators=[wtforms.validators.Required()])
    submit = wtforms.SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form,
                                 name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
