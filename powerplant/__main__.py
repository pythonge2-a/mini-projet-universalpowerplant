# Importantion de toutes les classes et méthodes
from powerplant import *
import os

loopcount = 0
app = App() # Création de l'application globale
kwhCSV_path = os.path.join("assets", "kwh_price.csv")
prix = KwhPrice(kwhCSV_path) # Création de l'objet prix
market = marketing() # Création de l'objet marketing

def loop(): #boucle du jeu , actualise les paramètres du jeu toute les secondes

    global loopcount
    loopcount += 1
    day = 0
 
    #actualisation des jours (1 jour = 30 secondes)
    if loopcount % 30 == 0: #
        day = loopcount // 30

    # actualisation des paramètres du jeu
    demand = prix.get_demand(day, app.my_frame.marketing_frame.selling_price) #Mise à jour de la demande
    prix_vente = app.my_frame.marketing_frame.selling_price
    stock = app.my_frame.price_frame.kwh_stock
    money = app.my_frame.price_frame.money

    if stock > 0: 
        if app.my_frame.price_frame.kwh_stock < 1: #forcer la vente si le stock est inférieur à 1
            unite_vendue = app.my_frame.price_frame.kwh_stock
        else:
            unite_vendue = market.get_unit_sold(demand, stock)

        money += market.get_user_gain(prix_vente, unite_vendue)
        stock -= unite_vendue

    # Mise à jour sur l'interface
        app.my_frame.price_frame.kwh_stock = stock 
        app.my_frame.price_frame.money = money

    app.update_game()
    app.after(1000, loop)

def main(): #initialisation des paramètres de lancement du jeu
    bank = 1000
    kwh_stock = 1000
    market.set_user_bank(bank)
    app.my_frame.marketing_frame.set_stock_max(bank)
    app.my_frame.price_frame.set_kwh_stock(kwh_stock)

    loop()
    app.mainloop()

if __name__ == "__main__":
    main()

