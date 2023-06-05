from um import count

def test_um():
    assert count('hello, um, world') == 1


def test_case():
    assert count('hello, Um, world') == 1


def test_WordWithUm():
    assert count('yummy') == 0