import pandas as pd

Esterno_id = pd.read_csv('Esterno_id.csv', error_bad_lines=False)
Esterno_icaltype = pd.read_csv('Esterno_icaltype.csv', error_bad_lines=False)
Esterno_count = pd.read_csv('Esterno_count.csv', error_bad_lines=False)

Esterno = pd.concat([Esterno_id, Esterno_icaltype, Esterno_count], axis=1)
print(Esterno)


Interno_id = pd.read_csv('Interno_id.csv', error_bad_lines=False)
Interno_icaltype = pd.read_csv('Interno_icaltype.csv', error_bad_lines=False)
Interno_count = pd.read_csv('Interno_count.csv', error_bad_lines=False)

Interno = pd.concat([Interno_id, Interno_icaltype, Interno_count], axis=1)

index_names = Esterno[ Esterno['icalType: Descending'] != "airbnb" ].index
Esterno.drop(index_names, inplace = True)

index_names1 = Interno[ Interno['channel: Descending'] != "AIRBNB" ].index
Interno.drop(index_names1, inplace = True)


s1 = pd.merge(Esterno, Interno, how='inner', on=['apartmentId: Descending'])

print(s1)

for el in s1:
    print(el)

del s1['icalType: Descending']
del s1["channel: Descending"]

print(s1)

#Sum of nights --> Bookiply
#Count --> Esterni

Count_esterne = s1["Count"].tolist()
Bookiply = s1["Sum of nights"].tolist()

print(Count_esterne)
print(Bookiply)

Bookiply_meglio = 0
Esterne_meglio = 0
Uguale = 0

i = 0
while i < 112:
    if Count_esterne[i] < Bookiply[i]:
        Bookiply_meglio +=1
    if Count_esterne[i] > Bookiply[i]:
        Esterne_meglio +=1
    if Count_esterne[i] == Bookiply[i]:
        Uguale += 1
    i += 1

print(Bookiply_meglio)
print(Esterne_meglio)
print(Uguale)

#Per esterno, 783 su 2731 sono airnbnb
#Per interno, 1258 su 4863 sono airbnb
# In comune ne hanno 112. Questo vuol dire che 671 ricevono prenotazioni solo esterne, mentre 1146 ricevono prenotazioni solo con Bookiply
#Per quelle che compaiono in entrambe, 71 vanno meglio su Bookiply, 32 da sole, e 9 vanno allo stesso modo

Bookiply_meglio_list = []
Esterne_meglio_list = []


i = 0
while i < 112:
    if Count_esterne[i] < Bookiply[i]:
        Bookiply_meglio_list.append(int(Bookiply[i] - Count_esterne[i]))
    if Count_esterne[i] > Bookiply[i]:
        Esterne_meglio_list.append(int(Count_esterne[i]- Bookiply[i]))
    i += 1

print(len(Bookiply_meglio_list))

a = sum (Bookiply_meglio_list)
print(a/71)


print(len(Esterne_meglio_list))
b = sum(Esterne_meglio_list)
print(b/32)

#Quando è meglio bookiply, è meglio di 7.64 notti
#Quando è meglio Esterne, è meglio di 6.18 notti
