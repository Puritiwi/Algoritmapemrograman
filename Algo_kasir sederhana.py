# Nama Barang
indomie       = int(input("Jumlah indomie       : "))
minuman       = int(input("Jumlah minuman       : "))
gula          = int(input("Jumlah gula          : "))
beras         = int(input("Jumlah beras         : "))
telur         = int(input("Jumlah telur         : "))

# Harga Barang
j_indomie       = 40000*indomie
j_minuman       =10000*minuman 
j_gula          = 15000*gula 
j_beras         = 12000*beras
j_telur         = 30000*telur

# Perhitungan
belanja=(j_indomie+j_minuman+j_gula+j_beras+j_telur)

# Diskon
if belanja > 200000:
    diskon = belanja*0.2
else:
  diskon = 0
f_diskon = f"                                            {diskon:.2f}".rstrip("0").rstrip(".")

# Total Harga 
harga = belanja-diskon
f_harga = f"                                              {harga:.2f}".rstrip("0").rstrip(".")

print("------------------------------------------------------")
print("               TOKO SEMBAKO BERLIAN                   ")
print("------------------------------------------------------")
print("   No   |   Nama Produk   |  Qty  |  Harga  |  Jumlah ")
print("   1.         Indomie        " ,indomie,                                                               "Rp.40000","","Rp"    ,j_indomie)
print("   2.         Minuman        " ,minuman,                                                               "Rp.10000","","Rp",j_minuman)
print("   3.          Gula          " ,gula,                                                                  "Rp.15000","","Rp",j_gula)
print("   4.          Beras         " ,beras,                                                                 "Rp.12000","","Rp",j_beras)
print("   5.          Telur         " ,telur,                                                                 "Rp.30000","","Rp",j_telur) 
print("")
print("------------------------------------------------------")
print("                          Total Belanja : Rp.",belanja )
print("                             Diskon     : Rp.",f_diskon)
print("-----------------------------------------------------",)
print("")
print("                           Total Harga : Rp.",f_harga)
bayar = int(input("                   Bayar   : Rp."         ))
while bayar < harga:
    print("uang anda kurang'")
    bayar = int(input("                                    Bayar      : Rp "))
    
# kembali 
kembali = bayar-harga 
f_kembali = f"                                            {kembali:.2f}".rstrip("0").rstrip(".")
print("                           Kembalian : Rp",f_kembali)
print("")
print("")
print("") 
print("                     TERIMAKASIH                     ")
