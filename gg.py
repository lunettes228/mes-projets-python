class Pizza:
    def __init__(self,nom: str="",prix: int=0, ingredients:str=[] ):
        self.nom=nom
        self.prix=prix
        self.ingredients=ingredients
    def presenter_pizza(self):
        if self.nom=="":
            self.demander_nom()
            self.demander_prix()
            self.verifier_le_format_du_prix()
            self.demander_ingredients()
            print(f"Le nom de ce pizza est : {self.nom}" + f"\nSon prix : {self.prix} $".title() + f"\nSes ingredients sont: ".title() +", ".join(self.ingredients).title())
        else:
            print(f"Le nom de ce pizza est : {self.nom}" + f"\nSon prix : {self.prix} $".title() + f"\nSes ingredients sont: ".title() +", ".join(self.ingredients).title())
    def demander_nom(self):
        self.nom=input("Quel est le nom de votre pizza:  ")
    def demander_prix(self):
        self.prix=input("Quel est le prix de cette pizza: ")
    def verifier_le_format_du_prix(self):
        try:
            self.prix=int(self.prix)
        except:
            print("Valeur de prix incorrect entrez un chiffre !!!!")
            quit()
    def demander_ingredients(self):
        m=int(input("Combien d'ingrédients vous voulez mettre:  "))
        x=1
        for i in range(m):
            vol=input(f"Quel est le nom de l'ingredient {x} : ? ") 
            (self.ingredients).append(vol)
            x=x+1
pizza_x=Pizza()
pizza_x.presenter_pizza()

