import student as student

# ---------- Average Calculation ----------
def test_calculate_average():
    assert student.calculate_average(85, 90, 95) == 90.0


# ---------- Grade S (90–100) ----------
def test_grade_S_lower_boundary():
    assert student.calculate_grade(90) == "S"

def test_grade_S_middle_value():
    assert student.calculate_grade(95) == "S"

def test_grade_S_upper_boundary():
    assert student.calculate_grade(100) == "S"


# ---------- Grade A (80–89) ----------
def test_grade_A_lower_boundary():
    assert student.calculate_grade(80) == "A"

def test_grade_A_middle_value():
    assert student.calculate_grade(85) == "A"

def test_grade_A_upper_boundary():
    assert student.calculate_grade(89) == "A"


# ---------- Grade B (65–79) ----------
def test_grade_B_lower_boundary():
    assert student.calculate_grade(65) == "B"

def test_grade_B_middle_value():
    assert student.calculate_grade(70) == "B"

def test_grade_B_upper_boundary():
    assert student.calculate_grade(79) == "B"


# ---------- Grade C (50–64) ----------
def test_grade_C_lower_boundary():
    assert student.calculate_grade(50) == "C"

def test_grade_C_middle_value():
    assert student.calculate_grade(55) == "C"

def test_grade_C_upper_boundary():
    assert student.calculate_grade(64) == "C"


# ---------- Grade D (40–49) ----------
def test_grade_D_lower_boundary():
    assert student.calculate_grade(40) == "D"

def test_grade_D_middle_value():
    assert student.calculate_grade(45) == "D"

def test_grade_D_upper_boundary():
    assert student.calculate_grade(49) == "D"


# ---------- Grade F (Below 40) ----------
def test_grade_F_below_40():
    assert student.calculate_grade(39) == "F"
