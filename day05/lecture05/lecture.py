import pytest

def main():
    test_square()
    test_str()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

def test_str():
    with pytest.raises(TypeError):
        square("cat")

def square(num):
    return num * num

if __name__ == "__main__":
    main()