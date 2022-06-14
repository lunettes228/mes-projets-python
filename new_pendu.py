import random
choix = ["casserole", "cuillere", "patate", "souris"]
solution = random.choice(choix)
tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "
print(">> Bienvenue dans le pendu <<")
while tentatives > 0:
  print(f"\nMot à deviner: {len(solution)} caractères : ", affichage)
  proposition = input("proposez une lettre : ").lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives -= 1
  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print(f"\n    * Fin de la partie *  le mot est :  '{affichage.upper()}' ")