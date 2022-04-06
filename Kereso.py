f=open("nevezetesseg.txt","r",encoding="utf-8")
nagylista=[]
for sor in f:
    kislista=sor[:-1].split(":")
    nagylista.append(kislista)
f.close()

while True:
    print('')
    print('1- A Megváltó Krisztus szobra\n2 - Tiahuanaco\n3 - Potala Palota\n4 - Isztambuli Nagy Bazár\n5 - Central Park\n6 - Operaház\n7 - Universal´s Islands of Adventure\n8 -  Nagy Palota\n9 - National Museum of Natural History\n10 - Versailles-i kastély')
    v = int(input('Nevezetesség :'))
    print('Nevezetesség: ',nagylista[v-1][0])
    print('Helyszín: ',nagylista[v-1][1])
    print('Épitése: ',nagylista[v-1][2])

    
