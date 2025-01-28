class CompteBancaire:
    def __init__(self):
        self.solde=0
    def Menu(self): 
         
         print("entrer l' option de votr choix")
         print("1. deposer le montant ")
         print("2. retirer le montant")
         print("3.. afficher le solde ") 
         
         while True:
            Menu()
            option= int(input("faites votre choix"))
            if option=='1':
                self.Deposer()
            elif option=='2':
                self.Retirer()
            elif option=='3':
                self.Afficher()
            else:
                print("au revoir")
                break                   
    def Deposer(self,solde_final):
        self.solde=self.solde +  solde_final
    def Retirer(self,solde_final):
        if self.solde>=solde_final:
            return self.solde - solde_final 
        else:
            print(f"pas de retrait possible")
    def Afficher(self):
        print(f"le solde actuel est: {self.solde}")

solde1=CompteBancaire()
solde1.Deposer(1000)
solde1.Retirer(5000)
solde1.Afficher()