# Nama : Maverick Mikolas Mulyadi
# Nim : 71200582

# Kali ini tentang materi File Handling dari modul 8,
# Ando ingin memasukkan kata kata yang dia pikirkan kedalam suatu file. 
# tetapi dia tidak ingin menggunakan program teks editor biasa sehingga dia 
# membuat program untuk membaca dan menulis file sendiri

# TestCase :
# Masukkan Pilihan Anda :1
# ---Masukkan kata---  
# Masukkan Kata anda : Kata


# Masukkan Pilihan Anda :2
# ---Kata yang anda masukkan---

# Kata
# ////////////////////////////
# Masukkan Pilihan Anda :3
# Exit


# Input :

# Masukkan Pilihan,Masukkan Kata

# Proses:

# open file(File.txt,w,r)
#masukkan pilihan satu menulis
#masukkan pilihan dua membaca
#masukkan pilihan tiga exit 
# print masukkan kata
# file.write(masukkan katanya)

# pilihan kedua
# file.read()


# Output:

while True:
    pilihan = int(input("Masukkan Pilihan Anda : "))
    if pilihan == 1:
        files = open("File.txt","a")
        print("---Masukkan Kata---")
        Kata = input("Masukkan Kata Anda : ")
        files.write(Kata)
        files.write("\n")
        print("\n")

    elif pilihan == 2:
        files = open("File.txt","r")
        print("---Kata yang anda masukkan---")
        print(files.read())
        print("////////////////////////////////")
    elif pilihan == 3:
        print("Anda berhasil Keluar")
        exit
        



