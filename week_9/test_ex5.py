import pytest

@pytest.mark.smoke
def test_case1():
    assert False

@pytest.mark.slow
def test_case2():
    assert True   

@pytest.mark.regression
def test_case3():
    assert True

@pytest.mark.smoke
def test_case4():
    assert True
