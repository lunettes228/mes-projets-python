class Personne:
    def __init__(self, nom=str(""), age=0):
        self.nom = nom
        self.age = int(age)

    def se_presenter(self):
        if self.nom == "" and self.age != 0:
            self.nom = input("quel est votre nom")
            print(
                f"mon nom est: {self.nom} , j'ai {self.age} ans".capitalize())
            self.age_legal()
        elif self.nom != "" and self.age != 0:
            print(
                f"mon nom est: {self.nom} , j'ai {self.age} ans".capitalize())
            self.age_legal()
        elif self.nom != "" and self.age == 0:
            print(
                f"votre nom est: {self.nom} , je ne connais pas votre age".capitalize())
        else:
            self.nom = input("quel est votre nom ? ")
            self.age = int(input("quel est votre age ? "))
            print(
                f"mon nom est: {self.nom} , j'ai {self.age} ans".capitalize())
            self.age_legal()
    def age_legal(self):
        if self.age >= 18:
            print(f"{self.nom}, vous etes majeur".capitalize())
        else:
            print(f"{self.nom}, vous etes mineur".capitalize())


personne1 = Personne()
personne1.se_presenter()
# personne2=personne("roger",14)
# personne2.se_presenter()
