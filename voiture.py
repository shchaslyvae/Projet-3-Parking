import random
class Voiture:
    def __init__(self, immatriculation:str, marque:str, proprietaire:str ):
        self.immatriculation = immatriculation
        self.marque = marque
        self.proprietaire = proprietaire
        self.abone = False
        self.place = ""
    
    
    def immatriculation(self):
        return self.immatriculation
    
    def marque(self):
        return self.marque
    
    def proprietaire(self):
        return self.proprietere
    
    def abone(self):
        return self.abone
    
    def num_place(self):
        return self.place 

    


class Parking:
    def __init__ (self ):
        self.niveau = "0"
        self.voitures = []
        self.voiture = ""
        self.places_occupees = []


    def get_immatriculation(self, voiture): #marche
        """méthode pour afficher mmatriculation"""
        return voiture.immatriculation
    
    def get_marque(self, voiture): #marche
        return voiture.marque
    
    def get_proprietere(self, voiture): #marche
        return voiture.proprietaire
    
    def est_abonee(self, voiture): #marhce
        return voiture.abone 
    
    def get_num_place(self, voiture): #marche
        return voiture.place 
    
    def abonner(self, voiture: Voiture): #marche
        """méthode qui permett d'abonner ou d'annuler un abonnement """
        if self.est_abonee(voiture):
            voiture.abone = False
            print("abonnement annulé")
        else: 
            voiture.abone = True
            print("abonné")

    def placer(self, voiture): #marche 
        val = random.randint(0, 80)
        self.place = val
        self.etage = random.randint(0, 4)
        self.place_etage = self.place + (self.etage*100)
        self.places_occupees.append(self.place_etage)
        voiture.place = self.place_etage

    
    def place_occupee_voiture(self):
        for i in self.place_occupees:
            if i == self.place_etage:
                return self.get_immatriculation()
            
    def liste_place_abonnee(self):
        return self.place_occupees

    """
    def place_libre(self):
        place_libre = []
        for i in self.places_occupees:
            if i == self.place_etage:
                return 
    """
            
    def places_libres_sans_abonnement(self):
        self.places = []
        self.place_liste = 1
        self.niveau_liste = 0
        for i in range(5):
            for j in range(80):
                self.places.append(self.niveau_liste+self.niveau_liste)
                self.place_liste += 1
            self.niveau_liste += 100
            self.place_liste = 1
        for i in self.place_occupees:
            self.places.remove(i)
        return self.places
    
    def representer_niveau(self):
        return self.niveau_liste
        
        

voiture1 = Voiture("AA-001-AA", "BMW", "M. Informatique")
voiture2 = Voiture("AB-565-AB", "audi", "Piere")
parking = Parking()
parking.placer(voiture1)
parking.placer(voiture2)
#test 
"""
print(parking.get_num_place(voiture1))
print(parking.get_num_place(voiture2))
print(parking.get_marque(voiture1))
print(parking.get_marque(voiture2))
print(parking.get_immatriculation(voiture1))
print(parking.get_immatriculation(voiture2))
print(parking.get_proprietere(voiture1))
"""
print(parking.est_abonee(voiture1))
parking.abonner(voiture1)
parking.abonner(voiture1)

        
    
        
    
                

    
            

    

    