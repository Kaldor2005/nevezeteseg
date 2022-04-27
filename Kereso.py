f=open("nevezetesseg.txt","r",encoding="utf-8")
nagylista=[]
for sor in f:
    kislista=sor[:-1].split(":")
    nagylista.append(kislista)
f.close()

def alfa1():
    while True:
        print('')
        print('1- A Megváltó Krisztus szobra\n2 - Tiahuanaco\n3 - Potala Palota\n4 - Isztambuli Nagy Bazár\n5 - Central Park\n6 - Operaház\n7 - Universal´s Islands of Adventure\n8 -  Nagy Palota\n9 - National Museum of Natural History\n10 - Versailles-i kastély')
        v = int(input('Nevezetesség :'))
        print('Nevezetesség: ',nagylista[v-1][0])
        print('Helyszín: ',nagylista[v-1][1])
        print('Épitése: ',nagylista[v-1][2])

def alfa2():
    while True:
        print('')
        print('Adja meg a keletkezési évet')
        v = int(input('Évszám: '))
        if v == 1931:
            print(nagylista[0])
        elif v == 800:
            print(nagylista[1])
        elif v == 1800:
            print(nagylista[2])
        elif v == 1461:
            print(nagylista[3])
        elif v == 1840:
            print(nagylista[4])
        elif v == 1973:
            print(nagylista[5])
        elif v == 1999:
            print(nagylista[6])
        elif v == 1782:
            print(nagylista[7])
        elif v == 1910:
            print(nagylista[8])
        elif v == 1634:
            print(nagylista[9])
        else:
            print('Nincs adat')

def alfa3():
    while True:
        print('')
        print('Adja meg az ország nevét')
        v = input('Ország neve: ')
        if v == 'Brazília':
            print(nagylista[0])
        elif v == 'Bolívia':
            print(nagylista[1])
        elif v == 'Kína':
            print(nagylista[2])
        elif v == 'Törökország':
            print(nagylista[3])
        elif v == 'Egyesült királyság':
            print(nagylista[4])
        elif v == 'Ausztrália':
            print(nagylista[5])
        elif v == 'USA':
            print(nagylista[6])
            print(nagylista[8])
        elif v == 'Thailand':
            print(nagylista[7])
        elif v == 'Franciaország':
            print(nagylista[9])
        else:
            print('Nincs adat')
        
    


while True:
    print('')
    print('1 - Nevezetesség név megadása\n2 - Évszám megadása\n3 - Országnév megadása')
    print('Melyik funkciót választja?')
    v = int(input('Funkció: '))
    if v == 1:
        alfa1()
    if v == 2:
        alfa2()
    if v == 3:
        alfa3()

    
