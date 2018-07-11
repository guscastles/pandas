"""
Module to test functional programming style pattern matching.
"""
from pprint import pprint
from functools import reduce


def test(*args, **kwargs):
    arg_resp = [one(param) for param in args if len(args) == 1 and not kwargs]
    kwarg_resp = [kone(one=value) for key, value in kwargs.items() if key == 'one' and not args]
    return reduce(lambda a, b: f'{a}{b}', arg_resp + kwarg_resp) if arg_resp or kwarg_resp else None


def kone(one=''):
    return one


def one(that_is_one):
    return that_is_one


if __name__ == '__main__':
    pprint(test(1))
    pprint(test(one=1.0))
    pprint(test())
    pprint(test(1, 2))
