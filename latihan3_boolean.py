# Setting Variabel Identitas
nim   = input("Masukkan NIM   :")
nama  = input("Masukkan Nama  :")
kelas = input("Masukkan Kelas :")
prodi = input("Masukkan Prodi :")

#Setting Variabel nilai
bhs_indo = int(input("Nilai Bahasa Indonesia   :"))
bhs_ing  = int(input("Nilai Bahasa Inggris     :"))
pd       = int(input("Nilai Pemrograman Dasar  :"))
mtk      = int(input("Nilai Matematika         :"))
kal1     = int(input("Nilai Kalkulus 1         :"))
so       = int(input("Nilai Sistem Operasi     :"))

# Perhitungan
rata = (bhs_indo+bhs_ing+pd+mtk+kal1+so)/6

if(rata >0 and rata <=60):
    grade_rata = ("c")
elif(rata > 60 and rata <=75):
    grade_rata = ("B")
elif(rata > 75 and rata <=85):
    grade_rata = ("AB")
elif(rata > 85 and rata <=100):
    grade_rata = ("A")
else:
    grade_rata =("Grade Anda Tidak Ditemukan!")

# Grade tiap makul
if(bhs_indo >0 and bhs_indo <=60):
    grade_indo = ("c")
elif(bhs_indo  > 60 and bhs_indo  <=75):
    grade_indo = ("B")
elif(bhs_indo  > 75 and bhs_indo <=85):
    grade_indo = ("AB")
elif(bhs_indo  > 85 and bhs_indo  <=100):
    grade_indo = ("A")
else:
    grade_indo =("Grade Anda Tidak Ditemukan")
    
if(bhs_ing>0 and bhs_ing <=60):
    grade_ing= ("c")
elif(bhs_ing > 60 and bhs_ing <=75):
    grade_ing = ("B")
elif(bhs_ing > 75 and bhs_ing<=85):
    grade_ing = ("AB")
elif(bhs_ing > 85 and bhs_ing<=100):
    grade_ing = ("A")
else:
    grade_ing =("Grade Anda Tidak Ditemukan!")
    
if(pd >0 and pd <=60):
    grade_pd = ("c")
elif(pd > 60 and pd <=75):
    grade_pd = ("B")
elif(pd > 75 and pd <=85):
    grade_pd = ("AB")
elif(pd > 85 and pd <=100):
    grade_pd = ("A")
else:
    grade_pd=("Grade Anda Tidak Ditemukan!")
    
if(mtk >0 and mtk <=60):
    grade_mtk = ("c")
elif(mtk > 60 and mtk <=75):
    grade_mtk = ("B")
elif(mtk > 75 and mtk <=85):
    grade_mtk = ("AB")
elif(mtk > 85 and mtk<=100):
    grade_mtk = ("A")
else:
    grade_mtk =("Grade Anda Tidak Ditemukan!")
    
if(kal1 >0 and kal1 <=60):
    grade_kal1= ("c")
elif(kal1 > 60 and kal1<=75):
    grade_kal1 = ("B")
elif(kal1 > 75 and kal1 <=85):
    grade_kal1 = ("AB")
elif(kal1 > 85 and kal1<=100):
    grade_kal1 = ("A")
else:
    grade_kal1 =("Grade Anda Tidak Ditemukan!")
    
if(so >0 and so <=60):
    grade_so = ("c")
elif(so > 60 and so <=75):
    grade_so= ("B")
elif(so> 75 and so <=85):
    grade_so = ("AB")
elif(so > 85 and so <=100):
    grade_so= ("A")
else:
    grade_SO =("Grade Anda Tidak Ditemukan!")

# cetak hasil
print("-----------------------------------------")
print("         Kartu Hasil Studi               ")
print("    UNNIVERSITAS SELAMAT SRI BATANG      ")
print("-----------------------------------------")
print("NIM          :",nim)
print("Nama Lengkap :",nama)
print("Kelas        :",kelas)
print("Program Studi:",prodi)
print("-----------------------------------------")
print("No  Nama Makul        Nilai        Grade ")
print("-----------------------------------------")
print("1.Bahasa Indonesia    :",bhs_indo," ",grade_indo)
print("2.Bahasa Inggris      :",bhs_ing," ",grade_ing)
print("3.Pemrograman Dasar   :",pd," ",grade_pd)
print("4.Matematika          :",mtk," ",grade_mtk)
print("5.Kalkulus 1          :",kal1," ",grade_kal1)
print("6.Sistem Operasi      :",so," ",grade_so)
print("-----------------------------------------")
print("Rata - rata                        :",rata)
print("Kategori                           :",grade_rata)
print("-----------------------------------------")
