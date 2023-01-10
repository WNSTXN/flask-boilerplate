from importlib import import_module
from os import listdir

def initialise_routes():

    print('\nROUTES')

    [
        print(f' * {import_module(f"app.routes.{file_name[:-3]}").__name__} route found') 
        for file_name in listdir('app/routes')
        if file_name != '__init__.py' and file_name.endswith('.py')
    ]

    print('')
