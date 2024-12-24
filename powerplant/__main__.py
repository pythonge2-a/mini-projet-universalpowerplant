# Importantion de toutes les classes et méthodes
from powerplant import *
import os

loopcount = 0
app = App() # Création de l'application globale
kwhCSV_path = os.path.join("assets", "kwh_price.csv")
prix = KwhPrice(kwhCSV_path) # Création de l'objet prix
market = marketing() # Création de l'objet marketing
prod = production() # Création de l'objet production

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
    # Production

    production = prod.get_production_totale()
    if stock + production > app.my_frame.marketing_frame.stock_max:
        stock = app.my_frame.marketing_frame.stock_max
    else:
        stock += production

    # Vente
    if stock > 0: 
        unite_vendue = market.get_unit_sold(demand, stock)
        if unite_vendue > stock:
            unite_vendue = stock
    
        money += market.get_user_gain(prix_vente, unite_vendue)
        stock -= unite_vendue

    # Mise à jour sur l'interface
        app.my_frame.price_frame.kwh_stock = stock 
        app.my_frame.price_frame.money = money

    app.update_game()
    app.after(100, loop)

def main(): #initialisation des paramètres de lancement du jeu
    bank = 100
    kwh_stock = 100
    kwh_stock_max = 2000

    prod.add_moulin()
    app.my_frame.marketing_frame.set_stock_max(kwh_stock_max)
    app.my_frame.price_frame.set_kwh_stock(kwh_stock)
    app.my_frame.price_frame.set_money(bank)

    loop()
    app.mainloop()

if __name__ == "__main__":
    main()

