# Setting Variabel Identitas
nim   = input("Masukkan NIM   :")
nama  = input("Masukkan Nama  :")
kelas = input("Masukkan Kelas :")
prodi = input("Masukkan Prodi :")

# Perhitungsn
phi=3.14
r = int(input("Masukkan Panjang Jari-Jari Lingkaran: "))

luas = phi*(r*r)
keliling = 2*phi*r
# Setting Variabel
kalimat = ["UNISS","di","belajar","pada","Mahasiswa","Pemrograman","ruang","lab","Algoritma","semester","topik","Data","tipe","dan","dengan","Batang",2]

print("------------------------------------------------")
print("              OPERASI ARITMATIKA                ")
print("------------------------------------------------")
print("nim    :%s"%(nim))
print("nama  :%s"%(nama))
print("kelas:%s"%(kelas))
print("prodi:%s"%(prodi))
print("------------------------------------------------")
print("                   LINGKARAN                    ")
print("------------------------------------------------")
print("Luas lingkaran adalah :%d"%(luas))
print("Keliling lingkaran adalah :%d"%(keliling))
print("-------------------------------------------------")
print("                      KALIMAT                    ")
print("-------------------------------------------------")
print(kalimat[4],kalimat[9],kalimat[16],kalimat[2],kalimat[8],kalimat[5],kalimat[1],kalimat[6],kalimat[7],kalimat[14],kalimat[10],kalimat[12],kalimat[11],kalimat[1],kalimat[0],kalimat[15])
