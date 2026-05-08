import pytest
import sys
@pytest.mark.skip(reason="not implemented yet")
def test_db_func():
    assert False

@pytest.mark.skipif(sys.platform=="win64",reason="it does not work on windows")
def test_os_files():
    assert True

@pytest.mark.parametrize("a,b,p",[(5,2,10),(7,3,21),(9,5,45)])
def test_prod(a,b,p):
    assert a*b==p
