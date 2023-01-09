from typing import Literal

from flask import Flask
from flask_cors import CORS
from waitress import serve

from app.config import Config


class App:

    HTTPMethods = Literal['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
    flask = Flask(__name__)
    CORS(flask)

    config = flask.config
    config.from_object(Config)
    config['CORS_HEADERS'] = 'Content-Type'

    get = flask.get
    post = flask.post
    put = flask.put
    delete = flask.delete
    patch = flask.patch


    def run(debug: bool | None, load_dotenv: bool=True, **options):

        if not debug:
            print(f'Waitress serving on http://{App.config["HOST"]}:{App.config["PORT"]}')
            serve(App.flask, host=App.config['HOST'], port=App.config['PORT'])
            return
        
        App.flask.run(
            host=App.config['HOST'],
            port=App.config['PORT'],
            debug=debug, 
            load_dotenv=load_dotenv, 
            **options
        )


    def route(rule: str, methods: list[HTTPMethods]=['GET'], **options):

        return App.flask.route(rule, methods=methods, **options)
