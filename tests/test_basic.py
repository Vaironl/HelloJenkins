import pytest

def inc(x):
    return x+1

def tests_answer():
    assert inc(4) == 5