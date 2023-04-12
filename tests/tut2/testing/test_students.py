from datetime import datetime
import pytest
from tests.tut2.myapp.Students import is_eligible_for_degree


def test_student_get_age (dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age

@pytest.mark.parametrize("credits,expected",[(21,True), (11,False)])
def test_is_eligible_for_degree(make_dummy_student, credits, expected):
    assert is_eligible_for_degree(make_dummy_student("Abhi", credits)) is expected

@pytest.mark.parametrize("dummy_student,expected",[(21,True), (11,False)], indirect=["dummy_student"])
def test_is_eligible_for_degree_2(dummy_student, expected):
    assert is_eligible_for_degree(dummy_student) is expected