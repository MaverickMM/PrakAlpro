#Nama : Maverick Mikolas Mulyadi
#Nim  : 71200582

# Modul 11 Tuples ion ingin menghapus kata dari dalam
# tuples yang sudah diberikan, bantulah ion membuat program
# tersebut

# tuples = ('Alpro','itu','susah')
# tuples = ('Alpro')
# tuples = ('Alpro','susah')
# tuples = ('itu','susah')

'''
input:
tuples
proses:
for i ,list, for 2,ubah jadi list lal jadi tuple lagi
output:
'''

def menghapus(kata,hapus):
    tmp = list()
    for i in kata:
        tmp.append(i)
    for j in hapus:
        tmp.remove(j)
    print(tmp)
kata = ('Alpro','itu','susah','mudah')
hapus = ['mudah']
menghapus(kata,hapus)
