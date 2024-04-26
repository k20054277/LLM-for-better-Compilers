#!/usr/bin/env python

import pytest

def test_as():
    # Test the 'as' keyword
    assert 1 == 1, "The values should be equal"
    assert 2 != 3, "The values should not be equal"

def test_pytest():
    # Test using pytest
    assert 4 == 4, "The values should be equal"
    assert 5 > 3, "The first value is greater than the second"