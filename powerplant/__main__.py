# Importantion de toutes les classes et méthodes
from powerplant import *
import os

loopcount = 0
app = App() # Création de l'application globale
kwhCSV_path = os.path.join("assets", "kwh_price.csv")
prix = KwhPrice(kwhCSV_path) # Création de l'objet prix
market = marketing() # Création de l'objet marketing
prod = production() # Création de l'objet production
storage = Storage() # Création de l'objet storage

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
    money = app.my_frame.price_frame.get_money()
    gainpers = app.my_frame.marketing_frame.gainpers
    gain = 0

    prod.nSinge = app.my_frame.invest_frame.nSinge
    prod.nMoulin = app.my_frame.invest_frame.nMoulin
    prod.nChampignon = app.my_frame.invest_frame.nChampignon
    prod.nSolaire = app.my_frame.invest_frame.nSolaire
    prod.nBiomasse = app.my_frame.invest_frame.nBiomasse
    prod.nNucleaire = app.my_frame.invest_frame.nNucleaire
    prod.nFusion = app.my_frame.invest_frame.nFusion
    prod.nDyson = app.my_frame.invest_frame.nDyson
    prod.nGalaxy = app.my_frame.invest_frame.nGalaxy
    prod.nDimension = app.my_frame.invest_frame.nDimension
    prod.nGrandmere = app.my_frame.invest_frame.nGrandmere

    storage.n_capacitor = app.my_frame.stock_frame.nCapacitor
    storage.n_batterie = app.my_frame.stock_frame.nBatterie
    storage.n_graphene_batterie = app.my_frame.stock_frame.nGraphene_batterie
    storage.n_biocapacitor = app.my_frame.stock_frame.nBiocapacitor
    storage.n_magnetic_container = app.my_frame.stock_frame.nMagnetic_container
    storage.n_quantum_core = app.my_frame.stock_frame.nQuantum_core
    storage.n_cosmic_crystal = app.my_frame.stock_frame.nCosmic_crystal
    storage.n_antimatter_chamber = app.my_frame.stock_frame.nAntimatter_chamber
    

    # Production
    production = prod.get_production_totale()
    if stock + production > app.my_frame.price_frame.stock_max:
        stock = app.my_frame.price_frame.stock_max
    else:
        stock += production

    # Vente
    if stock > 0 and loopcount % 10 == 0: 
        unite_vendue = market.get_unit_sold(demand, stock)
        if unite_vendue > stock:
            unite_vendue = stock
        gain = market.get_user_gain(prix_vente, unite_vendue)
        gainpers = gain
        money += gain
        stock -= unite_vendue
    else:
        if stock == 0:
            gainpers = 0

    # stockage
    kwh_stock_max = storage.get_stock()

    # Mise à jour sur l'interface
    app.my_frame.price_frame.kwh_stock = stock 
    app.my_frame.price_frame.set_money(money)
    app.my_frame.marketing_frame.demand = demand
    app.my_frame.marketing_frame.gainpers = gainpers 
    app.my_frame.price_frame.stock_max = kwh_stock_max

    app.update_game()
    app.after(100, loop)

def main(): #initialisation des paramètres de lancement du jeu

    kwh_stock_max = 500

    app.my_frame.price_frame.set_stock_max(kwh_stock_max)
    loop()
    app.mainloop()

if __name__ == "__main__":
    main()

