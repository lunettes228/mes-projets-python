class personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=int(age)
    def se_presenter(self):
        print(f"vous vous appelez : {self.nom}, vous avez : {self.age} ans".capitalize())
        
personne1=personne("jean", 30)
personne2=personne("paul", 25)
personne1.se_presenter()
personne2.se_presenter()
