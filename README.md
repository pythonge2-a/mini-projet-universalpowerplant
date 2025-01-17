[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/oOQR1xPR)
# Universal Powerplant

## Membres

- Dos Santos Yann
- Sena Pablo
- Djéhiche Jéremie
- Porret Leo
- Uluçinar Can

## Description

### Concept  
Le joueur contrôle une IA programmée pour maximiser la production d'énergie électrique. Le but ultime est de convertir toute la matière de l'univers en énergie, atteignant une omnipotence énergétique.

### Déroulement du jeu  
1. **Phase 1 : Production manuelle**  
   - Production d’énergie via un bouton manuel.  
   - Vente d’énergie pour accumuler des fonds.  

2. **Phase 2 : Automatisation**  
   - Construction de machines : éoliennes, générateurs à charbon, panneaux solaires.  

3. **Phase 3 : Optimisation technologique**  
   - Déblocage d’innovations : stockage avancé, générateurs améliorés, nouvelles sources d’énergie (fusion nucléaire, antimatière).  

4. **Phase 4 : Expansion planétaire**  
   - Exploitation des ressources d’autres planètes et collecte d’énergie dans l’espace.  

5. **Phase 5 : Omnipotence énergétique**  
   - Conversion des galaxies en énergie et redémarrage de l’univers.  

---

### Mini-jeux intégrés  
1. **Jeu de câblage**  
   - Objectif : Connecter des points pour compléter un circuit.  
   - Récompense : A définir.  

2. **Jeux sinus**  
   - Objectif : Faire correspondre un sinus fixe à un autre à régler.  
   - Récompense : A définir.  

3. **Jeux de la dynamo**  
   - Objectif : Acheter/vendre de l’énergie au meilleur moment.  
   - Récompense : Augmente la production d'énergie réaliser par rapport au nombre de tour réalisé.  

4. **Jeux du simon**  
   - Objectif : Appliquer une séquence de couleurs sur des boutons de couleurs.  
   - Récompense : A définir.  

---

## Objectifs
- Concevoir un jeu incrémental captivant basé sur la production et l’optimisation de l’énergie.  
- Intégrer des mécaniques variées, comme les mini-jeux, pour maintenir l’intérêt du joueur.  
- Explorer des concepts technologiques et philosophiques liés à l’exploitation énergétique.  


## Cahier des charges

### A réaliser (Obligatoirement) :
- Création d'une interface
- Création des mini-jeux
- Création d'une palette de jeux
- Définir le prix de ventes d'énergie
- Créer un système de production


### A réaliser (si le temps nous le permet) :
- Implementation d'un bouton de sauvegarde du jeux via Pickle. 
- Implementation d'un bouton de chargement de la sauvegarde via Pickle
- Un terminal avec des messages
- Ajout d'un lore

## Installation

```bash
poetry install # installe les dépendances du projet
poetry run powerplant # lance le programme
```

## Gestion des dépendances

Si il y besoin d'installer des dépendances pour la création de classes, vous pouvez utiliser Poetry pour gérer les dépendances du projet. Par exmple, pour installer numpy:
```bash
poetry add numpy # ajoute numpy au projet
poetry show # affiche les dépendances incluses du projet
...
```
## (Pour les étudiants, à supprimer une fois fait)

### Comment créer le module

1. Créer un nouveau répertoire avec le nom du module
2. Créer un fichier `__init__.py` vide
3. Créer un fichier `__main__.py` vide
4. Mettre à jour le fichier `README.md`
5. Créer un projet Poetry avec `poetry new`
6. Ajouter les fichiers à Git
7. Commit et push
