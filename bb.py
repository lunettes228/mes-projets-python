class Personne:
    def __init__(self, name=str(""), age=0):
        self.name = name
        self.age = int(age)
        
    def se_presenter(self):
        print(f"constructeur personne: {self.name}")
        if self.name == "" and self.age != 0:
            self.demander_nom()
            self.print_name_and_age()
            self.age_legal()
        elif self.name != "" and self.age != 0:
            self.print_name_and_age()
            self.age_legal()
        elif self.name != "" and self.age == 0:
            print(
                f"votre nom est: {self.name} , je ne connais pas votre age".capitalize())
        else:
            self.demander_nom()
            self.demander_age()
            self.print_name_and_age()
            self.age_legal()

    def print_name_and_age(self):
        print(
            f"mon nom est: {self.name} , j'ai {self.age} ans".capitalize())

    def demander_nom(self):
        self.name = input("quel est votre nom? ")

    def demander_age(self):
        self.age = int(input("quel est votre age ? "))

    def age_legal(self):
        if self.age >= 18:
            print(f"{self.name}, vous etes majeur".capitalize())
        else:
            print(f"{self.name}, vous etes mineur".capitalize())


personne1 = Personne("luc",17)
# personne1.se_presenter()
personne2 = Personne("jeanne",22)
# personne2.se_presenter()
# personne3=Personne()
# personne3.se_presenter()
# personne4=Personne()
# personne4.se_presenter()
liste=(personne1,personne2)
for i in liste:
    print(i.se_presenter())
    
    
