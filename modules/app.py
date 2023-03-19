from flask import Flask, redirect, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # make request and add token data to data base
        return redirect(f"/token/{request.form['name']}")
    return render_template('token.html')


@app.route('/token/<string:token>')
def count_page(token):
    # load data from data base
    return 'Count Page'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')