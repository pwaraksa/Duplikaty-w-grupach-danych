import pandas as pd
from simpledbf import Dbf5
from itertools import groupby
dbf = Dbf5(r'C:\Users\patryk.waraksa\Desktop\test\crtOrtoRGB_3857.dbf')

df = dbf.to_dataframe()

df_2var = df[["name", "id_katalog"]]

# print(df_2var)

# print(df_2var.loc[3].index)
# print(df[df['name'] == 'M-34-61-B-c-3-4'].index)


# print(df_2var.duplicated())

duplicates_asess = df_2var.duplicated()
# duplicates_asess.column = ['dupl']
# print(duplicates_asess.head())

# for i in duplicates_asess:
#     if i == True:
#         print(i.get_loc())
#         # print(duplicates_asess[duplicates_asess.iloc[:, 0] == 'True'].index)

df_dupl = df_2var[duplicates_asess]

print(df_dupl)

ls_godlo = []
ls_katalog = []

godla = df_dupl.name
katalogi = df_dupl.id_katalog

for i in godla:
    ls_godlo.append(i)

for i in katalogi:
    ls_katalog.append(i)


with open('lista_duplikatow_na_katalog_ortoRGB.txt', 'w') as f:
    line = "godlo,id_katalogu \n"
    f.write(line)
    for i in range(len(ls_godlo)):
        line = str(ls_godlo[i]) +','+ str(ls_katalog[i])  + "\n"
        f.write(line)
