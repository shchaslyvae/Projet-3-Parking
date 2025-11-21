from random import*
class Voiture:
    def __init__(self, immatriculation:str, marque:str, proprietere:str ):
        self.immatriculation = immatriculation
        self.marque = marque
        self.proprietere = proprietere
        self.abone = False
        self.place = ""
    
    """
    def immatriculation(self):
        return self.immatriculation
    
    def marque(self):
        return self.marque
    
    def proprietere(self):
        return self.proprietere
    
    def abone(self):
        return self.abone
    
    def num_place(self):
        return self.place 

    """


class Parking:
    def __init__ (self, voiture:Voiture):
        self.niveau = "0"
        self.voitures = []
        self.voiture = voiture


    def get_immatriculation(self):
        return self.voiture.immatriculation
    
    def get_marque(self):
        return self.voiture.marque
    
    def get_proprietere(self):
        return self.voiture.proprietaire
    
    def est_abonee(self):
        return self.voiture.abone
    
    def get_num_place(self):
        return self.voiture.place 
    
    def abonner(self, voiture: Voiture):
        """méthode qui permett d'abonner ou d'annuler un abonnement """
        if voiture.est_abonee():
            voiture.abone = False
            print("abonnement annulé")
        else: 
            voiture.abonne = True
            print("abonné")

    def placer(self):
        self.place = random.randint(0,80)
        self.etages 

    
            

    

    