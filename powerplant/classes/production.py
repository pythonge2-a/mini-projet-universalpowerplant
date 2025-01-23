# Fichier de gestion de la production d'énergie
# Gère la production active et passive d'énergie

class production:
    def __init__(self):
        self.production_active = 0
        self.production_passive = 0

        # Assets production passive
        self.singe          = 1         # Singe sur un vélo
        self.moulin         = 10        # Moulin à eau
        self.champignon     = 50        # Ferme de champignons bioluminescents
        self.solaire        = 100       # Panneau solaire
        self.biomasse       = 250       # Ferme de biomasse
        self.nucleaire      = 500       # Centrale nucléaire
        self.fusion         = 1000      # Réacteur de fusion
        self.dyson          = 5000      # Sphère de Dyson
        self.galaxy         = 10000     # Galaxy harveseter
        self.dimension      = 100000    # Centrale dimensionnelle
        self.grandmere      = 1000000   # L'amour de grand-mère

        self.nSinge         = 0
        self.nMoulin        = 0
        self.nChampignon    = 0
        self.nSolaire       = 0
        self.nBiomasse      = 0
        self.nNucleaire     = 0
        self.nFusion        = 0
        self.nDyson         = 0
        self.nGalaxy        = 0
        self.nDimension     = 0
        self.nGrandmere     = 0

    def update_production_passive(self):
        self.production_passive = self.nSinge*self.singe + self.nMoulin*self.moulin + self.nChampignon*self.champignon + self.nSolaire*self.solaire + self.nBiomasse*self.biomasse + self.nNucleaire*self.nucleaire + self.nFusion*self.fusion + self.nDyson*self.dyson + self.nDimension*self.dimension + self.nGrandmere*self.grandmere
        return self.production_passive
    
    def get_production_totale(self):
        self.update_production_passive()
        return self.production_active + self.production_passive
    



        

