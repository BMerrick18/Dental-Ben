from src.services import patient_details
from datetime import date


#test the validate_sex function

def test_validate_sex_male():
    assert patient_details.validate_sex("m") == "male"
    assert patient_details.validate_sex("male") == "male"

def test_validate_sex_female():
    assert patient_details.validate_sex("f") == "female"
    assert patient_details.validate_sex("female") == "female"
    
def test_validate_sex_invalid():
    assert patient_details.validate_sex("") is None
    assert patient_details.validate_sex("x") is None
    assert patient_details.validate_sex("invalid") is None
    assert patient_details.validate_sex("9") is None
    assert patient_details.validate_sex("males") is None

#test the validate_date_of_birth function

def test_validate_date_of_birth_valid():
    assert patient_details.validate_date_of_birth("2000-01-01") == date(2000, 1, 1)
    assert patient_details.validate_date_of_birth("2000-12-31") == date(2000, 12, 31)
    assert patient_details.validate_date_of_birth("2000-02-29") == date(2000, 2, 29)

def test_validate_date_of_birth_invalid():
    assert patient_details.validate_date_of_birth("") is None
    assert patient_details.validate_date_of_birth("2000-01-01-01") is None
    assert patient_details.validate_date_of_birth("2000-13-01") is None
    assert patient_details.validate_date_of_birth("hello") is None

