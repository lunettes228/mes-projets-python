class personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    def se_presenter(self):
        print(f"vous vous appelez : {self.nom}, vous avez : {self.age} ans".capitalize())
        self.est_majeur()
    def est_majeur(self):
        if self.age>=18:
            print(f"moi {self.nom} je suis majeur !!!!".capitalize())
            # return True
        else:
            print(f"moi {self.nom} je suis  mineur !!!".capitalize())
            # return False
            
        
personne1=personne("jean", 30)
personne2=personne("paul", 15)
personne1.se_presenter()
personne2.se_presenter()
