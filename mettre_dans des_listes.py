noms=[]
while True:
    nom=input("entrez un nom: ".capitalize())
    noms.append(nom.capitalize())
    noms.sort()
    if nom=="":
        break
print("noms des personnes : ".capitalize())
print(noms[1::])

        