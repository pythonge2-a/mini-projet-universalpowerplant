# gère le stockage de l'énergie produite par les différentes sources d'énergie
#pas utilisée pour le moment 
class Storage :
    def __init__(self):

        self.n_capacitor = 0
        self.n_batterie = 0
        self.n_graphene_batterie = 0
        self.n_biocapacitor = 0
        self.n_magnetic_container = 0
        self.n_quantum_core = 0
        self.n_antimatter_chamber = 0 

        self.capacitor = 10
        self.batterie = 50
        self.graphene_batterie = 100
        self.biocapacitor = 250
        self.magnetic_container = 500
        self.quantum_core = 1000
        self.antimatter_chamber = 5000

        self.stock_max = 0
        self.stock_min = 200

    def get_stock(self):
        self.stock_max = self.stock_min + self.n_capacitor*self.capacitor + self.n_batterie*self.batterie + self.n_graphene_batterie*self.graphene_batterie + self.n_biocapacitor*self.biocapacitor + self.n_magnetic_container*self.magnetic_container + self.n_quantum_core*self.quantum_core + self.n_antimatter_chamber*self.antimatter_chamber


    
