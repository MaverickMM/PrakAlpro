#Nama : Maverick Mikolas Mulyadi
#Nim  : 71200582
"""
Seperti pada modul Pertemuan 4 disini akan digunakan Def untuk membuat fungsi baru
Jika Arsi Ingin mengetahui berapakah nilai rata-rata dari total yang dia punya
yaitu nilai quiz 1 = 90, quiz 2 = 80, quiz 3 = 90, quiz 4 = 100, quiz 5 = 70,
uts = 80, uas = 90. total semua nilai quiz jika digabungkan yaitu 10%
nilai uts adalah 40% dan nilai uas adalah 50%, Buatlah Prgram menghitung seperti dibawah ini
"""
"""
Input:
Nilai quiz1
nilai quiz2
nilai quiz3
nilai quiz4
nilai quiz5
nilai uts
nilai uas

Proses:
pertama buat def nilaiquiz1,2,3,4,5 / 5
totalquiz * 0.1 + uts * 0.4 + uas * 0.5

def if >= 90 return 'A':
    elif >= 80 return 'B':
    elif >= 70 return 'C':
    elif >= 60 return 'D':
    else:
     return 'E' 

Output:
======================================
==Selamat Datang Di Kalkulator Nilai==
======================================
Masukkan Nama Anda: >? Arsi
Selamat Datang  Arsi
Masukkan nilai QUIZ 1 anda : >? 90
Masukkan nilai QUIZ 2 anda : >? 80
Masukkan nilai QUIZ 3 anda : >? 90
Masukkan nilai QUIZ 4 anda : >? 100
Masukkan nilai QUIZ 5 anda : >? 70
Masukkan nilai UTS anda : >? 80
Masukkan nilai UAS anda : >? 90
Rata - Rata Nilai anda adalah :  85.6
Nilai Total Anda  adalah :  B

"""

def nilai_total(nilai1,nilai1_2,nilai1_3,nilai1_4,nilai1_5,nilai2,nilai3):
    total_quiz = (nilai1 + nilai1_2 + nilai1_3 + nilai1_4 + nilai1_5) / 5
    total = (0.1 * total_quiz) + (0.4 * nilai2) + (0.5 * nilai3)
    return total

def Huruf(totalnilai):

    if totalnilai >= 90:
        return 'A'
    elif totalnilai >= 80:
        return 'B'
    elif totalnilai >= 70:
        return 'C'
    elif totalnilai >= 60:
        return 'D'
    else:
        return 'E'


print ("======================================")
print ("==Selamat Datang Di Kalkulator Nilai==")
print ("======================================")

nama = input("Masukkan Nama Anda : ")
print ("Selamat datang",nama)

nilai1 = int(input("Masukkan nilai QUIZ 1 anda : "))
nilai1_2 = int(input("Masukkan nilai QUIZ 2 anda : "))
nilai1_3 = int(input("Masukkan nilai QUIZ 3 anda : "))
nilai1_4 = int(input("Masukkan nilai QUIZ 4 anda : "))
nilai1_5 = int(input("Masukkan nilai QUIZ 5 anda : "))
nilai2 = int(input("Masukkan nilai UTS anda : "))
nilai3 = int(input("Masukkan nilai UAS anda : "))

totalnilai = nilai_total(nilai1,nilai1_2,nilai1_3,nilai1_4,nilai1_5,nilai2,nilai3)

print("Rata - Rata Nilai anda adalah : ", nilai_total(nilai1,nilai1_2,nilai1_3,nilai1_4,nilai1_5,nilai2,nilai3))
print("Nilai Total Anda  adalah : ",Huruf(totalnilai))