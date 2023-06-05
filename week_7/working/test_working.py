from working import convert
import pytest

def test_2dots():
    assert convert('6:30 AM to 5:00 PM') == '06:30 to 17:00'
    assert convert('8:00 PM to 6:00 AM') == '20:00 to 06:00'


def test_no2dots():
    assert convert('6 AM to 5 PM') == '06:00 to 17:00'
    assert convert('8 PM to 6 AM') == '20:00 to 06:00'


def test_invalid2dots_minutes():
    with pytest.raises(ValueError):
        convert('12:00 AM to 5:68 PM')


def test_invalid2dots_hours():
    with pytest.raises(ValueError):
        convert('14:00 AM to 5:00 PM')

def test_invalidNo2dots():
    with pytest.raises(ValueError):
        convert('14 AM to 5 PM')


def test_invalidformat():
     with pytest.raises(ValueError):
        convert('11AM to 9PM')

def test_to():
    with pytest.raises(ValueError):
        convert('11 AM 9 PM')