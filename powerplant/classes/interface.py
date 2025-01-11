import customtkinter
from . import *
 
class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
 
        # Configure the grid layout for the MainFrame
        self.grid_rowconfigure(0, weight=1)  # One row
        self.grid_rowconfigure(1, weight=3)  # One row
        self.grid_columnconfigure(0, weight=1)  # Three columns
        self.grid_columnconfigure((1,2), weight=2)  # Three columns
 
        # add widgets onto the frame
        self.price_frame = PriceFrame(master=self)
        self.price_frame.grid(row=0, column=0, padx=5, pady=5, sticky="w")
 
        self.stock_frame = StockFrame(master=self)
        self.stock_frame.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.marketing_frame = MarketingFrame(master=self)
        self.marketing_frame.grid(row=0, column=1, padx=5, pady=5, sticky="w")
 
        self.invest_frame = InvestFrame(master=self)
        self.invest_frame.grid(row=1, column=0, padx=5, pady=5, sticky="w")      
 
class PriceFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._bg_color="#EAEAEA"
 
        self.kwh_stock = 0
        self.money = 0
        self.stock_max = 0
 
        # add widgets onto the frame
        self.price_label = customtkinter.CTkLabel(self, text="fr -----",width=300,anchor="w")
        self.price_label.grid(row=0,column=0,padx=10,pady=2,sticky="w",)
 
        self.main_button = customtkinter.CTkButton(self, text="Generate energy",command=self.generate_kwh,fg_color="#7ED8FF")
        self.main_button.grid(row=2,column=0,padx=10,pady=15)
 
       
        self.kwh_label = customtkinter.CTkLabel(self, text=" Unsold Stock : ///// kWh",width=300,anchor="w")
        self.kwh_label.grid(row=1,column=0,padx=10,pady=2,sticky="w")
 
    def set_kwh_stock(self, kwh):
        self.kwh_stock = kwh
        return self.kwh_stock
   
    def set_money(self, money):
        self.money = money
        return self.money
    
    def set_stock_max(self, stock_max):
        self.stock_max = stock_max
        return self.stock_max
   
    def update_mk(self): #Mise à jour des paramètres de l'interface
        self.price_label.configure(text=f"Avaible Funds : {self.money:.4f} fr")
        self.kwh_label.configure(text=f"Unsold Stock : {self.kwh_stock:.4f} kWh / {self.stock_max} ")
 
    def generate_kwh(self):
        self.kwh_stock+=1

class StockFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._bg_color="#EAEAEA"

        # add widgets onto the frame
        self.stock_label = customtkinter.CTkLabel(self, text="Stockage :", font=("Arial", 16))
        self.stock_label.grid(row=0,column=0, padx=10, pady=15, sticky="w")
   
        self.capa_button = customtkinter.CTkButton(self,text="capacitor")
        self.capa_button.grid(row=1,column=0, padx=10, pady=5, sticky="w")
 
        self.pile_button = customtkinter.CTkButton(self,text="aa cell")
        self.pile_button.grid(row=2,column=0, padx=10, pady=5, sticky="w")
 
        self.batterie_button = customtkinter.CTkButton(self,text="batterie")
        self.batterie_button.grid(row=3,column=0, padx=10, pady=5, sticky="w")
 
        self.graphene_button = customtkinter.CTkButton(self,text="graphene")
        self.graphene_button.grid(row=4,column=0, padx=10, pady=5, sticky="w")
 
        self.antimat_button = customtkinter.CTkButton(self,text="antimatter")
        self.antimat_button.grid(row=5,column=0, padx=10,pady=5, sticky="w")
 
class InvestFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._bg_color="#EAEAEA"
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        self.nDyson = 0
        self.nMonkey = 0
        # add widgets onto the frame
        self.invest_label = customtkinter.CTkLabel(self, text="Investments :", font=("Arial", 16))
        self.invest_label.grid(row=0,column=0, padx=10, pady=15, sticky="w")
   
        self.monkey_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#7ED8FF",hover_color="#0078AC")
        self.monkey_button.grid(row=1,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.monkeyCnt_label = customtkinter.CTkLabel(self, text="- Monkey on a bike")
        self.monkeyCnt_label.grid(row=1,column=0, padx=5,pady=0,sticky="w")
        self.monkeyCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.monkeyCost_label.grid(row=2,column=0, padx=5,pady=0,sticky="w")

        self.mushroom_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#7ED8FF",hover_color="#0078AC")
        self.mushroom_button.grid(row=3,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.mushroomCnt_label = customtkinter.CTkLabel(self, text="- Bioluminescent Mushroom")
        self.mushroomCnt_label.grid(row=3,column=0, padx=5,pady=0,sticky="w")
        self.mushroomCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.mushroomCost_label.grid(row=4,column=0, padx=5,pady=0,sticky="w")

        self.solar_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#7ED8FF",hover_color="#0078AC")
        self.solar_button.grid(row=5,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.solarCnt_label = customtkinter.CTkLabel(self, text="- Solar Panel")
        self.solarCnt_label.grid(row=5,column=0, padx=5,pady=0,sticky="w")
        self.solarCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.solarCost_label.grid(row=6,column=0, padx=5,pady=0,sticky="w")

        self.biomass_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#7ED8FF",hover_color="#0078AC")
        self.biomass_button.grid(row=7,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.biomassCnt_label = customtkinter.CTkLabel(self, text="- Biomass plant")
        self.biomassCnt_label.grid(row=7,column=0, padx=5,pady=0,sticky="w")
        self.biomassCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.biomassCost_label.grid(row=8,column=0, padx=5,pady=0,sticky="w")

        self.nuclear_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#7ED8FF",hover_color="#0078AC")
        self.nuclear_button.grid(row=9,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.nuclearCnt_label = customtkinter.CTkLabel(self, text="- Nuclear plant")
        self.nuclearCnt_label.grid(row=9,column=0, padx=5,pady=0,sticky="w")
        self.nuclearCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.nuclearCost_label.grid(row=10,column=0, padx=5,pady=0,sticky="w")

        self.fusion_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#0078AC",hover_color="#7ED8FF")
        self.fusion_button.grid(row=11,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.fusionCnt_label = customtkinter.CTkLabel(self, text="- Fusion reactor")
        self.fusionCnt_label.grid(row=11,column=0, padx=5,pady=0,sticky="w")
        self.fusionCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.fusionCost_label.grid(row=12,column=0, padx=5,pady=0,sticky="w")

        self.dyson_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#0078AC",hover_color="#7ED8FF")
        self.dyson_button.grid(row=13,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.dysonCnt_label = customtkinter.CTkLabel(self, text="- Dyson Sphere")
        self.dysonCnt_label.grid(row=13,column=0, padx=5,pady=0,sticky="w")
        self.dysonCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.dysonCost_label.grid(row=14,column=0, padx=5,pady=0,sticky="w")

        self.galaxy_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#0078AC",hover_color="#7ED8FF")
        self.galaxy_button.grid(row=15,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.galaxyCnt_label = customtkinter.CTkLabel(self, text="- Galaxy Harvester")
        self.galaxyCnt_label.grid(row=15,column=0, padx=5,pady=0,sticky="w")
        self.galaxyCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.galaxyCost_label.grid(row=16,column=0, padx=5,pady=0,sticky="w")

        self.dimesional_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#0078AC",hover_color="#7ED8FF")
        self.dimesional_button.grid(row=17,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.dimesionalCnt_label = customtkinter.CTkLabel(self, text="- Dimensional generator")
        self.dimesionalCnt_label.grid(row=17,column=0, padx=5,pady=0,sticky="w")
        self.dimesionalCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.dimesionalCost_label.grid(row=18,column=0, padx=5,pady=0,sticky="w")

        self.grandma_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color="#0078AC",hover_color="#7ED8FF")
        self.grandma_button.grid(row=19,column=1, padx=5, pady=0, sticky="w", rowspan=2)
        self.grandmaCnt_label = customtkinter.CTkLabel(self, text="- Grandma's love")
        self.grandmaCnt_label.grid(row=19,column=0, padx=5,pady=0,sticky="w")
        self.grandmaCost_label =customtkinter.CTkLabel(self,text="Price : --")
        self.grandmaCost_label.grid(row=20,column=0, padx=5,pady=0,sticky="w")


    def update_prod(self):
        self.monkeyCnt_label.configure(text=f"{self.nMonkey} Monkeys")
        self.dysonCnt_label.configure(text=f"{self.nDyson} Dyson Spheres")
 
 
class MarketingFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._bg_color="#EAEAEA"
 
        self.selling_price = 0.2 # Prix de base
        self.demand = 0
        self.gainpers = 0
 
        # add widgets onto the frame
        self.marketing_label = customtkinter.CTkLabel(self, text="Marketing :", font=("Arial", 16))
        self.marketing_label.grid(row=0,column=0, padx=10, pady=15, sticky="w")
 
        self.price_label = customtkinter.CTkLabel(self, text="-- fr")
        self.price_label.grid(row=1,column=0,padx=5,pady=5)
 
        self.increasePrice_button = customtkinter.CTkButton(
            master=self,
            text="+",
            command=self.increase_price,
            corner_radius=10,  # Set the corner radius to half the height for a circular shape
            width=20,  # Make the button square for a true circle
            height=20,
            fg_color="#7ED8FF",  # Set the button color
            text_color="black"  # Set the text color
        )
        self.increasePrice_button.grid(row=1,column=1)
        self.decreasePrice_button = customtkinter.CTkButton(
            master=self,
            text="-",
            command=self.decrease_price,
            corner_radius=10,  # Set the corner radius to half the height for a circular shape
            width=20,  # Make the button square for a true circle
            height=20,
            fg_color="#7ED8FF",  # Set the button color
            text_color="black"  # Set the text color
        )
        self.decreasePrice_button.grid(row=1,column=2)
 
        self.demand_label = customtkinter.CTkLabel(self, text="Demand -- %")
        self.demand_label.grid(row=2,column=0,sticky="w")
 
        self.gainpers_label = customtkinter.CTkLabel(self, text="Gain/s ---")
        self.gainpers_label.grid(row=3,column=0, sticky="w")
 
    def update_price_label(self):
        self.price_label.configure(text=f"{self.selling_price:.2f} fr")
   
    def increase_price(self):
        self.selling_price += 0.01
        self.update_price_label()
 
    def decrease_price(self):
        if self.selling_price > 0.01:  # Empêche d'avoir un prix négatif
            self.selling_price -= 0.01
        self.update_price_label()

    def update_pstk(self): #Mise à jour des paramètres de l'interface
        self.demand_label.configure(text=f"Demand : {self.demand:.2f} %")
        self.gainpers_label.configure(text=f"Gain/s : {self.gainpers:.4f}")

 
class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
 
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=10)
        self.button1 = customtkinter.CTkButton(self, text="bouton 1", command=self.button1_action)
        self.button1.grid(row=1,column=0,padx=10)
 
    def button1_action(self) :
        self.button1.configure(state="disabled", text="womp womp")
 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
 
        self.my_frame = MainFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
 
    def update_game(self):
        self.my_frame.marketing_frame.update_pstk()
        self.my_frame.price_frame.update_mk()
        self.my_frame.invest_frame.update_prod()