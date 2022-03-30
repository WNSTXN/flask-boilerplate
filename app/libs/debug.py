from builtins import print as _print


def print(*args, **kwargs):
    '''
    Prints text to stdout.
    '''

    if 'flush' in kwargs:
        del kwargs['flush']

    _print(*args, **kwargs, flush=True)