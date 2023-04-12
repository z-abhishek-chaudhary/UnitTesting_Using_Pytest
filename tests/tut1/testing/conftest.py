from tests.tut1.myapp.Students import Student
from datetime import datetime
import pytest

@pytest.fixture
def dummy_student():
    return Student("Abhishek", datetime(2002, 2, 14), "CSE", 20)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name,credits):
        return Student(name,datetime(2002, 2, 14), "CSE", credits)
    return _make_dummy_student