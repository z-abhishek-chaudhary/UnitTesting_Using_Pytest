from tests.test3.Students import StudentDB
db = None

def setup_module(module):
    global db
    db = StudentDB()
    db.connect('/Users/Abhishek/MyPackage/Learning/PyTest_Demo/tests/test3/data.json')

def test_student1_data():
    student_data = db.get_data("Abhishek")
    assert student_data['id'] == 1 
    assert student_data['result'] == "pass"

def test_student2_data():
    student_data = db.get_data("Aman")
    assert student_data['id'] == 2
    assert student_data['result'] == "fail"