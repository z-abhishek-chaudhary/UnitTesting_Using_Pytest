import pytest
from tests.test1.main import add, age_validate


class TestSample1:
    @pytest.mark.parametrize("a,b,c", [(1,2,3),(5,"4",9),(10,95,45),("1","2","12"),(5,"4",9),("10","95","45"), ([1,2],[4],[1,2,4])])
    def test_add(self,a,b,c):
        assert add(a,b) == c
    

class TestSample2:
    @pytest.mark.parametrize("a",[10,0,-2])
    def test_age_validate(self,a):
        age_validate(a)

    
    def test_age_invalid(self):
        with pytest.raises(ValueError, match="Age cannot be Negative"):
            age_validate(-10)
       

class TestSample3:
    @pytest.mark.parametrize("dict", [{"id" : 1, "name": "Abhishek"},{"id" : 2, "name": ""}])
    def test_add(self,dict):
        assert len(dict.get("name")) > 0