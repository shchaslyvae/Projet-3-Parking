# Fonction Voiture

A être complété

# Fonction Parking

J'ai crée plusieurs méthodes pour repésenter le parking :

- ```__init__``` : Initialise le niveau, les voitures et les places occupées
- ```get_immatriculation``` : renvoie l'immatriculation de la voiture
- ```get_marque``` : renvoie la marque de la voiture
- ```get_proprietere``` : renvoie le propriétaire de la voiture
- ```get_abonee``` : renvoie l'abonnement de la voiture
- ```get_num_place``` : Renvoie le numéro de place de la voiture
- ```placer``` : Si le numéro de place de la voiture n'est pas dans ```self.voitures```, on la place. Choisit un nombre aléatoire pour la place entre 0 et 80, et pour l'étage entre 0 et 4 et utilisant le module randint.
- ```place_libre``` : Renvoie les places libres
- ```place_occupee_voiture``` : Retourne l'immatriculation de la voiture qui occupe la place
- ```liste_place_abonnee``` : Renvoie la liste des places occupées.
- ```places_libres_sans_abonnement``` : Crée une liste de toutes les places, et de cette liste, crée une liste de places libres qui n'ont pas d'abonnement.
- ```representer_niveau``` : Renvoie le niveau auquel la voiture est située.