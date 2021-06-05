#Nama : Maverick Mikolas Mulyadi
#Nim  : 71200582

'''
Mavei ingin membuat program untuk dapat 
mengecek nama dan umur yang diberikan
=untuk nama= +untuk umur+

jadskdjasadasdasd=Goni=asdad asdasdasda+19+sadasdad
ljlhhadskasdadsdasd=Maveri=asdasfgfhj+179+sadashkj
asdadasddjassadasasd=Spiro=asdhjlljhljsdasda+20+sadasdad

input

n = 5,for,input,regex,def,for

Process
n = 3
for i in range(n):
    input
    namaumur(input)

output

'''
import re
def namaumur(text):
    x = re.findall("\=([^\d]+)\=|\+([^)]+)\+",text)
    for i in x:
        for j in i:
            if j !='':
                print(j)

n = 3
for i in range(n):
    text = str(input("Masukkan Text yang anda mau : "))
    namaumur(text)
