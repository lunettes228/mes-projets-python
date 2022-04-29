
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



liste_de_fichiers =["sam.png", "google.com", "zoom.exe", "formatrion_complete.mkv", "dadju_reine.mp3"]
extension_de_liste=((".exe","exécutable"),  (".com","lien(url)"),(".mkv","vidéo"),(".mp3","audio"),(".png","image"))
for n in liste_de_fichiers:
    a=n.split(".")
    b=".".join(a)
    for i in extension_de_liste:
        h=i[0].split(".")
        if a[-1] in h :
            print(f"bonjour ce fichier est un: {h[1]}")
            break
        else:
            print("hello")
            break
        