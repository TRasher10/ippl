import matplotlib.pyplot as plt

# =========================
# VALIDASI INPUT
# =========================
def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input harus numerik")
    if value < 0 or value > 100:
        raise ValueError("Input harus dalam range 0-100")
    return value

# =========================
# HITUNG NILAI AKHIR
# =========================
def hitung_nilai_akhir(tugas, uts, uas):
    tugas = validate_input(tugas)
    uts = validate_input(uts)
    uas = validate_input(uas)
    return 0.3 * tugas + 0.3 * uts + 0.4 * uas

# =========================
# MENENTUKAN GRADE
# =========================
def tentukan_grade(nilai):
    if nilai < 50:
        return "E"
    elif nilai <= 64:
        return "D"
    elif nilai <= 74:
        return "C"
    elif nilai <= 84:
        return "B"
    else:
        return "A"

# =========================
# BVA TESTING
# =========================
def run_bva_tests():
    # Boundary values: min=0, min+1=1, max-1=99, max=100, out-of-bound: -1 dan 101
    bva_values = [-1, 0, 1, 99, 100, 101]
    results = []

    print("=== BVA TESTING ===")
    for t in bva_values:
        for u in bva_values:
            for a in bva_values:
                try:
                    nilai = hitung_nilai_akhir(t, u, a)
                    grade = tentukan_grade(nilai)
                    results.append(nilai)
                    print(f"T:{t}, UTS:{u}, UAS:{a} -> {nilai:.2f} ({grade})")
                except Exception as e:
                    print(f"T:{t}, UTS:{u}, UAS:{a} -> ERROR: {e}")
    return results

# =========================
# MULTI-PARAMETER BOUNDARY TESTING
# =========================
def run_mpbt_tests():
    print("\n=== MULTI-PARAMETER BOUNDARY TESTING ===")

    nominal = 50
    boundaries = [0, 1, 99, 100]
    results = []

    # Variasi TUGAS
    for t in boundaries:
        try:
            nilai = hitung_nilai_akhir(t, nominal, nominal)
            grade = tentukan_grade(nilai)
            results.append(nilai)
            print(f"T:{t}, UTS:{nominal}, UAS:{nominal} → {nilai:.2f} ({grade})")
        except Exception as e:
            print(f"T:{t}, UTS:{nominal}, UAS:{nominal} → ERROR: {e}")

    # Variasi UTS
    for u in boundaries:
        try:
            nilai = hitung_nilai_akhir(nominal, u, nominal)
            grade = tentukan_grade(nilai)
            results.append(nilai)
            print(f"T:{nominal}, UTS:{u}, UAS:{nominal} → {nilai:.2f} ({grade})")
        except Exception as e:
            print(f"T:{nominal}, UTS:{u}, UAS:{nominal} → ERROR: {e}")

    # Variasi UAS
    for a in boundaries:
        try:
            nilai = hitung_nilai_akhir(nominal, nominal, a)
            grade = tentukan_grade(nilai)
            results.append(nilai)
            print(f"T:{nominal}, UTS:{nominal}, UAS:{a} → {nilai:.2f} ({grade})")
        except Exception as e:
            print(f"T:{nominal}, UTS:{nominal}, UAS:{a} → ERROR: {e}")

    return results

# =========================
# ROBUSTNESS TESTING
# =========================
def run_robust_tests():
    print("\n=== ROBUSTNESS TEST ===")

    tests = [
        (0, 0, 0),
        (100, 100, 100),
        (50.5, 60.7, 70.2),
        ("A", 50, 60),
        (None, 50, 60),
        (999, 50, 60)
    ]

    for t, u, a in tests:
        try:
            nilai = hitung_nilai_akhir(t, u, a)
            grade = tentukan_grade(nilai)
            print(f"{t}, {u}, {a} -> {nilai:.2f} ({grade})")
        except Exception as e:
            print(f"{t}, {u}, {a} -> ERROR: {e}")

# =========================
# VISUALISASI
# =========================
def visualize(results, mpbt_results=None):
    if not results:
        return

    # Gabungkan semua hasil jika mpbt disertakan
    all_results = results + (mpbt_results if mpbt_results else [])

    # Histogram distribusi nilai akhir
    plt.figure(figsize=(10, 5))
    plt.hist(all_results, bins=10, color='steelblue', edgecolor='black')
    plt.title("Distribusi Nilai Akhir")
    plt.xlabel("Nilai")
    plt.ylabel("Frekuensi")
    plt.tight_layout()
    plt.savefig("distribusi_nilai.png")
    plt.show()

    # Distribusi grade
    grades = [tentukan_grade(n) for n in all_results]
    grade_order = ["E", "D", "C", "B", "A"]
    grade_count = {g: 0 for g in grade_order}
    for g in grades:
        grade_count[g] = grade_count.get(g, 0) + 1

    plt.figure(figsize=(8, 5))
    plt.bar(grade_count.keys(), grade_count.values(), color='steelblue', edgecolor='black')
    plt.title("Distribusi Grade")
    plt.xlabel("Grade")
    plt.ylabel("Jumlah")
    plt.tight_layout()
    plt.savefig("distribusi_grade.png")
    plt.show()

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    hasil_bva = run_bva_tests()
    hasil_mpbt = run_mpbt_tests()
    run_robust_tests()
    # [FIX] Pass both BVA and MPBT results to visualize
    visualize(hasil_bva, hasil_mpbt)
