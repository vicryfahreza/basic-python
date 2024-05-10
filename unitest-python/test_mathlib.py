import mathlib
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3,9), reason="I dont want run this test at the moment")
def test_calc_total():
    total = mathlib.calc_total(3,6)
    assert total == 9

def test_calc_multiply():
    total = mathlib.calc_multiply(6,10)
    assert total == 60

def test_dummy():
    assert True

# to run from module
# py.test

# to run test with reason
# py.test -v -rsx

# to run specific function test
# pytest -k calc -v
