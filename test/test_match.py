"""
Testing the number of matched items in a list
given a pattern.
"""
import re
from functools import reduce, partial
import pytest


STRING_LIST = ['avocado', 'abacate', 'invocado', 'fruit', 'fruta', 'frutado']
PATTERN = r'^(.*(cado)|(fru).*)$'

@pytest.mark.wip
def test_match():
    import timeit
    assert match(PATTERN, STRING_LIST) == {'fru': 3, 'cado': 2}


def update(dictionary, matched_pattern):

    def _count_item(dictionary, item):
        return 1 if item not in dictionary else dictionary[item] + 1

    def _valid_item(item):
        return [element for element in item if element][-1]

    if matched_pattern:
        item = _valid_item(matched_pattern.groups())
        dictionary[item] = _count_item(dictionary, item)
    return dictionary


def match2(pattern, string_list):
    count_dict = {}
    for item in string_list:
        count_dict = update(count_dict, re.match(pattern, item))
    return count_dict


def match(pattern, string_list):
    """
    Counts the number of matches in the string list according to the pattern.
    A dictionary is returned with the number of matches for each sub-pattern.
    """

    def _match(str_list, count_dict):
        if not str_list:
            return count_dict
        return _match(str_list[1:], update(count_dict, re.match(pattern, str_list[0])))

    return _match(string_list, {})

