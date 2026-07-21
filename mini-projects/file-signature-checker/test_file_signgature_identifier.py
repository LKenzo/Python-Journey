import pytest
import file_signature_identifier as signature

def test_file_opener():
    with pytest.raises(SystemExit):
        signature.file_opener("")
    with pytest.raises(SystemExit):
        signature.file_opener("test")
    with pytest.raises(SystemExit):
        signature.file_opener("file.txt")
    with pytest.raises(SystemExit):
        signature.file_opener("py.")

def test_file_identifier():
    assert signature.file_identifier("FFD8FFE0") #jpg
    assert signature.file_identifier("FFD8FFE1") == None
    assert signature.file_identifier("89504E") == None
    assert signature.file_identifier("FFFE") == None
    assert signature.file_identifier("") == None
