# Nama : Maverick Mikolas Mulyadi
# Nim  : 71200582


'''
Seperti pada modul pertemuan 5 saya menggunakan for, dicontoh kali ini
Giorno ingin membuat program tentang batas minimum apakah dia lulus atau tidak jika
dia tidak mengerjakan tugas selama beberapa hari
'''

'''
Input

hari
ya, tidak, keluar

proses

hari = input
total = 0
for i in range (1,hari+1)

total > hari // 10


output

Selamat datang di --- Hari ini Ngerjain Tugas Tidak? ---
Berapa hari Tugas yang ingin kamu hitung?: 10
Apakah kamu mengerjakan tugas hari ini?: ya
Poin Kamu +1 
Poin Kamu sekarang ada  1
Apakah kamu mengerjakan tugas hari ini?: ya
Poin Kamu +1 
Poin Kamu sekarang ada  2
Apakah kamu mengerjakan tugas hari ini?: ya
Poin Kamu +1 
Poin Kamu sekarang ada  3
Apakah kamu mengerjakan tugas hari ini?: ya
Poin Kamu +1 
Poin Kamu sekarang ada  4
Apakah kamu mengerjakan tugas hari ini?: ya
Poin Kamu +1 
Poin Kamu sekarang ada  5
Apakah kamu mengerjakan tugas hari ini?: ya
Poin Kamu +1 
Poin Kamu sekarang ada  6
Apakah kamu mengerjakan tugas hari ini?: ya
Poin Kamu +1 
Poin Kamu sekarang ada  7
Apakah kamu mengerjakan tugas hari ini?: tidak
Yah Poin Kamu -1 
Poin Kamu sekarang ada  6
Apakah kamu mengerjakan tugas hari ini?: tidak
Yah Poin Kamu -1 
Poin Kamu sekarang ada  5
Apakah kamu mengerjakan tugas hari ini?: ya
Poin Kamu +1 
Poin Kamu sekarang ada  6
Selamat kamu memiliki  6 poin
Selamat kamu lulus

'''

total = 0
hari = 0
print("Selamat datang di --- Hari ini Ngerjain Tugas Tidak? ---")
try:
    hari = int(input("Berapa hari Tugas yang ingin kamu hitung?: "))

except:
    print("Maaf harus Berupa angka")

for i in range (1,hari+1):

    pilihan = str(input("Apakah kamu mengerjakan tugas hari ini?: "))
    if pilihan == "ya":
        total = total + 1

        print("Poin Kamu +1") 
        print("Poin Kamu sekarang ada " ,total)

    elif pilihan == "tidak":  
        total = total - 1

        print("Poin Kamu -1") 
        print("Poin Kamu sekarang ada " ,total)

    elif pilihan == "keluar":
        break

print ("Selamat kamu memiliki",total,"poin")
if total > (hari//2):
    print("Selamat kamu lulus")
else:
    print("Yah kamu tidak lulus")

