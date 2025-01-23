# Mis en commentaire car je peux pas vérifier si cela fonctionne

# import pickle
# from powerplant.classes.interface import MainFrame, PriceFrame, StockFrame, InvestFrame, MarketingFrame
# from powerplant.classes.production import Production, AnotherProductionClass

# class SaveManager:
#     def __init__(self, interface_objects, production_objects, save_file: str = "game_save.pkl"):
#         """
#         Initialise le gestionnaire de sauvegarde avec les instances des objets d'interface et de production,
#         ainsi que le nom du fichier de sauvegarde.
#         """
#         self.interface_objects = interface_objects
#         self.production_objects = production_objects
#         self.save_file = save_file

#     def save_game(self):
#         """
#         Sauvegarde l'état actuel des objets d'interface et de production dans un fichier en utilisant pickle.
#         """
#         with open(self.save_file, 'wb') as file:
#             # Utilise pickle pour sérialiser les objets d'interface et de production et les écrire dans le fichier
#             pickle.dump({
#                 'interface_objects': self.interface_objects,
#                 'production_objects': self.production_objects
#             }, file)
#         print("Game saved successfully.")

#     def load_game(self):
#         """
#         Charge l'état sauvegardé des objets d'interface et de production à partir du fichier en utilisant pickle.
#         """
#         try:
#             with open(self.save_file, 'rb') as file:
#                 # Utilise pickle pour désérialiser les objets à partir du fichier
#                 data = pickle.load(file)
#                 self.interface_objects = data['interface_objects']
#                 self.production_objects = data['production_objects']
#             print("Game loaded successfully.")
#         except FileNotFoundError:
#             # Gère le cas où le fichier de sauvegarde n'existe pas
#             print("Save file not found.")