mult=x=input("vous voulez voir la table de quelle chiffre?: ".upper())
k=1

for mult in range(0,12):
    try:
        x=int(x)
        print(f"{x}*{k} = {x*k}")
        k=k+1
    except:
        print("ERREUR ENTREZ UN CHIFFRE PAS UNE LETTRE !!! \nREDEMARREZ LE PROGRAMME!!!!!!!!!"  )
        break
    