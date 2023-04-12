import sys
import pytest

@pytest.mark.xfail
def test_greater():
    n = 100
    assert n >20

@pytest.mark.xfail
def test_greater_equals():
    n = 100
    assert n >=100

@pytest.mark.skip(reason="Just skip this test")
def test_lesser():
    n = 99
    assert n < 23

@pytest.mark.skipif(sys.version_info > (3,10), reason="Use Python 3.10 or later")
def test_lesser2():
    n = 99
    assert n > 23