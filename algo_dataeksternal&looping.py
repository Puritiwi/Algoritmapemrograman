# Open File
data = open("data_iris.txt", "r")
print ("Nama File",data.name)

#read 
file_konten = data.read(100)
print ("Isi Data:",file_konten[17:39])

#Closed 
data.close()

# For loops
#for i in range(1,10): 
     #print(i)
list_dosen =("Wawan","Salim","Dedi","Lukman")
list_jadwal =("Senin","Selasa","Rabu","Kamis","Jumat")

for i in (list_dosen):
    for k in (list_jadwal):
        print(i," - ",k)
