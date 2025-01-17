import customtkinter
import subprocess
from . import *
 
class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.background_color = colors.background_color
        # Configure the grid layout for the MainFrame
        self.grid_rowconfigure(0, weight=1)  # One row
        self.grid_rowconfigure(1, weight=3)  # One row
        #self.grid_columnconfigure(0, weight=1)  # Three columns
        self.grid_columnconfigure((0,1,2,3), weight=1)  # Three columns
 
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
        self._bg_color=colors.background_color
 
        self.kwh_stock = 0
        self.money = 0
        self.stock_max = 0
 
        # add widgets onto the frame
        self.price_label = customtkinter.CTkLabel(self, text="fr -----",width=300,anchor="w")
        self.price_label.grid(row=0,column=0,padx=10,pady=2,sticky="w",)
 
        self.main_button = customtkinter.CTkButton(self, text="Generate energy", text_color="black",command=self.generate_kwh,fg_color=colors.lightButton_color)
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
        self._bg_color=colors.background_color

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        # add widgets onto the frame
        self.stock_label = customtkinter.CTkLabel(self, text="Stockage :", font=("Arial", 16))
        self.stock_label.grid(row=0,column=0, padx=10, pady=15, sticky="w")

        self.capa_label = customtkinter.CTkLabel(self,justify="left", text="10 Capacitors\nCAP x nb KWH\nPrice :")
        self.capa_label.grid(row=1,column=0, padx=10,pady=10,sticky="w")
        self.capa_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color)
        self.capa_button.grid(row=1,column=1, padx=5, pady=0, sticky="w")

        self.battAA_label = customtkinter.CTkLabel(self,justify="left", text="10 AA Batteries\nCAP x nb KWH\nPrice :")
        self.battAA_label.grid(row=2,column=0, padx=10,pady=10,sticky="w")
        self.battAA_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color)
        self.battAA_button.grid(row=2,column=1, padx=5, pady=0, sticky="w")

        self.graphene_label = customtkinter.CTkLabel(self,justify="left", text="10 Graphene Batteries\nCAP x nb KWH\nPrice :")
        self.graphene_label.grid(row=3,column=0, padx=10,pady=10,sticky="w")
        self.graphene_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color)
        self.graphene_button.grid(row=3,column=1, padx=5, pady=0, sticky="w")

        self.biocap_label = customtkinter.CTkLabel(self,justify="left", text="10 Biocapacitors\nCAP x nb KWH\nPrice :")
        self.biocap_label.grid(row=4,column=0, padx=10,pady=10,sticky="w")
        self.biocap_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color)
        self.biocap_button.grid(row=4,column=1, padx=5, pady=0, sticky="w")

        self.magneticCont_label = customtkinter.CTkLabel(self,justify="left", text="10 Magnetic containers\nCAP x nb KWH\nPrice :")
        self.magneticCont_label.grid(row=5,column=0, padx=10,pady=10,sticky="w")
        self.magneticCont_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color)
        self.magneticCont_button.grid(row=5,column=1, padx=5, pady=0, sticky="w")

        self.quantumCore_label = customtkinter.CTkLabel(self,justify="left", text="10 Quantum cores\nCAP x nb KWH\nPrice :")
        self.quantumCore_label.grid(row=6,column=0, padx=10,pady=10,sticky="w")
        self.quantumCore_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color)
        self.quantumCore_button.grid(row=6,column=1, padx=5, pady=0, sticky="w")

        self.cosmicCryst_label = customtkinter.CTkLabel(self,justify="left", text="10 Cosmic crystals\nCAP x nb KWH\nPrice :")
        self.cosmicCryst_label.grid(row=7,column=0, padx=10,pady=10,sticky="w")
        self.cosmicCryst_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color)
        self.cosmicCryst_button.grid(row=7,column=1, padx=5, pady=0, sticky="w")

        self.antimatChamber_label = customtkinter.CTkLabel(self,justify="left", text="10 Antimatter chamber\nCAP x nb KWH\nPrice :")
        self.antimatChamber_label.grid(row=8,column=0, padx=10,pady=10,sticky="w")
        self.antimatChamber_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color)
        self.antimatChamber_button.grid(row=8,column=1, padx=5, pady=0, sticky="w")

class InvestFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._bg_color=colors.background_color
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        # Number of each investment
        self.nSinge = 0
        self.nMoulin = 0
        self.nChampignon = 0
        self.nSolaire = 0
        self.nBiomasse = 0
        self.nNucleaire = 0
        self.nFusion = 0
        self.nDyson = 0
        self.nGalaxy = 0
        self.nDimension = 0
        self.nGrandmere = 0

        # add widgets onto the frame
        self.invest_label = customtkinter.CTkLabel(self, text="Investments :", font=("Arial", 16))
        self.invest_label.grid(row=0,column=0, padx=10, pady=15, sticky="w")

        self.monkey_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nSinge} Monkey on a bike\nPrice : --")
        self.monkey_label.grid(row=1,column=0, padx=10,pady=8,sticky="w")
        self.monkey_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_singe)
        self.monkey_button.grid(row=1,column=1, padx=5, pady=0, sticky="w")

        self.windmill_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nFusion} Windmill \nPrice : --")
        self.windmill_label.grid(row=2,column=0, padx=10,pady=8,sticky="w")
        self.windmill_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_moulin)
        self.windmill_button.grid(row=2,column=1, padx=5, pady=0, sticky="w")

        self.mushroom_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nBiomasse} Bioluminescent Mushroom\nPrice : --")
        self.mushroom_label.grid(row=3,column=0, padx=10,pady=8,sticky="w")
        self.mushroom_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_champignon)
        self.mushroom_button.grid(row=3,column=1, padx=5, pady=0, sticky="w")

        self.solar_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nSolaire} Solar Panel\nPrice : --")
        self.solar_label.grid(row=4,column=0, padx=10,pady=8,sticky="w")
        self.solar_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_solaire)   
        self.solar_button.grid(row=4,column=1, padx=5, pady=0, sticky="w")
        
        self.biomass_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nBiomasse} Biomass farm\nPrice : --")
        self.biomass_label.grid(row=5,column=0, padx=10,pady=8,sticky="w")
        self.biomass_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_biomasse)
        self.biomass_button.grid(row=5,column=1, padx=5, pady=0, sticky="w")

        self.nuclear_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nNucleaire} Nuclear plant\nPrice : --")
        self.nuclear_label.grid(row=6,column=0, padx=10,pady=8,sticky="w")
        self.nuclear_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_nucleaire)
        self.nuclear_button.grid(row=6,column=1, padx=5, pady=0, sticky="w")

        self.fusion_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nFusion} Fusion reactor\nPrice : --")
        self.fusion_label.grid(row=7,column=0, padx=10,pady=8,sticky="w")
        self.fusion_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_fusion)
        self.fusion_button.grid(row=7,column=1, padx=5, pady=0, sticky="w") 

        self.dyson_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nDyson} Dyson spehere\nPrice : --")
        self.dyson_label.grid(row=8,column=0, padx=10,pady=8,sticky="w")
        self.dyson_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_dyson)
        self.dyson_button.grid(row=8,column=1, padx=5, pady=0, sticky="w")

        self.galaxy_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nGalaxy} Galaxy harvester\nPrice : --")
        self.galaxy_label.grid(row=9,column=0, padx=10,pady=8,sticky="w")
        self.galaxy_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_galaxy)
        self.galaxy_button.grid(row=9,column=1, padx=5, pady=0, sticky="w")

        self.dimensional_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nDimension} Dimensional generator\nPrice : --")
        self.dimensional_label.grid(row=10,column=0, padx=10,pady=8,sticky="w")
        self.dimensional_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_dimension)
        self.dimensional_button.grid(row=10,column=1, padx=5, pady=0, sticky="w")

        self.grandma_label = customtkinter.CTkLabel(self,justify="left", text=f"{self.nGrandmere} Grandma's Love\nPrice : --")
        self.grandma_label.grid(row=11,column=0, padx=10,pady=8,sticky="w")
        self.grandma_button = customtkinter.CTkButton(self,text="Buy",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.add_grandmere)
        self.grandma_button.grid(row=11,column=1, padx=5, pady=0, sticky="w")

        self.minigame_button = customtkinter.CTkButton(self,text="Mini_game",text_color="black", fg_color=colors.lightButton_color,hover_color=colors.background_color, command=self.launch_minigame)
        self.minigame_button.grid(row=12,column=1, padx=5, pady=0, sticky="w")

    # Function to launch the minigame
    def launch_minigame(self):
        subprocess.Popen(["python3", "powerplant/classes/jeux_cable.py"])

    def add_singe(self):
        self.nSinge += 1

    def add_moulin(self):
        self.nMoulin += 1

    def add_champignon(self):
        self.nChampignon += 1

    def add_solaire(self):
        self.nSolaire += 1

    def add_biomasse(self):
        self.nBiomasse += 1

    def add_nucleaire(self):
        self.nNucleaire += 1

    def add_fusion(self):
        self.nFusion += 1

    def add_dyson(self):
        self.nDyson += 1

    def add_galaxy(self):
        self.nGalaxy += 1

    def add_dimension(self):
        self.nDimension += 1
    
    def add_grandmere(self):
        self.nGrandmere += 1

    def update_prod(self):
        self.monkey_label.configure(text=f"{self.nSinge} Monkeys on a bike\nPrice : --")
        self.windmill_label.configure(text=f"{self.nMoulin} Windmills\nPrice : --")
        self.mushroom_label.configure(text=f"{self.nChampignon} Bioluminescent Mushrooms\nPrice : --")
        self.solar_label.configure(text=f"{self.nSolaire} Solar Panels\nPrice : --")
        self.biomass_label.configure(text=f"{self.nBiomasse} Biomass farms\nPrice : --")
        self.nuclear_label.configure(text=f"{self.nNucleaire} Nuclear plants\nPrice : --")
        self.fusion_label.configure(text=f"{self.nFusion} Fusion reactors\nPrice : --")
        self.dyson_label.configure(text=f"{self.nDyson} Dyson speheres\nPrice : --")
        self.galaxy_label.configure(text=f"{self.nGalaxy} Galaxy harvesters\nPrice : --")
        self.dimensional_label.configure(text=f"{self.nDimension} Dimensional generators\nPrice : --")
        self.grandma_label.configure(text=f"{self.nGrandmere} Grandma's Love\nPrice : --")
 
 
class MarketingFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._bg_color=colors.background_color
 
        self.selling_price = 0.2 # Prix de base
        self.demand = 0
        self.gainpers = 0
 
        # add widgets onto the frame
        self.marketing_label = customtkinter.CTkLabel(self, text="Marketing :", font=("Arial", 16))
        self.marketing_label.grid(row=0,column=0, padx=10, pady=15, sticky="w")
 
        self.price_label = customtkinter.CTkLabel(self, text="0.20 fr")
        self.price_label.grid(row=1,column=0,padx=5,pady=5)
 
        self.increasePrice_button = customtkinter.CTkButton(
            master=self,
            text="+",
            command=self.increase_price,
            corner_radius=10,  # Set the corner radius to half the height for a circular shape
            width=20,  # Make the button square for a true circle
            height=20,
            fg_color=colors.lightButton_color,  # Set the button color
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
            fg_color=colors.lightButton_color,  # Set the button color
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
        self.geometry("850x850")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
 
        self.my_frame = MainFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
 
    def update_game(self):
        self.my_frame.marketing_frame.update_pstk()
        self.my_frame.price_frame.update_mk()
        self.my_frame.invest_frame.update_prod()