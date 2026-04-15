import matplotlib.pyplot as plt


def cek_kelulusan(kehadiran, nilai_akhir, pembayaran):

    if kehadiran < 75:
        return "TIDAK LULUS"
    if pembayaran != "Lunas":
        return "TIDAK LULUS"
    if nilai_akhir < 60:
        return "TIDAK LULUS"
    return "LULUS"


def print_decision_table():

    print("\n=== DECISION TABLE KELULUSAN ===")
    print(f"{'Kondisi/Aksi':<30} {'R1':<6} {'R2':<6} {'R3':<6} {'R4':<6} {'R5':<6} {'R6':<6} {'R7':<6} {'R8':<6}")
    print("-" * 80)
    print(f"{'C1: Kehadiran >= 75%':<30} {'T':<6} {'T':<6} {'T':<6} {'T':<6} {'F':<6} {'F':<6} {'F':<6} {'F':<6}")
    print(f"{'C2: Nilai Akhir >= 60':<30} {'T':<6} {'T':<6} {'F':<6} {'F':<6} {'T':<6} {'T':<6} {'F':<6} {'F':<6}")
    print(f"{'C3: Pembayaran = Lunas':<30} {'T':<6} {'F':<6} {'T':<6} {'F':<6} {'T':<6} {'F':<6} {'T':<6} {'F':<6}")
    print("-" * 80)
    print(f"{'A1: LULUS':<30} {'✓':<6} {'-':<6} {'-':<6} {'-':<6} {'-':<6} {'-':<6} {'-':<6} {'-':<6}")
    print(f"{'A2: TIDAK LULUS':<30} {'-':<6} {'✓':<6} {'✓':<6} {'✓':<6} {'✓':<6} {'✓':<6} {'✓':<6} {'✓':<6}")
    print()
    print("Keterangan: T=True, F=False, ✓=Aksi yang dijalankan")
    print()
    print("Penyederhanaan Decision Table:")
    print("- Rule R2, R3, R4, R5, R6, R7, R8 semuanya menghasilkan TIDAK LULUS")
    print("- Dapat disederhanakan: jika SEMUA kondisi True -> LULUS, selainnya TIDAK LULUS")
    print()
    print("Decision Table Sederhana:")
    print(f"{'Kondisi/Aksi':<30} {'R1':<12} {'R2 (else)':<12}")
    print("-" * 56)
    print(f"{'C1: Kehadiran >= 75%':<30} {'T':<12} {'F / -':<12}")
    print(f"{'C2: Nilai Akhir >= 60':<30} {'T':<12} {'F / -':<12}")
    print(f"{'C3: Pembayaran = Lunas':<30} {'T':<12} {'F / -':<12}")
    print("-" * 56)
    print(f"{'A1: LULUS':<30} {'✓':<12} {'-':<12}")
    print(f"{'A2: TIDAK LULUS':<30} {'-':<12} {'✓':<12}")


def run_tests():
    print("\n=== TEST KELULUSAN ===")
    print(f"{'No':<4} {'Kehadiran':<12} {'Nilai':<8} {'Pembayaran':<16} {'Expected':<15} {'Hasil':<15} {'Status'}")
    print("-" * 90)

    test_cases = [
        # (kehadiran, nilai, pembayaran, expected)
        (80, 70, "Lunas",       "LULUS",       "Rule R1: semua syarat terpenuhi"),
        (70, 80, "Lunas",       "TIDAK LULUS", "Rule R5: kehadiran < 75"),
        (80, 50, "Lunas",       "TIDAK LULUS", "Rule R3: nilai < 60"),
        (80, 80, "Tidak Lunas", "TIDAK LULUS", "Rule R2: pembayaran tidak lunas"),
        (75, 60, "Lunas",       "LULUS",       "Boundary: semua pas batas minimal"),
        (74, 100, "Lunas",      "TIDAK LULUS", "Boundary: kehadiran 74 (< 75)"),
        (75, 59, "Lunas",       "TIDAK LULUS", "Boundary: nilai 59 (< 60)"),
        (100, 100, "Lunas",     "LULUS",       "Rule R1: semua nilai maksimal"),
    ]

    results = []
    for i, (k, n, p, expected, desc) in enumerate(test_cases, 1):
        hasil = cek_kelulusan(k, n, p)
        results.append(hasil)
        status = "PASS ✓" if hasil == expected else "FAIL ✗"
        print(f"{i:<4} {k:<12} {n:<8} {p:<16} {expected:<15} {hasil:<15} {status} - {desc}")

    passed = sum(1 for i, (k, n, p, expected, _) in enumerate(test_cases)
                 if results[i] == expected)
    print(f"\nTotal: {passed}/{len(test_cases)} test case berhasil")
    return results

# =========================
# VISUALISASI
# =========================
def visualize(results):
    count = {"LULUS": 0, "TIDAK LULUS": 0}
    for r in results:
        count[r] += 1

    plt.figure(figsize=(8, 5))
    colors = ['#4CAF50' if k == 'LULUS' else '#F44336' for k in count.keys()]
    bars = plt.bar(count.keys(), count.values(), color=colors, edgecolor='black')
    plt.title("Distribusi Kelulusan")
    plt.xlabel("Status")
    plt.ylabel("Jumlah")
    for bar, val in zip(bars, count.values()):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                 str(val), ha='center', va='bottom', fontweight='bold')
    plt.tight_layout()
    plt.savefig("distribusi_kelulusan.png")
    plt.show()

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    print_decision_table()
    hasil = run_tests()
    visualize(hasil)
