# import pytest
from pytest_understanding.classes.SomeClass import SomeClass

class Tests():
    def test_one(self):
        x = SomeClass()
        assert x.greatings() == 'Hello'

    def test_two(self):
        x = SomeClass()
        assert x.greatings('Bob') == 'Hello, Bob'
