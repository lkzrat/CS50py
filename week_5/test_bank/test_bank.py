from bank import value


def test_hello():
    assert value('hello') == 0


def test_hword():
    assert value('hi, how are you?') == 20


def test_noh():
    assert value('What\'s up?') == 100


def test_case():
    assert value('hello') == value('Hello')