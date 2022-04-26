noms = ["samuel", "roger", "naomi", "vitali", "roger", "ahlin", "youssef", "raoul", "ibrahim", "naffi", "ivan", "zaynab", "kola", "emeraude", "appo",
        "merveille", "victorine", "victoire", "jédéon", "samira", "walter", "essor", "abdou", "josé", "raymond", "staff", "happiness"]
lenght_noms = len(noms)
element = input("l'index de quel noms afficher ?")
element_miniscule = element.lower()
nombre_de_fois = noms.count(element_miniscule)
if element_miniscule in noms:
    index_de_lélément = noms.index(element_miniscule)
    print(f"l'élément est dans la liste de {lenght_noms}  noms !!!".upper())
    if nombre_de_fois > 0:
        for i in range(nombre_de_fois):
            if nombre_de_fois == 1:
                print(f"son index est: {index_de_lélément}".capitalize())
                print(f"il est répété: {nombre_de_fois} fois".capitalize())
                break
            elif nombre_de_fois > 1:
                print(
                    f"son premier index est: {index_de_lélément}".capitalize())
                x = index_de_lélément+1
                index_de_lélément = noms.index(element_miniscule, x)
                print(f"il est répété: {nombre_de_fois} fois".capitalize())
                print(f"son second index est: {index_de_lélément}")
                break
else:
    print("le nom saisie n'est pas dans la liste de noms!!!!!".upper())
    # break
    # break