"""
Tests for `pytestpackage` module.
"""
import pytest
from pytestpackage import pytestpackage

def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5


class TestPytestpackage(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass
