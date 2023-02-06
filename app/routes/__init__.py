from importlib import import_module
from os import listdir


def initialise_routes():
    """
    Summary
    -------
    import all route modules
    """
    print('\nROUTES')

    module_file_names = [
        file_name for file_name in listdir('app/routes')
        if not file_name.startswith('__init__') and file_name.endswith('.py')
    ]

    for file_name in module_file_names:
        module_name = import_module(f"app.routes.{file_name[:-3]}").__name__
        print(f' * {module_name} route found')

    print('')
