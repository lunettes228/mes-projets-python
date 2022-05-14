class personne:
    def __init__(self,nom="",age=0):
        self.nom=nom
        self.age=age
    def se_presenter(self):
        if self.nom !="" and self.age!=0:
            print(f"vous vous appelez : {self.nom}, vous avez : {self.age} ans".capitalize())
            self.est_majeur()
        elif self.nom=="":
            self.x=input("quel est votre nom ? :")
            print(f"vous vous appelez : {self.x}, vous avez : {self.age} ans".capitalize())
            self.est_majeur()
        elif self.age==0:
            print(f"vous vous appelez {self.nom}, je ne connais pas votre age!!!")
        else:
             print(f"vous vous appelez {self.x}, je ne connais pas votre age!!!")
    def est_majeur(self):
        if self.age>=18:
            print(f"{self.nom} vous etes majeur !!!!".capitalize())
            # return True
        elif self.nom=="" and self.age>=18:
            print(f"{self.x} vous etes majeur !!!!".capitalize())
        elif self.nom=="" and self.age<18:
            print(f"{self.x} vous etes mineur !!!!".capitalize())
        else:
            print(f"{self.nom} vous etes mineur !!!!".capitalize())
            # return False
            
        
personne1=personne()
personne2=personne()
personne1.se_presenter()
personne2.se_presenter()
