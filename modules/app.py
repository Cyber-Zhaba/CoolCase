from flask import Flask, redirect, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # make request and add token data to data base
        return redirect(f"/token/{request.form['name']}")
    return render_template('token.html')


class EditPointForm(FlaskForm):
    SH = StringField('SH')
    fuel = StringField('Топливо')

class SmolForm(FlaskForm):
    point = StringField('point')


@app.route('/token/<string:token>', methods=['GET', 'POST'])
def count_page(token):
    # load data from data base
    form = EditPointForm(SH=120)
    form_1 = SmolForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(2)
        if form_1.validate_on_submit():
            print(1)
        # update data
    return render_template('info.html', form=form, form_1=form_1)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')