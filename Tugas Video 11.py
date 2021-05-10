#Nama : Maverick Mikolas Mulyadi
#Nim  : 71200582

#Modul 12 Tentang SET 
#Maverick ingin membedakan kedua item dalam set, 
#dia ingin mengambil item yang sama dari kedua,item yang tidak sama dari kedua - duanya
#dan mengambil item dari semuanya
#set 1 = {1,2,3,4,5,6}
#set 2 = {1,2,3,4,5,7}

#input
# set1 , set2 , hitung berapa kali 1 ,hitung berapa kali 2
#proses
# masukkan isi,masukkan isi 2,add set1, add set2,print yang sama darib keduanya,print yang beda,ambil semua
#output

item1 = set()
item2 = set()
masukkan = int(input("Masukkan berapa panjang Set 1 : "))
for i in range(masukkan):
    set1 = input("Masukkan Huruf/Angka kedalam Set 1 : ").strip()
    item1.add(set1)
masukkan2 = int(input("Masukkan berapa panjang Set 2 : "))
for i in range(masukkan2):
    set2 = input("Masukkan Huruf/Angka kedalam Set 1 : ").strip()
    item2.add(set2)

print(sorted(item1))
print(sorted(item2))

sama = item1 & item2
beda = item1 ^ item2
semua = item1 | item2

print(sorted(sama))
print(sorted(beda))
print(sorted(semua))
