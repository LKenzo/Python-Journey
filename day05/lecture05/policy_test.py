from day05.lecture05.policy import check_password

def test_valid_password():
    assert check_password("GoodPassword!") == True

def test_short_password():
    assert check_password("test!") == False

def test_missing_symbol_password():
    assert check_password("badpassword") == False