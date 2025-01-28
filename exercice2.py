class Animal:
    def __init__(self,nom,espece):
        self.nom= nom
        self.espece= espece
        
    def Parler(self):
      print(self.nom , self.espece)
      print("je suis un " + self.espece)


class Chien(Animal):
   
   def __init__(self,espece, aboyer:str):
    
    self.espece=espece
    self.aboyer=aboyer

   def Parler(self) : 
        
    print(f"je suis un  { self.espece}  , {self.aboyer}")

print()
animal1=Animal("je suis rex","animal") 
animal1.Parler()

print()


chien=Chien("chien","ouaf!")
chien.Parler()
          
      
                    
