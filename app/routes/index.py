from flask import render_template

from app import App


@App.route('/')
def index() -> str:

    return render_template('index.html')
