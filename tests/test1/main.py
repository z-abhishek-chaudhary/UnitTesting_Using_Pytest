def add(a,b):
    return a+b

def age_validate(age):
    if age < 0:
        raise ValueError("Age cannot be Negative")