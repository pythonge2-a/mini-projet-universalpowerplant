[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/oOQR1xPR)
# Universal Powerplant

## Membres

- Dos Santos Yann
- Sena Pablo
- Djéhiche Jéremie
- Porret Leo
- Uluçinar Can

## Description

### Concept initial
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
- Implementation de sauvegardes du jeu via Pickle 
- Un terminal avec des messages
- Ajout d'un lore

## Installation

```bash
poetry install # installe les dépendances du projet
poetry run powerplant # lance le programme
```

## Problèmes de dépendances et de versions 
Si des erreurs surviennent lorsque vous essayez de lancer le jeu, essayer les solutions suivantes.

### Mauvaise version de Python 
Pour mettre Python à jour vers Python 3.13.0 suivez les instructions suivantes : 
```bash
# Update package lists{
sudo apt update

# Install dependent libraries:
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev

# Download Python binary package:
wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz

# Unzip the package:
tar -xzf Python-3.13.0.tgz

# Execute configure script
cd Python-3.13.0
./configure --enable-optimizations

# Build Python 3.13
make -j 2

# Install Python 3.13
sudo make install

# Verify the installation
python3.13
```

### Lorsque l'erreur vient de tkinter 
```bash
sudo apt install tk-dev libsqlite3-dev libssl-dev libffi-dev zlib1g-dev
```

```bash
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tar.xz
sudo tar -xf Python-3.13.0.tar.xz
cd Python-3.13.0
```

```bash
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
```

```bash
python3.13 -m tkinter
```

Une fenêtre de tkinter devrait s'ouvrir. Si ce n'est pas le cas et que des problèmes de droit d'écritures surviennent, essayez :
```bash
sudo chown -R yann:yann /usr/src/Python-3.13.0
```

```bash
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
```

```bash
python3.13 -m tkinter
```
Une fenêtre de tkinter devrait s'ouvrir.

### Lorsque l'erreur vient de drivers audio (pygame.mixer)

```bash
sudo apt update
sudo apt install libsdl2-mixer-2.0-0
```

## Lancement des tests
```bash
poetry run pytest tests/test_Game.py
```
