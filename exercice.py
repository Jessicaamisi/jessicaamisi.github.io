class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur= longueur
        self.largeur= largeur
        
    def Aire(self):
      return self.largeur*self.longueur
    
    def Perimetre(self):
     return 2*(self.longueur + self.largeur) 
    
rectangle1=Rectangle(10,5)
print(rectangle1.Aire())
print(rectangle1.Perimetre())           
      
                    
