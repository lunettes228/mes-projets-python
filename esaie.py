
# # noms = ["samuel", "roger", "naomi", "v48itali", "roger", "ahlin", "youssef", "rao47ul", "ibrahim", "naffi", "ivan", "zaynab", "kola", "emeraude", "appo",
# #         "merveille", "victo45rine", "victoire", "jédéon", "samira", "walter", "essor", "abdou", "josé55", "raymond", "staff", "happiness"]

# # ceci c'est juste pour tester la fonction is digit

# k=input("quel est le nom? ")
# y=any([ x.isdigit() for x in k ])
# while y is True:
#     print("la liste contient un élément avec un chiffre")
#     break
# else:
#     print("la liste ne contient pas d'élément avec un chiffre")

# # la fonction is digit est maintenant maitrisé


# liste_de_fichiers = ["sam.png", "google.com", "zoom.exe",
#                      "formatrion_complete.mkv", "dadju_reine.mp3"]
# extension_de_liste = (("exe", "exécutable"),  ("com", "lien(url)"),
#                       ("mkv", "vidéo"), ("mp3", "audio"), ("png", "image"))
# for n in liste_de_fichiers:
#     a = n.split(".")

#     b = ".".join(a)
#     for i in extension_de_liste:
#         for m in i:
#             h = i[0].split(".")
#             if a[-1] == i[0]:
#                 print(f"bonjour ce fichier est un/une: {m}")
#                 break
#             else:
#                 print("hello")
#                 break

#     break

noms = ["samuel", "ahlin", "mike", "roger", "merveille"]


noms_et_age = {"samuel": "18 ans", "ahlin": "28 ans",
               "mike": "14 ans", "roger": "22 ans", "merveille": "6 ans"}

for i in noms:
    for n in noms_et_age:
        p = n[i]
        if p in n:
            print(f"le nom de la personne est {i} : il a {p} ans")
