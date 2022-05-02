
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

noms = ["mt5.exe", "ninho arme de point.mp3", "google.com", "santrinos egbé(clip officiel).mp4", "mes notes.txt"]


noms_et_type_de_fichier = {"exe": "exécutable", "com": "lien(url)",
               "mp3": "fichier mp3 ", "mp4": "fichier video", "txt": "document text"}

for i in noms_et_type_de_fichier:
    for n in noms:
        nom_split=n.split(".")
        m=noms_et_type_de_fichier[i]
        if nom_split[1] in i:
            print( n +" est un: "+ m.upper()) 
            break 
# else:
#     break
    # print("c'est un fichier non connue")
noms_1=["samuel","reine","alice","antoine","nicola","david","maxim"]
len_noms=[len(nom) for nom in noms_1]
nom_join="".join(noms_1)
# x=0
# for i in noms:
#     a=len(i)
#     # len_noms.append(a)
#     # print(len_noms)
#     x=a+x
# print(x) 
# for i in noms:
#     len_noms.append(len(i))
# # print(len_noms)
# print("le nombre total de caractères de la liste de nom est : ",sum(len_noms))
print(f"cette liste de noms_1 contient : {len(nom_join)} caractères".upper())           