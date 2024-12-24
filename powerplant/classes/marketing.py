# Fichier de gestion du marketing
# Définition du prix de vente utilisateur
# Calcul des gain/s en fonction de la demande

class marketing:
    def __init__(self):
        self.user_price = 0
        self.bank = 0

    def set_user_price(self, price):    #définit le prix de vente utilisateur
        self.user_price = price
        return self.user_price

    def set_user_bank(self, bank):    #définit la banque utilisateur (utile pour les tests unitaires)
        self.bank = bank
        return self.bank
    
    def get_user_bank(self):    #retourne la valeur de la banque utilisateur
        return self.bank
    
    def get_user_gain(self, selling_price, unit_sold):    #retourne les gains utilisateur par seconde
        return selling_price * unit_sold
    
    def update_user_bank(self, demand, storage):    #met à jour la banque utilisateur
        self.bank += self.get_user_gain(demand, storage)
        return self.bank
    
    def get_unit_sold(self, demand, storage):    #retourne le nombre d'unités vendues
        return storage * demand / 100