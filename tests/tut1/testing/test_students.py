from datetime import datetime
import pytest

from tests.tut1.myapp.Students import Student, get_topper


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20

def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("Abhishek", 95),
        make_dummy_student("Raman", 89),
        make_dummy_student("Bhupender", 93),
        make_dummy_student("Sunny", 19)
    ]

    topper = get_topper(students) 

    assert topper == students[0]