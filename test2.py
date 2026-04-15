import pytest
from soal2 import cek_kelulusan

def test_lulus():
    """Rule R1: Semua kondisi terpenuhi -> LULUS"""
    assert cek_kelulusan(80, 70, "Lunas") == "LULUS"

def test_tidak_lulus_kehadiran():
    """Rule R5/R6/R7/R8: Kehadiran < 75 -> TIDAK LULUS"""
    assert cek_kelulusan(70, 80, "Lunas") == "TIDAK LULUS"

def test_tidak_lulus_nilai():
    """Rule R3/R4: Nilai < 60 -> TIDAK LULUS"""
    assert cek_kelulusan(80, 50, "Lunas") == "TIDAK LULUS"

def test_tidak_lulus_pembayaran():
    """Rule R2: Pembayaran tidak lunas -> TIDAK LULUS"""
    assert cek_kelulusan(80, 80, "Tidak Lunas") == "TIDAK LULUS"

def test_boundary_lulus():
    """Boundary: kehadiran=75, nilai=60, lunas -> LULUS (tepat di batas)"""
    assert cek_kelulusan(75, 60, "Lunas") == "LULUS"

def test_boundary_tidak_lulus_kehadiran():
    """Boundary: kehadiran=74 (satu di bawah batas) -> TIDAK LULUS"""
    assert cek_kelulusan(74, 100, "Lunas") == "TIDAK LULUS"

def test_boundary_tidak_lulus_nilai():
    """Boundary: nilai=59 (satu di bawah batas) -> TIDAK LULUS"""
    assert cek_kelulusan(75, 59, "Lunas") == "TIDAK LULUS"

def test_semua_tidak_terpenuhi():
    """Rule R8: Semua kondisi tidak terpenuhi -> TIDAK LULUS"""
    assert cek_kelulusan(50, 40, "Tidak Lunas") == "TIDAK LULUS"
