import customtkinter
from . import *
 
class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
 
        # Configure the grid layout for the MainFrame
        self.grid_rowconfigure(0, weight=1)  # One row
        self.grid_columnconfigure((0, 1, 2), weight=1)  # Three columns
 
        # add widgets onto the frame
        self.price_frame = PriceFrame(master=self)
        self.price_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
 
        self.stock_frame = StockFrame(master=self)
        self.stock_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
 
        self.invest_frame = InvestFrame(master=self)
        self.invest_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
       
        self.marketing_frame = MarketingFrame(master=self)
        self.marketing_frame.grid(row=1, column=1)
 
class PriceFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
 
        self.kwh_stock = 0
        self.money = 0
 
        # add widgets onto the frame
        self.price_label = customtkinter.CTkLabel(self, text="fr -----",width=300,anchor="w")
        self.price_label.grid(row=0,column=0,padx=10,pady=15,sticky="w",)
 
        self.main_button = customtkinter.CTkButton(self, text="Generate energy",command=self.generate_kwh)
        self.main_button.grid(row=2,column=0,padx=10,pady=10)
 
       
        self.kwh_label = customtkinter.CTkLabel(self, text=" Unsold Stock : ///// kWh",width=300,anchor="w")
        self.kwh_label.grid(row=1,column=0,padx=10,pady=15,sticky="w")
 
   
    def set_kwh_stock(self, kwh):
        self.kwh_stock = kwh
        return self.kwh_stock
   
    def set_money(self, money):
        self.money = money
        return self.money
   
    def update_mk(self): #Mise à jour des paramètres de l'interface
        self.price_label.configure(text=f"Avaible Funds : {self.money:.4f} fr")
        self.kwh_label.configure(text=f"Unsold Stock : {self.kwh_stock:.4f} kWh")
 
    def generate_kwh(self):
        self.kwh_stock+=1
 
class StockFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
 
        # add widgets onto the frame
        self.stock_label = customtkinter.CTkLabel(self, text="Stockage :")
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
        self.nDyson = 0
        self.nMonkey = 0
        # add widgets onto the frame
        self.invest_label = customtkinter.CTkLabel(self, text="Investissements :")
        self.invest_label.grid(row=0,column=0, padx=10, pady=15, sticky="w")
   
        self.monkey_button = customtkinter.CTkButton(self,text="monkey on a bike")
        self.monkey_button.grid(row=1,column=0, padx=5, pady=5, sticky="w")
        self.monkeyCnt_label = customtkinter.CTkLabel(self, text="Monkeys")
        self.monkeyCnt_label.grid(row=1,column=1, padx=5,pady=2,sticky="w")
        self.monkeyCost_label =customtkinter.CTkLabel(self,text="Cost : --")
        self.monkeyCost_label.grid(row=2,column=0, padx=5,pady=2,sticky="w")
 
        self.dyson_button = customtkinter.CTkButton(self,text="dyson sphere")
        self.dyson_button.grid(row=1,column=3, padx=5, pady=5, sticky="w")
        self.dysonCnt_label = customtkinter.CTkLabel(self, text="Dyson Spheres")
        self.dysonCnt_label.grid(row=1,column=4, padx=5,pady=2,sticky="w")
        self.dysonCost_label =customtkinter.CTkLabel(self,text="Cost : --")
        self.dysonCost_label.grid(row=2,column=3, padx=5,pady=2,sticky="w")

    def update_prod(self):
        self.monkeyCnt_label.configure(text=f"{self.nMonkey} Monkeys")
        self.dysonCnt_label.configure(text=f"{self.nDyson} Dyson Spheres")
 
 
class MarketingFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
 
        self.selling_price = 0.2 # Prix de base
        self.stock_max = 0
 
        # add widgets onto the frame
        self.invest_label = customtkinter.CTkLabel(self, text="Marketing :")
        self.invest_label.grid(row=0,column=0, padx=10, pady=15, sticky="w")
 
        self.price_label = customtkinter.CTkLabel(self, text="1 fr")
        self.price_label.grid(row=1,column=0,padx=5,pady=5)
 
        self.increasePrice_button = customtkinter.CTkButton(
            master=self,
            text="+",
            command=self.increase_price,
            corner_radius=10,  # Set the corner radius to half the height for a circular shape
            width=20,  # Make the button square for a true circle
            height=20,
            fg_color="white",  # Set the button color
            text_color=colors.green  # Set the text color
        )
        self.increasePrice_button.grid(row=1,column=1)
        self.decreasePrice_button = customtkinter.CTkButton(
            master=self,
            text="-",
            command=self.decrease_price,
            corner_radius=10,  # Set the corner radius to half the height for a circular shape
            width=20,  # Make the button square for a true circle
            height=20,
            fg_color="white",  # Set the button color
            text_color=colors.red  # Set the text color
        )
        self.decreasePrice_button.grid(row=1,column=2)
 
        self.demand_label = customtkinter.CTkLabel(self, text="Demand -- %")
        self.demand_label.grid(row=2,column=0, sticky="w")
 
        self.gainpers_label = customtkinter.CTkLabel(self, text="Gain/s ---")
        self.gainpers_label.grid(row=2,column=0, sticky="w")
 
        self.stockMax_label = customtkinter.CTkLabel(self, text="Stock --- /max")
        self.stockMax_label.grid(row=2,column=0, sticky="w")
   
    def increase_price(self):
        self.selling_price += 0.01
        self.update_price_label()
 
    def decrease_price(self):
        if self.selling_price > 0.01:  # Empêche d'avoir un prix négatif
            self.selling_price -= 0.01
        self.update_price_label()
   
    def set_stock_max(self, stock):
        self.stock_max = stock
        return self.stock_max
   
    def update_pstk(self): #Mise à jour des paramètres de l'interface
        self.stockMax_label.configure(text=f"{self.stock_max} /max")
        self.price_label.configure(text=f"{self.selling_price:.2f} fr")

 
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
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
 
    def update_game(self):
        self.my_frame.marketing_frame.update_pstk()
        self.my_frame.price_frame.update_mk()
        self.my_frame.invest_frame.update_prod()