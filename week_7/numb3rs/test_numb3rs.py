from numb3rs import validate

def test_ip():
    assert validate('192.168.0.1') == True


def test_letters():
    assert validate('123.abx.234.1') == False


def test_nothing():
    assert validate('123..213.1') == False


def test_outofrange():
    assert validate('256.255.255.255') == False


def test_firstbyte():
    assert validate('192.266.266.266') == False