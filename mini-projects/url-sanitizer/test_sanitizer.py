import pytest
from sanitizer import url_sanitizer

@pytest.fixture
def tld_set():
    return {"com","org","gov","net"}

def test_url(tld_set):
    assert url_sanitizer("http://youtube.com", tld_set) == "youtube.com"
    
    with pytest.raises(ValueError):
        url_sanitizer("notvalidurl", tld_set)

def test_dot_url(tld_set):
    with pytest.raises(ValueError):
        url_sanitizer("www.youtube.zzz", tld_set)
    
    with pytest.raises(ValueError):
        url_sanitizer("roblox.", tld_set)

    with pytest.raises(ValueError):
        url_sanitizer("google    .com", tld_set)

    with pytest.raises(ValueError):
        url_sanitizer("non://google    .", tld_set)

    