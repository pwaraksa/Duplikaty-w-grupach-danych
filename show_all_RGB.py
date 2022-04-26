import pandas as pd
from simpledbf import Dbf5
from itertools import groupby
dbf = Dbf5(r'C:\Users\patryk.waraksa\Desktop\test\crtOrtoRGB_3857.dbf')

df = dbf.to_dataframe()


# print(df.head())
# print(df.name)
godla = df.name
katalogi = df.id_katalog

# print(katalogi)
# print(godla)
duplicates = godla.duplicated()
# print(duplicates)

ls_godlo = []
ls_katalog = []
for i in godla:
    ls_godlo.append(i)

for i in katalogi:
    ls_katalog.append(i)
# print(ls)

with open('lista_wszystkie_godla_ortoRGB.txt', 'w') as f:
    for i in range(len(ls_godlo)):
        line = str(ls_godlo[i]) + ',' + str(ls_katalog[i]) + "\n"
        f.write(line)


'''

#lista duplikatów z listy ls:
res = [(x, count) for x, g in groupby(sorted(ls)) if (count := len(list(g))) > 1]
# print(res)

with open('lista_duplikatow.txt', 'w') as f:
    for item in res:
        line = str(item[0])+" : "+str(item[1])+"\n"
        f.write(line)
'''