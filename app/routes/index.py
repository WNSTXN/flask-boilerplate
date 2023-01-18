from flask import render_template

from app import App


@App.route('/')
def index() -> str:
    """
    Summary
    -------
    render the index page
    """
    return render_template('index.html')
