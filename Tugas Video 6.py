#Maverick Mikolas Mulyadi
#71200582

# tugas video kali ini dibuat dengan string seperti yang telah
# diajarkan, lisa ingin membuat program string untuk membuat kata rahasia
# dengan cara dibalik balik / slicing

# input
# 1 input masukkan
# proses
# 3 kali slicing
# output

# Masukkan kata: saya
# saya
# ayas
# aysay
try:
    masukkan = str(input("Masukkan kata: "))

except:
    print("Maaf inputan anda salah")
text1 = masukkan[::1]
text2 = masukkan[::-1]
text3 = masukkan[:1:-1]
text4 = masukkan[:-1:1]
print("Text pertama : ",text1)
print("Text kedua   : ",text2)
print("Text ketiga  : ",text3,end="")
print(text4)



