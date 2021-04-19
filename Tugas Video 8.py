#Nama : Maverick Mikolas Mulyadi
#Nim : 71200582

# Modul 9 List
# Ando ingin menghilangkan duplikat dari list yang dia buat,
# sehingga Ando menciptakan program untuk menghilangkan duplikat yang
# ada didalam list

# jika dimasukkan ["Satu","Satu","Dua","Tiga","Tiga","Empat"]
# maka hasilnya:
# ['Satu', 'Dua', 'Tiga', 'Empat']

# input

# input list

# Proses

# list1,List2,for i,if i not in List2 maka  i di append List2

# output


def duplika(List_satu):
    duplikat = []
    hitung = 0
    for i in List_satu:
        if i not in duplikat:
            duplikat.append(i)
            hitung += 1
    return(f"List anda ada {hitung} yaitu : \n{duplikat}")

List_satu = ["Satu","Satu","Dua","Tiga","Tiga","Empat","5","5",6,7,7]

print(duplika(List_satu))

List_satu = ["Satu","Satu","Dua"]

print(duplika(List_satu))

List_satu = ["Tiga","Empat","5","5",6,7,7]

print(duplika(List_satu))
