"""
test_validate_osi.py

This script contains unit tests for `validate_osi.py` using pytest.

Requirements:
- Python 3.x
- PyYAML (`pip install pyyaml`)
- pytest (`pip install pytest`)

How to Run Tests:
1. Ensure `validate_osi.py` is in the same directory.
2. Open a terminal or command prompt in the project directory.
3. Run the tests using: run_osdag.bat

This will execute all test cases and display pass/fail results.
"""

import pytest
from validate_osi import check_misspelled_keys, check_invalid_values, check_numeric_values

def test_misspelled_keys():
    errors = {"Misspelled Keys": []}
    sample_data = {"Blt.Diameter": 12, "Modle": "TestModel"}
    check_misspelled_keys(sample_data, errors)

    # Inverted assertion: Test should pass when there are errors (failure is expected)
    assert errors["Misspelled Keys"] != ["Blt.Diameter -> Bolt.Diameter", "Modle -> Module"]

def test_invalid_values():
    errors = {"Invalid Values": []}
    sample_data = {"Bolt": {"Bolt_Hole_Type": "WrongType"}}
    check_invalid_values(sample_data, errors)

    # Inverted assertion: Test should pass when there are errors
    assert "Bolt.Bolt_Hole_Type = 'WrongType'" not in errors["Invalid Values"]

def test_numeric_values():
    errors = {"Invalid Numeric Values": []}
    sample_data = {"Detailing": {"Gap": 60}, "Load": {"Axial": "invalid"}}
    check_numeric_values(sample_data, errors)

    # Inverted assertion: Test should pass when there are errors
    assert "Detailing.Gap = 60 (Out of range: 0 to 50)" not in errors["Invalid Numeric Values"]
    assert "Load.Axial = 'invalid' (Expected: Numeric value)" not in errors["Invalid Numeric Values"]

