class Voiture:
 def __init__(self,marque=str,modele=str,annee=int):
    self.marque= marque
    self.modele= modele
    self.annee= annee
 def Demarrer(self):  
    print(f"la voiture {self.marque} , {self.modele}  demarre")  



voiture=Voiture("Mercedes benz", "ML", 1997)
voiture.Demarrer()