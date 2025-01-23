# Fichier de gestion du marketing
# Définition du prix de vente utilisateur
# Les méthodes en commentaires sont des méthodes qui n'ont pas été utilisées dans le jeu final

class marketing:
    def __init__(self):
        self.user_price = 0 #pas utilisé 
        self.bank = 0 #pas utilisé

    def get_user_gain(self, selling_price, unit_sold):    #retourne les gains utilisateur par seconde
        return selling_price * unit_sold
    
    
    def get_unit_sold(self, demand, storage):    #retourne le nombre d'unités vendues
        return int(storage * demand / 100)
    
