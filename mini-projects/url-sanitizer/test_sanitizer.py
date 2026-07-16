import pytest
from sanitizer import url_sanitizer

def test_url():
    url_sanitizer("http://youtube.com")
    
    with pytest.raises(ValueError):
        url_sanitizer("notvalidurl")