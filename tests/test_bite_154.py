from dataclasses import astuple, replace

import pytest

from bites.oop.bite_154 import Bite


@pytest.fixture()
def bites():
    b1 = Bite(number=1, title="sum of numbers")
    b2 = Bite(number=2, title="a second bite", level="Intermediate")
    b3 = Bite(number=3, title="a hard bite", level="Advanced")
    bites = [b1, b2, b3]
    return bites


def test_type_annotations():
    assert Bite.__annotations__ == {'number': int, 'title': str, 'level': str}


def test_getting_str_for_free(bites):
    expected = Bite(number=1, title='Sum of numbers', level='Beginner')
    assert bites[0] == expected