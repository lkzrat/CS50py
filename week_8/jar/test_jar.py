from jar import Jar
import pytest

def test_jarFormat():
    with pytest.raises(ValueError):
        test_jar = Jar('cat')

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

def test_depositError():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_depositFormat():
    jar = Jar(10)
    with pytest.raises(Exception):
        jar.deposit('cat')

def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    assert jar.size == 10
    jar.withdraw(5)
    assert jar.size == 5

def test_withdrawError():
    jar = Jar(10)
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.withdraw(11)

def test_withdrawFormat():
    jar = Jar(10)
    with pytest.raises(Exception):
        jar.withdraw('cat')

def test_str():
    jar = Jar(10)
    jar.deposit(5)
    assert str(jar) == '🍪🍪🍪🍪🍪'
