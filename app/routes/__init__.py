from importlib import import_module
from os import listdir


def import_route(file_name: str):
    """
    Summary
    -------
    import a route module

    Parameters
    ----------
    file_name (str) : name of the route module to import
    """
    module_name = import_module(f"app.routes.{file_name[:-3]}").__name__
    print(f' * {module_name} route found')


def initialise_routes():
    """
    Summary
    -------
    import all route modules
    """
    print('\nROUTES')

    module_names = (
        file_name for file_name in listdir('app/routes')
        if not file_name.startswith('__init__') and file_name.endswith('.py')
    )

    list(map(import_route, module_names))

    print('')
