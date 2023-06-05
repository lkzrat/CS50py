import pytest
from fuel import convert, gauge


def test_convert():
    assert convert('1/2') == 50


def test_division():
    with pytest.raises(ZeroDivisionError):
        convert('10/0')


def test_value():
    with pytest.raises(ValueError):
        convert('1.3/2')


def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'