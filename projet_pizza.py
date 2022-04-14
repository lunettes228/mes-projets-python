def afficher(pizzas):
    # pizzas.sort()
    # pizzas=("margueritta","mexicain","épissé", "vegetariens")
    
    print(f"le nombre de pizza est : ({len(pizzas)}) : ".capitalize())
    while True:
        # print(i)
        if pizzas!=vide:
            print(f"la première pizza est : la pizza ({pizzas[0]})\nla dernière pizza est : la pizza ({pizzas[len(pizzas)-1]})" )
            break
        else:
            print("il n'ya aucune pizza à afficher".upper())
            break
pizzas=["roi","saumon","tomate","fromage","végétarien","reine"]
pizzas.sort()
vide=()

def ajouter(pizzas):
    new=input("voulez vous ajouter une pizza (oui ou non?) :")
    while True:
        if new!="non":
            nouveau=input("quel est le nom de la pizza?")
            pizzas.append(nouveau)
            print(f"le nombre de pizza est devenu : ({len(pizzas)}) !!!!! ".capitalize())
            print(f"voici la liste: \n {pizzas}")
            if nouveau=="":
                break
        elif nouveau=="":
            print(f"le nombre de pizzas est toujours : ({len(pizzas)-1}) !!!!!! ".upper())
            print(f"voici la liste: \n {pizzas[0:len(pizzas)-1]}".capitalize())
            break
        else:
            print(f"le nombre de pizzas est toujours : ({len(pizzas)}) !!!!!! ".upper())
            print(f"voici la liste: \n {pizzas}".capitalize())
            return

afficher(pizzas)
ajouter(pizzas)
