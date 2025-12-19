import os
import sys


# Ensure src/ is importable
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)

from app.calculations import parse_int, multiply, divide
import pytest


def test_parse_int_valid():
    assert parse_int("3") == 3


def test_parse_int_missing():
    with pytest.raises(ValueError):
        parse_int(None)


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide_integral():
    assert divide(6, 3) == 2


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
