import random
choix = ["pierre", "feuille", "ciseau"]
# print("<------------------Début de Nouveau Tour--------------------->")
print("Début de Nouveau Tour".center(50, "-"))
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
point = 3
score = 0
choix_de_liste = random.choice(choix)
for i in range(point):
    v = print("Quel est votre choix ?".center(50, "-"))
    print("                          *                                   ")
    print("                          *                                   ")
    print("                          *                                   ")
    if choix_de_liste == "pierre":
        r = input("votre choix: ")
        if r == "feuille":
            print(f"Le choix de l'ordi est :{choix_de_liste}")
            print(f"votre choix est :{r}")
            score += 1
            print(f"Bravo vous avez gagné\nvotre score: {score}")

        elif r!=choix_de_liste:
            score -= 1
            print(f"Vous avez perdu\nvotre score: {score}")
            print(f"Le choix de l'ordi était :{choix_de_liste}")
            print(f"votre choix était :{r}")
        elif r==choix_de_liste :
            print(f"Le choix de l'ordi est :{choix_de_liste}")
            print(f"votre choix est :{r}")
            score += 0
            print(f"Personne n'a gagné !!!\nvotre score: {score}")
    elif choix_de_liste == "feuille":
        r = input("votre choix: ")

        if r == "ciseau":
            print(f"Le choix de l'ordi est :{choix_de_liste}")
            print(f"votre choix est :{r}")
            score += 1
            print(f"Bravo vous avez gagné\nvotre score: {score}")

        elif r!=choix_de_liste:
            print(f"Le choix de l'ordi était :{choix_de_liste}")
            print(f"votre choix était :{r}")
            score -= 1
            print(f"Vous avez perdu\nvotre score: {score}")
        elif r==choix_de_liste :
            print(f"Le choix de l'ordi est :{choix_de_liste}")
            print(f"votre choix est :{r}")
            score += 0
            print(f"Personne n'a gagné !!!\nvotre score: {score}")

    elif choix_de_liste == "ciseau":
        r = input("votre choix: ")

        if r == "pierre":
            print(f"Le choix de l'ordi est :{choix_de_liste}")
            print(f"votre choix est :{r}")
            score += 1
            print(f"Bravo vous avez gagné\nvotre score: {score}")

        elif r!=choix_de_liste:
            print(f"Le choix de l'ordi était :{choix_de_liste}")
            print(f"votre choix était :{r}")
            score -= 1
            print(f"Vous avez perdu\nvotre score: {score}")
        elif r==choix_de_liste :
            print(f"Le choix de l'ordi est :{choix_de_liste}")
            print(f"votre choix est :{r}")
            score += 0
            print(f"Personne n'a gagné !!!\nvotre score: {score}")
    

    choix_de_liste = random.choice(choix)

print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("                          '                                   ")
print("<--------------------Fin de Tour----------------------------->")
