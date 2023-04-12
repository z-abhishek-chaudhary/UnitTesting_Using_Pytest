from unittest import mock
from tests.tut4.myapp.sample import silly

from tut4.myapp.sample import random_sum


@mock.patch('tests.tut4.myapp.sample.random.randint')
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3,5]

    assert random_sum() == 8


@mock.patch('tests.tut4.myapp.sample.time.time')
@mock.patch('tests.tut4.myapp.sample.random.randint')
@mock.patch('tests.tut4.myapp.sample.requests.get')
def test_silly(mock_request_get, mock_randint, mock_time):
    test_params = {
        "timestamp" : 123,
        "number" : 4
    }
    mock_randint.return_value = test_params['number']
    mock_time.return_value = test_params['timestamp']

    mock_request_get.return_value = mock.Mock(**{"status_code" : 200, "json.return_value" :{"args" : test_params}})

    assert silly() == test_params