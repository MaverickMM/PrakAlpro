# Nama : Maverick Mikolas Mulyadi
# Nim  : 71200582

#Tentang Rekursif Ahman ingin membuat rekursif yang dapat menambah atau mengurang
#karena disuruh dosen sehingga dia akan membuat 
#program rekursif sederaha tersebut


# input
# inputan
# Proces

# output

def nambah(n,m=10):
    if n == m:
        print(n)

    else:
        print(n)
        n += 1
        nambah(n)

def kurang(n):
    if n < 1:
        print(n)

    else:
        print(n)
        n -= 1
        kurang(n)
        

a = int(input("Angka = "))
nambah(a)
kurang(a)
