# # nom=""
# # age = ""
# # while age == "" and nom=="":
# #     nom=input("quel est votre nom ?")
# #     age = input("quel est votre age ? ")
# #     try:
# #         age ==int(age) or nom==str(nom)

# #     except:
# #         print("Entrez une réponse valide")
# #     # try:
# #     #     nom=str(nom)
# #     # except:
# #     #     print("entrez un nom valide")
# # else :
# #     print("vous vous appellez  " + nom + " ,vous avez  " + str(age) + " ans")

# name=input("Entrez votre nom: ")
# age=input("Quel est votre age? ")
# try:
#     age=int(age)
# except:
#     print("Nom ou valeur d'age entrée incorrect !!!!")
# else:
#     print("Bonjour, vous vous appelez " +str(name)+" ,Vous avez "+str(age)+" ans aujourd'hui")

# nom=""
# while nom=="":
#     nom=input("Quel est votre nom ? ")
# else:
#     print("Vous vous appellez " + nom)


def demander_nom():
    nom_complet = str("")
    while nom_complet == "":
        nom_complet = input("Quel est votre nom?")
    # else:
    #     print("Entrez un Nom valide!!!!!")
    return(nom_complet)


nom = demander_nom()
# print("votre nom est :"+ nom)
# print("votre nom  est :" + nom2)

# print("vous avez "+age+"ans")


def demander_age(age):
    # age = int(input("quel est votre age ? "))
    if age >= 18:
        print("Vous etes majeur!!!")
        print("Vous vous appellez " + nom+" ,Vous avez "+str(age)+" ans")
    elif age == 17:
        print("Vous etes à 1an d'etre majeur!!!")
    else:
        print("Vous n'etes pas majeur!!!")


demander_age(int(input("quel est votre age?")))
