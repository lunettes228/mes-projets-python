class personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    def se_presenter(self):
        print(f"vous vous appelez : {self.nom}, vous avez : {self.age} ans".capitalize())
    def est_majeur(self):
        return self.age>=18
            # print(f"{self.nom} vous etes majeur !!!!".capitalize())
        #     return True
        # else:
            # print(f"{self.nom} vous n'estes pas majeur !!!".capitalize())
            # return False
            
        
personne1=personne("jean", 30)
personne2=personne("paul", 15)
personne1.se_presenter()
print(f"est majeur1: {personne1.est_majeur()}".capitalize())
personne2.se_presenter()
print(f"est majeur 2: {personne2.est_majeur()}".capitalize())