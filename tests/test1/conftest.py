import datetime
import pytest
from Students import Student

@pytest.fixture
def input_data():
    return 10

@pytest.fixture
def dummy_student():
    return Student("nikhil", datetime(2000, 1, 1), "coe", 21)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name,datetime(2000,1,1),"coe", credits)
    
    return _make_dummy_student

