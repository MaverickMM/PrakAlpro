'''
Nama = Maverick Mikolas Mulyadi
Nim  = 71200582

tugas video kali tentang Struktur Kontrol Kompleks dan mendapat ide dari Matematika diskit
Ando ingin mengenkripsi kata "SEMUA","ORANG","BAIK","MEMBERI","NILAI","BAGUS" 
dengan menggunakan metode caesar cipher
dengan rumus a * huruf + b % 26

pada rumus pertama a = 2 , b = 7
pada rumus kedua a = 2 , b = 6
pada rumus ketiga a = 4 , b = 8
pada rumus keempat a = 2 , b = 3
pada rumus kelima a = 1 , b = 11
pada rumus keenam a = 3 , b = 9

input :

a,b,huruf,keluar,spasi

proses :

list a-z , listkosong , a,b,masukkan huruf, while true , if,elif,else , 2 for

output :

Contoh Salah Satu Program (Test Case)

(a * huruf + b) % 26
Masukkan a : 2
Masukkan b : 7
Masukkan Huruf : s
(2 * s + 7) % 26
s  =  18        

[18]
Masukkan Huruf : e
(2 * e + 7) % 26
e  =  4

[18, 4]
Masukkan Huruf : m
(2 * m + 7) % 26
m  =  12

[18, 4, 12]
Masukkan Huruf : u
(2 * u + 7) % 26
u  =  20

[18, 4, 12, 20]
Masukkan Huruf : a
(2 * a + 7) % 26
a  =  0

[18, 4, 12, 20, 0]
Masukkan Huruf :  
r p f v h 

Masukkan Huruf : keluar

'''

huruf = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

angka = []

a = ''
b = ''
print("(a * huruf + b) % 26")
a =int(input("Masukkan a : "))
b =int(input("Masukkan b : "))

while True:
    isi = str(input("Masukkan Huruf : "))
    jawaban = isi.lower()

    if isi == ' ':
        for i in angka:
            char = ((a * i) + b) % 26 
            char1 = chr(char+97)
            print(char1,end=" ")
        print("\n")


    elif isi == 'keluar':
        break

    else:
        print(f"({a} * {isi} + {b}) % 26")
        for i in range (1):
            angka1 = ord(jawaban) - 97
            print(isi," = ",angka1, end=" ")
            print("\n")

            angka.append(angka1)
            print(angka)
