class Livre:
    def __init__(self, auteur=str, titre=str, page=int):
        self.auteur=auteur
        self.titre=titre
        self.page=page
    def Retourner(self):
        print(f"voici le livre de : {self.auteur}, le titre est :  {self.titre} avec : {self.page} pages") 
class Bibliotheque:
    def Ajouter_livre(self,livre):
        n=5
        self.livre=["romeo et juliette", "homme miliardaire "]
        for i in range (0,n):

            self.livre.append(input("ajouter un livre:"))
    def Afficher_livres(self):
        print(f"afficher le titre de : {self.livre}")
    

livreA=Livre("JEAN-PAUL SARTRE","Huis clos",79)
livreA.Retourner()


livreB=Bibliotheque()
livreB.Ajouter_livre("")
livreB.Afficher_livres()
    