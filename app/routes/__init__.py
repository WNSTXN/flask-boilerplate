from app.routes.index import index


def initialise_routes():

    [print(f'Initialising {route.__name__} route') for route in (
        index
    )]
