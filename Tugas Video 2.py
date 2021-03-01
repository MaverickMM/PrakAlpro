#Maverick Mikolas Mulyadi
#71200582

'''
berkaitan dengan materi percabangan pada modul yang diberikan dan contoh soal unguided
,jika Arsy ingin membeli pakaian A yang kualitasnya bagus
harga pakaian tersebut adalah 300000, Arsy ingin
mencocokan harga pakaian tersebut dengan harga pasaran
sehingga Arsy membuat program untuk mencocokan harga pakaian
dengan kualitas yang diterima
'''

''' 
input yang dibutuhkan : 

Harga Pakaian Berkualitas Bagus 200000 - 400000
Harga Pakaian Berkualitas Biasa 50000 - 100000
Harga Pakaian Berkualitas Kurang Bagus 5000 - 20000

Harga Kemahalan
Harga Sesuai
Harga Diskon
'''

'''
Proses kerja Program

pertama kita butuh if untuk memilih kualitas pakaian yang ingin dibeli
lalu buat kondisi harga pakaian yang ingin digunakan lalu 
buat kondisi if lagi jika harga sesuai,kemahalan atau harga tersebut diskon
'''

'''
Output yang diinginkan :

1. Kualitas Bagus
2. Kualitas Biasa
3. Kualitas Kurang Bagus
Kualitas Pakaian yang ingin dibeli : 
Anda Memilih Kualitas Pakaian yang 
Harga Pakaian Yang Ingin dibeli : 
Hasil Analisa :
'''

print('1. Kualitas Bagus')
print('2. Kualitas Biasa')
print('3. Kualitas Kurang Bagus')

pilihan = int(input('Kualitas Pakaian yang ingin dibeli : '))

if pilihan == 1:
    print ('Anda Memilih Kualitas Pakaian yang Bagus')
    bagus = int(input('Harga Pakaian Yang Ingin dibeli : '))

    if bagus >= 200000 and bagus <= 400000:
        print('Hasil Analisa : Harga Sesuai')

    elif bagus < 200000:
        print('Hasil Analisa : Harga Diskon')

    elif bagus > 400000:
        print('Hasil Analisa : Harga Kemahalan')

elif pilihan == 2:
    print ('Anda Memilih Kualitas Pakaian yang Biasa')
    biasa = int(input('Harga Pakaian Yang Ingin dibeli : '))

    if biasa >= 50000 and biasa <= 100000:
        print('Hasil Analisa : Harga Sesuai')

    elif biasa < 50000:
        print('Hasil Analisa : Harga Diskon')

    elif biasa > 100000:
        print('Hasil Analisa : Harga Kemahalan')

elif pilihan == 3:
    print ('Anda Memilih Kualitas Pakaian yang Kurang Bagus')
    kurang_bagus = int(input('Harga Pakaian Yang Ingin dibeli : '))

    if kurang_bagus >= 200000 and kurang_bagus <= 400000:
        print('Hasil Analisa : Harga Sesuai')

    elif kurang_bagus < 200000:
        print('Hasil Analisa : Harga Diskon')

    elif kurang_bagus > 400000:
        print('Hasil Analisa : Harga Kemahalan')
