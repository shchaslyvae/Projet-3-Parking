import random

class Voiture:
    def __init__(self, immatriculation: str, marque: str, proprietaire: str):
        self.immatriculation = immatriculation
        self.marque = marque
        self.proprietaire = proprietaire
        self.abone = False
        self.place = ""


class Parking:
    def __init__(self):
        self.niveau = "0"
        self.voitures = []          # les voitures dans parking
        self.places_occupees = []   # liste des plaves occupées

    def get_immatriculation(self, voiture):  # marche
        """méthode pour afficher immatriculation"""
        return voiture.immatriculation

    def get_marque(self, voiture):  # marche
        return voiture.marque

    def get_proprietere(self, voiture):  # marche
        return voiture.proprietaire

    def est_abonee(self, voiture):  # marche
        return voiture.abone

    def get_num_place(self, voiture):  # marche
        return voiture.place

    def abonner(self, voiture: Voiture):  # marche
        """méthode qui permet d'abonner ou d'annuler un abonnement"""
        if self.est_abonee(voiture):
            voiture.abone = False
            print("abonnement annulé")
        else:
            voiture.abone = True
            print("abonné")

    def placer(self, voiture):  # marche
        # si la voiture est pa dans a liste, on l'ajoute
        if voiture not in self.voitures:
            self.voitures.append(voiture)

        place = random.randint(1, 80)      # numero de place
        etage = random.randint(0, 4)       # etage
        place_etage = place + (etage * 100)

        
        self.places_occupees.append(place_etage)
        voiture.place = place_etage

    def place_occupee_voiture(self):
        resultats = []
        for v in self.voitures:
            if v.place != "":
                resultats.append((v.immatriculation, v.place))
        return resultats

    def liste_place_abonnee(self):
        return self.places_occupees

    def places_libres_sans_abonnement(self):
        toutes_les_places = []
        for etage in range(5):          # 0–4
            for num in range(1, 81):    # 1–80
                toutes_les_places.append(num + etage * 100)

        # on enleve les ocupées
        places_libres = []
        for p in toutes_les_places:
            if p not in self.places_occupees:
                places_libres.append(p)

        return places_libres

        

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
"""
print(parking.est_abonee(voiture1))
parking.abonner(voiture1)
parking.abonner(voiture1)
"""
print("Places occupées (immatriculation, place):")
print(parking.place_occupee_voiture())

print("Liste des places occupées :")
print(parking.liste_place_abonnee())

print("Place de la voiture 1:", parking.get_num_place(voiture1))
print("Place de la voiture 2:", parking.get_num_place(voiture2))


        
    
        
    
                

    
            

    

    