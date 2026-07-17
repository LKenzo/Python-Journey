import pytest
from sanitizer import url_sanitizer

def test_url():
    url_sanitizer("http://youtube.com")
    
    with pytest.raises(ValueError):
        url_sanitizer("notvalidurl")

def test_dot_url():
    with pytest.raises(ValueError):
        url_sanitizer("www.youtube.zzz")
    
    with pytest.raises(ValueError):
        url_sanitizer("roblox.")

    with pytest.raises(ValueError):
        url_sanitizer("google    .com")

    with pytest.raises(ValueError):
        url_sanitizer("non://google    .")

    