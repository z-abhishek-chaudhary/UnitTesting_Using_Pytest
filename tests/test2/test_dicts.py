import pytest
from sample_data import testing_dicts
from tests.test2.main import genrate_report

@pytest.mark.parametrize("dict" , testing_dicts)
def test_dict_1(dict):

    assert dict.get("id") > 0, f"The given id: {dict.get('id')} is not available in the database"
    assert len(dict.get("name")) > 0, f"The name field is empty"
    assert len(dict.get("subjects")) == 3, f"At student id: {dict['id']} number of subjects are {len(dict['subjects'])} but it shuld be 3"
    assert dict.get("average") > 60, f"The student with id: {dict['id']} have less average marks than 60"


@pytest.mark.parametrize("dict" , testing_dicts)
def test_dict_2(dict):
    errors = []
 
    # Testing if all the subjects are available or not 
    if not len(dict.get("subjects")) == 3:
        errors.append(f"At student id {dict['id']}, number of subjects are {len(dict['subjects'])} but it should be 3")

    # Testing if the average is greater than 60
    if not dict.get("average") > 60:
        errors.append(f"The student with id {dict['id']} have average marks {dict['average']} which is less than 60")

    # Testing if the average is correct or not.
    if len(dict.get("subjects")) == 3:
        sum = 0
        for subj in dict['subjects']:
            sum = sum + dict['subjects'][subj]
        sum = sum/3
        print(sum)
        if not int(sum) == int(dict['average']):
            errors.append("The average provided is incorrect the correct average is {sum}")

    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


@pytest.mark.parametrize("dict" , testing_dicts)
def test_dict_2_function(dict):
    assert dict['average'] > 0
    assert genrate_report(dict) in ["Excellent", "Very Good", "Good"]
