from seasons import get_date, min_alive

def test_correct():
    assert min_alive(str(get_date('2000-01-01') - get_date('1999-01-01'))) == 'Five hundred twenty-five thousand, six hundred minutes'