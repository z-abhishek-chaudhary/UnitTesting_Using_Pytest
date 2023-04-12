import pytest


def test_divisible_by_3(input_data):
    assert input_data % 3 == 0


def test_divisible_by_9(input_data):
    assert input_data % 9 == 0


@pytest.mark.parametrize("num, output",[(1,11),(2,22),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output



