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
        self.places_reservees = set() #places reservées pour les abonnées

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
        if voiture not in self.voitures:
            self.voitures.append(voiture)

        if self.est_abonee(voiture):
            voiture.abone = False
            if voiture.place != "":
                self.places_reservees.discard(voiture.place)

            print("abonnement annulé")
        else:
            voiture.abone = True
            if voiture.place == "":
                libres = self.places_libres_sans_abonnement()
                if not libres:
                    raise RuntimeError("Impossible de réserver: aucune place disponible.")
                self.places_reservees.add(random.choice(libres))
            else:
                self.places_reservees.add(voiture.place)

            print("abonné")

    def placer(self, voiture):  # marche
        # si la voiture est pa dans a liste, on l'ajoute
        if voiture not in self.voitures:
            self.voitures.append(voiture)

        if voiture.abone:
            candidates = [p for p in self.places_reservees if self.place_libre(p)]

            if candidates:
                place_etage = random.choice(candidates)
            else:
                libres = self.places_libres_sans_abonnement()
                if not libres:
                    raise RuntimeError("Parking complet (hors places réservées).")
                place_etage = random.choice(libres)

        else:
            libres = self.places_libres_sans_abonnement()

            if not libres:
                raise RuntimeError("Parking complet (hors places réservées).")
            place_etage = random.choice(libres)

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
        toutes_les_places = self.toutes_les_places()
        for etage in range(5):          # 0–4
            for num in range(1, 81):    # 1–80
                toutes_les_places.append(num + etage * 100)

        # on enleve les ocupées
        places_libres = []
        for p in toutes_les_places:
                if p not in self.places_occupees and p not in self.places_reservees:
                    places_libres.append(p)

        return places_libres
    
    def toutes_les_places(self):
        toutes_les_places = []
        for etage in range(5):          # 0–4
            for num in range(1, 81):    # 1–80
                toutes_les_places.append(num + etage * 100)
        return toutes_les_places

    def place_libre(self, place):
        return place not in self.places_occupees

    def voiture_sur_place(self, place):
        for v in self.voitures:
            if v.place == place:
                return v
        return None
    

    def nombre_places_libres_sans_abonnement(self):
        return len(self.places_libres_sans_abonnement())

    def places_abonnees_occupees_par_autres(self):
        resultat = []
        for p in self.places_reservees:
            v = self.voiture_sur_place(p)
            if v is not None and not v.abone:
                resultat.append((p, v.immatriculation))
        return resultat

    def representer_niveau(self, etage: int):
        parts = []
        for num in range(1, 81):
            p = num + etage * 100
            if p in self.places_occupees:
                etat = "OCC"
            else:
                etat = "LIB"
            if p in self.places_reservees:
                etat += "R"
            parts.append(f"{num:02d}:{etat}")
        return " | ".join(parts)



        

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


        
    
        
    
                

    
            

    

    