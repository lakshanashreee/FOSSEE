import math

# Define material grade properties as per IS800:2007 and IS2062:2011
grade_yield_strengths = {
    "E250": 250,  # MPa
    "E275": 275,
    "E300": 300,
    "E350": 350,
    "E410": 410
}

# Define design constants
partial_safety_factor = 1.25  # for weld material as per IS 800:2007

# Function to calculate weld strength
def calculate_weld_strength(size, length, material_grade):
    # Weld shear strength (as per IS 800:2007)
    weld_strength = (grade_yield_strengths[material_grade] / math.sqrt(3)) / partial_safety_factor
    return weld_strength * size * length

# Function to design a lap joint
def design_lap_joint(P, w, t1, t2):
    """
    P: Tensile force in kN
    w: Plate width in mm
    t1, t2: Plate thicknesses in mm
    """
    # Validate inputs
    if P <= 0:
        raise ValueError("Tensile force must be positive.")
    if w <= 0:
        raise ValueError("Plate width must be positive.")
    if t1 <= 0 or t2 <= 0:
        raise ValueError("Plate thickness must be positive.")
    
    # Convert tensile force to N (1 kN = 1000 N)
    P = P * 1000

    # Yield strengths of plates
    plate1_yield = grade_yield_strengths["E250"] * t1 * w  # Example plate grade: E250
    plate2_yield = grade_yield_strengths["E250"] * t2 * w  # Example plate grade: E250

    # Weld size selection (as per IS 800:2007, t_min = t1 or t2)
    weld_size = min(t1, t2) - 1  # Assuming a 1 mm reduction for throat thickness

    # Length of weld required
    material_grade = "E250"  # Example weld material grade
    weld_strength = calculate_weld_strength(weld_size, 1, material_grade)  # Per mm
    length_of_weld = P / weld_strength

    # Round to nearest 10 mm for practical purposes
    length_of_weld = math.ceil(length_of_weld / 10) * 10

    # Connection efficiency (utilization ratio)
    connection_strength = calculate_weld_strength(weld_size, length_of_weld, material_grade)
    efficiency = connection_strength / max(plate1_yield, plate2_yield)

    # Output results
    return {
        "Weld Size (mm)": weld_size,
        "Weld Material Grade": material_grade,
        "Length of Weld (mm)": length_of_weld,
        "Strength of Connection (N)": connection_strength,
        "Plate 1 Yield Strength (N)": plate1_yield,
        "Plate 2 Yield Strength (N)": plate2_yield,
        "Efficiency of Connection": round(efficiency, 2)
    }
