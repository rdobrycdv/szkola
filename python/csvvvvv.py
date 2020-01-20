import csv
import numpy as np
from collections import Counter

plik=open("zapis z pytona.csv", "w")
dane=[]

with open('company_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
            dane.append(row)
dane2=[]

for i in range(1,21):
    dane2.append(dane[i][0].split(';'))
    
ID=[0]
nazwisko=[]
imie=[]
pensja=[]
plec=[]
rok=[]

for i in range (0,20):
    ID.append(dane2[i][0])
    nazwisko.append(dane2[i][1])
    imie.append(dane2[i][2])
    pensja.append(int(dane2[i][3]))
    plec.append(dane2[i][4])
    rok.append(int(dane2[i][5]))
    
ID=np.transpose(ID)
nazwisko=np.transpose(nazwisko)
imie=np.transpose(imie)
pensja=np.transpose(pensja)
plec=np.transpose(plec)
rok=np.transpose(rok)


a=Counter(ID)
b= Counter(plec)
lo=len(ID)

#liczba pracownikow
plik.write("liczb osob w firmie: " + str(lo-1))
np.max(rok)
np.min(rok)

#pensja
x=np.max(pensja)
y=np.where(pensja==x)[0][0]
z=dane2[y][1]
plik.write("\nnajwiecej zarabia  " + nazwisko[y] + "  " + imie[y])

xa=np.min(pensja)
ya=np.where(pensja==xa)[0][0]
za=dane2[ya][1]
plik.write("\nnajmniej zarabia  " + nazwisko[ya] + "  " + imie[ya])

#statystyki zarobki
sr=sum(pensja)/len(pensja)
plik.write("\nsrednia pensja wynosi: " + str(sr))



#c=counter(plec).most_common()
#ratio=c[1][1]/c[0][1]


#lista zapisywanie
#plik=open("zapis z pytona.csv", "w")
#plik.write("dsdd")
#plik close()

plik.close()

