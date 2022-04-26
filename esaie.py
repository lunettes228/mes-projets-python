
# noms = ["samuel", "roger", "naomi", "v48itali", "roger", "ahlin", "youssef", "rao47ul", "ibrahim", "naffi", "ivan", "zaynab", "kola", "emeraude", "appo",
#         "merveille", "victo45rine", "victoire", "jédéon", "samira", "walter", "essor", "abdou", "josé55", "raymond", "staff", "happiness"]

# ceci c'est juste pour tester la fonction is digit

k=input("quel est le nom? ")
y=any([ x.isdigit() for x in k ])
while y is True:
    print("la liste contient un élément avec un chiffre")
    break
else:
    print("la liste ne contient pas d'élément avec un chiffre")
    
# la fonction is digit est maintenant maitrisé
