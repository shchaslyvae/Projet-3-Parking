# Projet-3-Parking - Avec Natael
# Documentation du projet MP3 — Gestion d’un parking

## Objectifs du projet

L’objectif de ce projet est de développer, en langage Python, un programme permettant de simuler la gestion d’un parking à l’aide de la programmation orientée objet. Le parking est composé de plusieurs niveaux et de places numérotées, sur lesquels des voitures peuvent être stationnées automatiquement.

Le projet permet de gérer les informations des voitures (immatriculation, marque, propriétaire), de distinguer les voitures abonnées des non-abonnées, de réserver des places spécifiques pour les abonnés et d’éviter les conflits de stationnement. Il permet également de connaître l’état du parking à tout moment : places libres, places occupées et places réservées. Ce travail a pour objectif de mettre en pratique les notions vues en cours, notamment les classes, les objets, les méthodes, les listes et les conditions.



## Mode d’utilisation du projet

Le projet s’utilise avec Python. Après avoir lancé le programme, il est possible de créer des objets de type `Voiture` en précisant l’immatriculation, la marque et le propriétaire. Ensuite, un objet `Parking` est créé pour gérer l’ensemble du stationnement.

Les voitures peuvent être abonnées à l’aide de la méthode `abonner()`, ce qui leur permet de bénéficier d’une place réservée. La méthode `placer()` permet de garer automatiquement une voiture sur une place disponible, en respectant les règles du parking (pas de double occupation et respect des places réservées).

Le programme permet également de consulter différentes informations : la liste des places occupées avec les immatriculations correspondantes, la vérification de la disponibilité d’une place, l’identification de la voiture stationnée sur une place donnée, le nombre de places libres hors abonnements ainsi que l’affichage textuel d’un niveau du parking.



## Répartition des tâches dans le binôme

Le travail a été réparti de manière équilibrée entre Natael et moi. Nous avons réalisé le projet ensemble, en travaillant sur la même logique et en nous concertant à chaque étape importante. Les tâches ont été partagées de façon équitable, chacun participant à la conception, à l’écriture et aux tests du code.

De mon côté, j’ai plus particulièrement vérifié l’ensemble des méthodes, corrigé certaines parties du programme, apporté les ajustements finaux nécessaires et rédigé la documentation complète du projet. 



## Difficultés rencontrées

Plusieurs difficultés ont été rencontrées lors de la réalisation du projet. La gestion des places réservées aux abonnés a nécessité une réflexion particulière afin d’éviter que des voitures non-abonnées ne s’y garent. Il a également fallu empêcher que deux voitures puissent occuper la même place lors de l’attribution aléatoire.


## Améliorations possibles

Plusieurs améliorations pourraient être apportées au projet. Il serait possible d’ajouter une interface graphique pour rendre l’utilisation plus intuitive et visuelle. On pourrait également améliorer la gestion des abonnements en associant explicitement chaque place réservée à un abonné précis.

D’autres améliorations incluent la gestion de la sortie des voitures, la sauvegarde de l’état du parking dans un fichier, l’ajout de messages utilisateurs plus détaillés ou encore une représentation plus graphique des niveaux du parking. Ces évolutions permettraient de rendre le projet plus complet et plus proche d’une application réelle.

