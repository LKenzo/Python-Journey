import pytest
from scanner import validate_port

def test_port():
    with pytest.raises(ValueError):
        validate_port(0)
    with pytest.raises(ValueError):
        validate_port("gacor")