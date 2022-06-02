from  random import*
list = ["long","jolie","rouge","mescain","yellow","red","colibri","zayn"]
mot=choice(list)
longueur_mot=" _ "
if len(mot) > 0:
    print(f"bienvenue dans le jeu!!!! \nle mot à deviner a {len(mot)} caracteres: {longueur_mot*len(mot)}".capitalize())
    lettres=longueur_mot*len(mot)
    