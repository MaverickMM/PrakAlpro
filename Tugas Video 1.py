# Nama : Maverick Mikolas Mulyadi
# Universitas Kristen Duta Wacana

# berkaitan dengan materi Variable, Expression dan Statements seperti pada contoh 1.3
# pada modul yang diberikan dan rumus tagihan secara kredit, jika
# Martin ingin membeli barang seharga 10.000.000 secara kredit selama
# (2 tahun atau 24 bulan) dengan bunga sebesar 10% uang muka yang
# dibayar oleh Martin adalah 500.000. dapatkanlah tagihan bulanannya

############################################################################

# Input yang dibutuhkan :

# harga barang
# uang muka
# berapa bulan
# sisa tagihan
# bunga
# jumlah bunga
# total tagihan
# tagihan perbulan
# sisa bulan
# tagihan cicilan

# Proses kerja program :
"""
harga
barang - uang
muka
bunga
10 %
hasil
dari
harga
barang - uang
muka(sisa
tagihan) *bunga
10 % = jumlah
bunga
sisa
tagihan + jumlah
bunga = total
tagihan
total
tagihan
dibagi
bulan
untuk
mendapatkan
tagihan
perbulannya
lalu
total
bulan - 1
untuk
mengetahui
sisa
cicilannya
total
tagihan
dikurang
tagihan
perbulan
setelah
itu
buatlah
output
"""
# Output yang ingin dihasilkan :

# Harga Sebuah Barang: 10000000
# Uang muka yang dibayar: 500000
# Durasi Cicilan berapa bulan? 24
# Tagihan Bulan ini adalah:  435417
# Sisa Tagihan Bulanan adalah:  23
# Sisa uang yang harus dibayar adalah:  10014583
# Total uang yang harus dibayar adalah:  10450000


hargabarang = int(input("Harga Sebuah Barang: "))
uangmuka = int(input("Uang muka yang dibayar: "))
berapabulan = int(input("Durasi Cicilan berapa bulan? "))

sisa_tagihan = int(hargabarang - uangmuka)

bunga = 10

jumlah_bunga = sisa_tagihan * bunga / 100

total_tagihan = sisa_tagihan + jumlah_bunga

tagihan_perbulan = total_tagihan / berapabulan

sisa_bulan = berapabulan - 1

tagihan_cicilan = total_tagihan - tagihan_perbulan

print('Tagihan Bulan ini adalah: ', round(tagihan_perbulan))
print('Sisa Tagihan Bulanan adalah: ', round(sisa_bulan))
print('Sisa uang yang harus dibayar adalah: ', round(tagihan_cicilan))
print('Total uang yang harus dibayar adalah: ', round(total_tagihan))
