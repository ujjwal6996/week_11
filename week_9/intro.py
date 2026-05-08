#standard naming conventions
1- filename- start or end with test_ or _test
2- function names should be started with test keyword
3- class name should be started with Testxxxx

#pytest running

1- pytest test_ex2.py
2- pytest .
3- pytest test_ex2.py -v 
4- pytest -k "increment"
5- pytest test_ex2.py::test_increment
6- pytest
#markers
applying some metadata on test functions, classes
built-in markers:
    @pytest.mark.skip
    @pytest.mark.skipif
    @pytest.mark.parameterize

# user define markers for frouping testing modules