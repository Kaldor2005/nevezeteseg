f=open("nevezetesseg.txt","r",encoding="utf-8")
nagylista=[]
for sor in f:
    kislista=sor[:-1].split(":")
    nagylista.append(kislista)
f.close()
