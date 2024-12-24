# Importantion de toutes les classes et méthodes
from powerplant import *
import os

loopcount = 0
app = App() # Création de l'application globale
kwhCSV_path = os.path.join("assets", "kwh_price.csv")
prix = KwhPrice(kwhCSV_path) # Création de l'objet prix
market = marketing() # Création de l'objet marketing

def loop(): #boucle de jeu , actualise les paramètres du jeu toute les secondes

    global loopcount
    loopcount += 1
    day = 0
 
    if loopcount % 30 == 0: #actualisation des jours
        day = loopcount // 30

    demand = prix.get_demand(day, app.my_frame.marketing_frame.selling_price) #Mise à jour de la demande

    if app.my_frame.price_frame.kwh_stock > 0: # Vente d'électricité
        prix_vente = app.my_frame.marketing_frame.selling_price
        unite_vendue = app.my_frame.price_frame.kwh_stock * demand / 100

        if app.my_frame.price_frame.kwh_stock < 1: #forcer la vente si le stock est inférieur à 1
            unite_vendue = app.my_frame.price_frame.kwh_stock

        gain = prix_vente * unite_vendue
        app.my_frame.price_frame.kwh_stock -= unite_vendue
        app.my_frame.price_frame.money += gain

    app.update_game()
    app.after(1000, loop)

def run():
    loop()
    app.mainloop()

def main(): #initialisation des paramètres de lancement du jeu
    bank = 1000
    kwh_stock = 1000
    market.set_user_bank(bank)
    app.my_frame.marketing_frame.set_stock_max(bank)
    app.my_frame.price_frame.set_kwh_stock(kwh_stock)

    run()

if __name__ == "__main__":
    main()

