import customtkinter as ctk
import math

class Dynamo:
    # Initialisation de la puissance de sortie du dynamo
    def __init__(self, power_output):
        self.power_output = power_output

    # Retourne la puissance de sortie actuelle du dynamo
    def generate_power(self):
        return self.power_output

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Dynamo")
        self.geometry("500x500")

        # Création d'une instance de Dynamo avec une puissance initiale de 0
        self.dynamo = Dynamo(0)

        # Création d'un label pour afficher la puissance de sortie du dynamo
        self.label = ctk.CTkLabel(self, text=f"Dynamo Power Output: {self.dynamo.generate_power()}")
        self.label.pack(pady=20)

        # Création d'un canvas pour dessiner les cercles et la ligne
        self.canvas = ctk.CTkCanvas(self, width=400, height=400)
        self.canvas.pack()

        # Initialisation des variables pour les cercles et l'animation
        self.outer_circle_radius = 150
        self.inner_circle_radius = 20
        self.angle = 0
        self.speed = 0  # Variable pour contrôler la vitesse initiale

        # Liste des paliers de vitesse
        self.speed_levels = [0, 1, 2, 3, 4, 5]
        self.speed_thresholds = [5, 10, 20, 35, 55, 80, 110, 145, 185, 230]  # Paliers progressifs
        self.current_speed_index = 0
        self.tours = 0  # Variable pour suivre le nombre de tours

        # Création du cercle extérieur
        self.outer_circle = self.canvas.create_oval(100, 100, 300, 300, outline="black")
        # Création de la ligne reliant le centre du cercle extérieur au cercle intérieur
        self.line = self.canvas.create_line(200, 200, 200, 200, fill="blue", width=5)
        # Création du cercle intérieur
        self.inner_circle = self.canvas.create_oval(250, 180, 290, 220, fill="red")

        # Liaison de l'événement de clic sur le canvas avec la méthode on_outer_circle_click
        self.canvas.bind("<Button-1>", self.on_outer_circle_click)

        # Création d'un bouton pour afficher et appliquer les améliorations de vitesse
        self.upgrade_button = ctk.CTkButton(self, text=f"Upgrade Speed (Next at {self.get_next_threshold()} tours)", state="disabled", command=self.upgrade_speed)
        self.upgrade_button.pack(pady=20)

        # Démarrage de l'animation
        self.update_animation()

    def on_outer_circle_click(self, event):
        # Vérifie si le clic est à l'intérieur du cercle extérieur
        if self.is_inside_circle(event.x, event.y, 200, 200, self.outer_circle_radius):
            # Incrémente l'angle de 10 degrés
            self.angle += 360

    def is_inside_circle(self, x, y, circle_x, circle_y, radius):
        # Vérifie si un point (x, y) est à l'intérieur d'un cercle de centre (circle_x, circle_y) et de rayon radius
        return (x - circle_x) ** 2 + (y - circle_y) ** 2 <= radius ** 2

    def update_animation(self):
        # Incrémente l'angle en utilisant la variable de vitesse
        self.angle += self.speed
        if self.angle >= 360:
            # Réinitialise l'angle et augmente la puissance de sortie du dynamo
            self.angle = 0
            self.dynamo.power_output += 1
            self.tours += 1
            self.label.configure(text=f"Dynamo Power Output: {self.dynamo.generate_power()}")

            # Vérifie si le palier pour l'amélioration de la vitesse est atteint
            if self.tours >= self.get_next_threshold():
                self.upgrade_button.configure(state="normal")

        # Calcule les nouvelles coordonnées du cercle intérieur
        x = 200 + self.outer_circle_radius * math.cos(math.radians(self.angle))
        y = 200 + self.outer_circle_radius * math.sin(math.radians(self.angle))

        # Met à jour les coordonnées du cercle intérieur et de la ligne
        self.canvas.coords(self.inner_circle, x - self.inner_circle_radius, y - self.inner_circle_radius, x + self.inner_circle_radius, y + self.inner_circle_radius)
        self.canvas.coords(self.line, 200, 200, x, y)

        # Planifie la prochaine mise à jour de l'animation
        self.after(50, self.update_animation)

    def get_next_threshold(self):
        # Retourne le prochain palier de tours pour l'amélioration de la vitesse
        if self.current_speed_index < len(self.speed_thresholds):
            return self.speed_thresholds[self.current_speed_index]
        return float('inf')  # Aucun palier supplémentaire

    def upgrade_speed(self):
        # Améliore la vitesse si possible
        if self.current_speed_index < len(self.speed_levels) - 1:
            # Soustrait les tours nécessaires du nombre total de tours
            next_threshold = self.get_next_threshold()
            self.tours -= next_threshold
            self.current_speed_index += 1
            self.speed = self.speed_levels[self.current_speed_index]
            self.upgrade_button.configure(text=f"Upgrade Speed (Next at {self.get_next_threshold()} tours)", state="disabled")

if __name__ == "__main__":
    # Crée et lance l'application
    app = App()
    app.mainloop()
    
    # Faudra faire en sorte que 
    # le nombre de tour est correctement afficher