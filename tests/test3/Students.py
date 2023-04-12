import json


class StudentDB:
    def __init__(self):
        self._data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self._data = json.load(json_file)
    
    def get_data(self,name):
        for student in self._data['students']:
            if student['name'] == name:
                return student
            