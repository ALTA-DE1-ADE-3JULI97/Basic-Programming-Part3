# input
student_score = 80
nilai = float(input("Masukkan nilai: "))
nama = input("Masukkan nama mahasiswa: ")
# Process: Your Solution Code Here
if nilai >= 80 and nilai <= 100:
    deskripsi = "A"
elif nilai >= 65 and nilai <= 79:
    deskripsi = "B+"
elif nilai >= 50 and nilai <= 64:
    deskripsi = "B"
elif nilai >= 35 and nilai <= 49:
    deskripsi = "C"
elif nilai >= 0 and nilai <= 34:
    deskripsi = "D"
else:
    deskripsi = "Nilai tidak valid"

# Output "Nilai A"
print("Nama mahasiswa:", nama)
print("Deskripsi nilai:", deskripsi)