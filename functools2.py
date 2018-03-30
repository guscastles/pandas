"""
Module with functional programming tools
"""


def immutable(func):
    'Decorator that guarantees the immutability of the dataframe'

    def __wrapper__(*args):
        return func(args[0][:])

    return __wrapper__
