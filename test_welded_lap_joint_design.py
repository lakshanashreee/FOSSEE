from welded_lap_joint_design import design_lap_joint

# Define test functions
def test_valid_lap_joint_design():
    result = design_lap_joint(P=50, w=200, t1=10, t2=8)
    assert result["Weld Size (mm)"] == 7  # Min thickness (t2) - 1 mm
    assert result["Weld Material Grade"] == "E250"
    assert result["Length of Weld (mm)"] > 0
    assert result["Strength of Connection (N)"] > 0
    assert result["Plate 1 Yield Strength (N)"] == 250 * 10 * 200
    assert result["Plate 2 Yield Strength (N)"] == 250 * 8 * 200
    assert 0 <= result["Efficiency of Connection"] <= 1
    print("test_valid_lap_joint_design passed")

def test_invalid_force():
    try:
        design_lap_joint(P=-10, w=200, t1=10, t2=8)
        print("test_invalid_force failed")
    except ValueError as e:
        assert str(e) == "Tensile force must be positive."
        print("test_invalid_force passed")

def test_invalid_plate_width():
    try:
        design_lap_joint(P=50, w=-200, t1=10, t2=8)
        print("test_invalid_plate_width failed")
    except ValueError as e:
        assert str(e) == "Plate width must be positive."
        print("test_invalid_plate_width passed")

def test_invalid_plate_thickness():
    try:
        design_lap_joint(P=50, w=200, t1=-10, t2=8)
        print("test_invalid_plate_thickness failed")
    except ValueError as e:
        assert str(e) == "Plate thickness must be positive."
        print("test_invalid_plate_thickness passed")

def test_efficiency_with_high_force():
    result = design_lap_joint(P=200, w=300, t1=15, t2=12)
    assert result["Efficiency of Connection"] <= 1
    assert result["Strength of Connection (N)"] > result["Plate 1 Yield Strength (N)"]
    print("test_efficiency_with_high_force passed")

def test_nearest_round_length():
    result = design_lap_joint(P=100, w=250, t1=12, t2=10)
    assert result["Length of Weld (mm)"] % 10 == 0  # Rounded to nearest 10 mm
    print("test_nearest_round_length passed")

# Test edge cases
def test_minimal_input_values():
    result = design_lap_joint(P=1, w=10, t1=1, t2=1)
    assert result["Weld Size (mm)"] == 0  # Throat thickness reduced for minimal t1 or t2
    assert result["Length of Weld (mm)"] > 0
    assert result["Efficiency of Connection"] <= 1
    print("test_minimal_input_values passed")

# Run tests
if __name__ == "__main__":
    try:
        test_valid_lap_joint_design()
        test_invalid_force()
        test_invalid_plate_width()
        test_invalid_plate_thickness()
        test_efficiency_with_high_force()
        test_nearest_round_length()
        test_minimal_input_values()
        print("\nAll tests passed!")
    except AssertionError:
        print("\nSome tests failed.")
