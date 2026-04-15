import pytest
from soal1 import hitung_nilai_akhir, tentukan_grade

# ==============================
# TEST VALID INPUT
# ==============================
def test_valid_input():
    """Test perhitungan dengan input valid"""
    # 0.3*80 + 0.3*80 + 0.4*80 = 80
    assert hitung_nilai_akhir(80, 80, 80) == 80

def test_valid_float_input():
    """Test perhitungan dengan input float"""
    hasil = hitung_nilai_akhir(50.5, 60.7, 70.2)
    assert isinstance(hasil, float)

# ==============================
# TEST BOUNDARY
# ==============================
def test_boundary_min():
    """Test batas minimum (nilai 0)"""
    assert hitung_nilai_akhir(0, 0, 0) == 0

def test_boundary_max():
    """Test batas maksimum (nilai 100)"""
    assert hitung_nilai_akhir(100, 100, 100) == 100

def test_boundary_min_plus_one():
    """Test minimum + 1"""
    hasil = hitung_nilai_akhir(1, 1, 1)
    assert hasil == pytest.approx(1.0)

def test_boundary_max_minus_one():
    """Test maksimum - 1"""
    hasil = hitung_nilai_akhir(99, 99, 99)
    assert hasil == pytest.approx(99.0)

# ==============================
# TEST INVALID INPUT
# ==============================
def test_invalid_below_min():
    """Test nilai di bawah batas minimum (-1)"""
    with pytest.raises(ValueError):
        hitung_nilai_akhir(-1, 50, 50)

def test_invalid_above_max():
    """Test nilai di atas batas maksimum (101)"""
    with pytest.raises(ValueError):
        hitung_nilai_akhir(50, 50, 101)

def test_invalid_string_input():
    """Test input berupa string"""
    with pytest.raises(ValueError):
        hitung_nilai_akhir("A", 50, 60)

def test_invalid_none_input():
    """Test input None"""
    with pytest.raises(ValueError):
        hitung_nilai_akhir(None, 50, 60)

# ==============================
# TEST GRADE
# ==============================
def test_grade_A():
    """Test grade A (nilai >= 85)"""
    assert tentukan_grade(90) == "A"
    assert tentukan_grade(85) == "A"
    assert tentukan_grade(100) == "A"

def test_grade_B():
    """Test grade B (75 <= nilai <= 84)"""
    assert tentukan_grade(75) == "B"
    assert tentukan_grade(80) == "B"
    assert tentukan_grade(84) == "B"

def test_grade_C():
    """Test grade C (65 <= nilai <= 74)"""
    assert tentukan_grade(65) == "C"
    assert tentukan_grade(70) == "C"
    assert tentukan_grade(74) == "C"

def test_grade_D():
    """Test grade D (50 <= nilai <= 64)"""
    assert tentukan_grade(50) == "D"
    assert tentukan_grade(60) == "D"
    assert tentukan_grade(64) == "D"

def test_grade_E():
    """Test grade E (nilai < 50)"""
    assert tentukan_grade(40) == "E"
    assert tentukan_grade(0) == "E"
    assert tentukan_grade(49) == "E"
