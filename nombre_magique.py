from random import *
def deviner_le_nombre(nombre_min,nombre_max):
    nombre_magique=randint(nombre_min,nombre_max)
    for i in range(0,10):
        nombre=input(f"quel est le nombre magique compris entre:{nombre_min} et {nombre_max}???".capitalize())
        try:
            nombre=int(nombre)
        except:
            print("entrez un nombre valide".capitalize())
        if nombre<nombre_magique:
            print("le nombre est plus grand".capitalize())
        elif nombre>nombre_magique:
            print("le nombre est plus petit".capitalize())    
        else:
            print(f"bravo le nombre magique est bien {nombre_magique}".capitalize())
            print("vous voulez rejouer?? redemarrer le jeu!!!!!".capitalize())
            break
    else:
        print("vous avez perdu redemarrez le jeu!!!".capitalize())
        print("vous avez perdu redemarrez le jeu!!!".capitalize())
        
deviner_le_nombre(10,100)