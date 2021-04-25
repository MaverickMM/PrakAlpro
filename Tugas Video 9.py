#Nama : Maverick Mikolas Mulyadi
#Nim  : 71200582
'''
modul 10 Dictionary
dia ingin menampilkan nama dan umur dari siswa dengan mudah 
sehingga dia membuat program sederhana



Berapa Kali:2
Nama    : Mave
Umur    : 18
Nama    : Noni
Umur    : 17
///////////////////////////
Nama : Mave
Umur : 18
============
Nama : Noni
Umur : 17
============


input:
 -jumlah nama dan umur yang akan dipanggil
 -Nama dan umur
proses:
 -dict
 -jumlah = int(input("Berapa Kali Nama dan Umur akan dipanggil))
 -for i in jumlah
    nama = asas
    umur = 19
    dict[nama] = umur
    print("///////")
-for i in dict.keys()
-for j in dict.values()
    if dict[i] == j
        print("nama :",i)
        print ("umur :",j)
output:

'''

nammur = dict()
jumlah = int(input("Berapa kali Nama dan Umur akan dipanggil : "))

for i in range (jumlah):
    nama = input("Nama : ")
    umur = int(input("Umur : "))
    nammur[nama] = umur
print("///////////////////////////")
for i in nammur.keys():
    for j in nammur.values():
        if nammur[i] == j:
            print("Nama :",i)
            print("Umur :",j)
