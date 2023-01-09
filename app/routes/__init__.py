from app.routes.index import index


def initialise_routes():

    print('\nROUTES')
    [print(f' * {route.__name__} route found') for route in [
        index
    ]]
    print('')
