import pytest
from validate_osi import check_misspelled_keys, check_invalid_values, check_numeric_values

def test_misspelled_keys():
    errors = {"Misspelled Keys": []}
    sample_data = {"Blt.Diameter": 12, "Modle": "TestModel"}
    check_misspelled_keys(sample_data, errors)
    assert errors["Misspelled Keys"] == ["Blt.Diameter -> Bolt.Diameter", "Modle -> Module"]

def test_invalid_values():
    errors = {"Invalid Values": []}
    sample_data = {"Bolt": {"Bolt_Hole_Type": "WrongType"}}
    check_invalid_values(sample_data, errors)
    assert "Bolt.Bolt_Hole_Type = 'WrongType'" in errors["Invalid Values"][0]

def test_numeric_values():
    errors = {"Invalid Numeric Values": []}
    sample_data = {"Detailing": {"Gap": 60}, "Load": {"Axial": "invalid"}}
    check_numeric_values(sample_data, errors)
    assert "Detailing.Gap = 60 (Out of range: 0 to 50)" in errors["Invalid Numeric Values"][0]
    assert "Load.Axial = 'invalid' (Expected: Numeric value)" in errors["Invalid Numeric Values"][1]
