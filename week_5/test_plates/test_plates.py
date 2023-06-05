from plates import is_valid


def test_letters():
    assert is_valid('123456') == False


def test_len():
    assert is_valid('AB1234567') == False
    assert is_valid('A') == False


def test_numpos():
    assert is_valid('AB123C') == False


def test_0pos():
    assert is_valid('AB0123') == False


def test_symbol():
    assert is_valid('CS!4') == False