# app.py is code to run the app ui

from flask import Flask, render_template

app = Flask(__name__)
# line to prevent cache from not updating static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/coming_soon')
def coming_soon_tm():
    return render_template('coming_soon_tm.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
