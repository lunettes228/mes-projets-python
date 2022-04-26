mult = x = input("vous voulez voir la table de quelle chiffre?: ".upper())
k = 1
n = int(input(f"jusqu'à quel chiffre afficher la table de {x} :".upper()))
for mult in range(0, n):
    try:
        x = int(x)
        print(f"{x} x {k} = {x*k}")
        k = k+1
    except:
        print(
            "ERREUR ENTREZ UN CHIFFRE PAS UNE LETTRE !!! \nREDEMARREZ LE PROGRAMME!!!!!!!!!")
        break
