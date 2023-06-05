from twttr import shorten


def test_default():
    assert shorten('') == ''


def test_novowel():
    assert shorten('hmmm') == 'hmmm'


def test_lower():
    assert shorten('twitter') == 'twttr'


def test_upper():
    assert shorten('TWITTER') == 'TWTTR'


def test_low_and_up():
    assert shorten('Twitter') == 'Twttr'


def test_num():
    assert shorten('twitter123') == 'twttr123'


def test_symbol():
    assert shorten('twitter$@!') == 'twttr$@!'