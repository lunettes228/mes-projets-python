import random
def deviner_le_nombre(nombre_min,nombre_max):
    nombre_magique=random.randint(nombre_min,nombre_max)
    for i in range(0,10):
        nombre=input(f"quel est le nombre magique compris entre:{nombre_min} et {nombre_max}???".upper())
        try:
            nombre=int(nombre)
        except:
            print("entrez un nombre valide".upper())
        if nombre<nombre_magique:
            print("le nombre est plus grand".upper())
        elif nombre>nombre_magique:
            print("le nombre est plus petit".upper())    
        else:
            print(f"bravo le nombre magique est bien {nombre_magique}".upper())
            print("vous voulez rejouer?? redemarrer le jeu!!!!!".upper())
            break
    else:
        print("vous avez perdu redemarrez le jeu!!!".upper())
        print("vous avez perdu redemarrez le jeu!!!".upper())
        
deviner_le_nombre(10,100)