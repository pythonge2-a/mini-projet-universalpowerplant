import customtkinter as ctk
import math

class Dynamo:
    # Initialisation de la puissance de sortie du dynamo
    def __init__(self, power_output):
        self.power_output = power_output

    # Retourne la puissance de sortie actuelle du dynamo
    def generate_power(self):
        return self.power_output

class App:
    def __init__(self, root):
        self.root = root

        # Configuration de la fenêtre principale
        self.root.title("Dynamo Game")
        self.root.geometry("500x500")

        # Création d'une instance de Dynamo avec une puissance initiale de 0
        self.dynamo = Dynamo(0)

        # Initialisation de la variable tours
        self.tours = 0

        # Initialisation du temps imparti (en secondes)
        self.time_left = 15

        # Création d'un label pour afficher le nombre de tours
        self.tours_label = ctk.CTkLabel(self.root, text=f"Tours: {self.tours}", font=("Helvetica", 24))
        self.tours_label.pack(pady=20)

        # Création d'un label pour afficher le temps restant
        self.time_label = ctk.CTkLabel(self.root, text=f"Time left: {self.time_left}s", font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        # Création d'un canvas pour dessiner les cercles et la ligne
        self.canvas = ctk.CTkCanvas(self.root, width=400, height=400)
        self.canvas.pack()

        # Initialisation des variables pour les cercles et l'animation
        self.outer_circle_radius = 150
        self.inner_circle_radius = 20
        self.angle = 0

        # Création du cercle extérieur
        self.outer_circle = self.canvas.create_oval(100, 100, 300, 300, outline="black")
        # Création de la ligne reliant le centre du cercle extérieur au cercle intérieur
        self.line = self.canvas.create_line(200, 200, 200, 200, fill="blue", width=5)
        # Création du cercle intérieur
        self.inner_circle = self.canvas.create_oval(250, 180, 290, 220, fill="red")

        # Met à jour la position initiale de la ligne et du cercle intérieur
        self.update_circle_and_line()

        # Liaison de l'événement de clic sur le canvas avec la méthode on_outer_circle_click
        self.canvas.bind("<Button-1>", self.on_outer_circle_click)

        # Démarrage du minuteur
        self.update_timer()

    def on_outer_circle_click(self, event):
        if self.time_left > 0:
            # Vérifie si le clic est à l'intérieur du cercle extérieur
            if self.is_inside_circle(event.x, event.y, 200, 200, self.outer_circle_radius):
                # Incrémente l'angle de 45 degrés
                self.angle += 45
                if self.angle >= 360:
                    self.angle -= 360
                    self.tours += 1
                    self.update_tours_label()

                # Met à jour la position de la ligne et du cercle intérieur
                self.update_circle_and_line()

    def is_inside_circle(self, x, y, circle_x, circle_y, radius):
        # Vérifie si un point (x, y) est à l'intérieur d'un cercle de centre (circle_x, circle_y) et de rayon radius
        return (x - circle_x) ** 2 + (y - circle_y) ** 2 <= radius ** 2

    def update_circle_and_line(self):
        # Calcule les nouvelles coordonnées du cercle intérieur
        x = 200 + self.outer_circle_radius * math.cos(math.radians(self.angle))
        y = 200 + self.outer_circle_radius * math.sin(math.radians(self.angle))

        # Met à jour les coordonnées du cercle intérieur et de la ligne
        self.canvas.coords(self.inner_circle, x - self.inner_circle_radius, y - self.inner_circle_radius, x + self.inner_circle_radius, y + self.inner_circle_radius)
        self.canvas.coords(self.line, 200, 200, x, y)

    def update_timer(self):
        if self.time_left > 0:
            # Décrémente le temps restant
            self.time_left -= 1
            # Met à jour l'affichage du temps restant
            self.time_label.configure(text=f"Time left: {self.time_left}s")
            # Appelle cette méthode à nouveau après 1 seconde
            self.root.after(1000, self.update_timer)
        else:
            # Termine le jeu lorsque le temps est écoulé
            self.end_game()

    def update_tours_label(self):
        # Met à jour l'affichage du nombre de tours
        self.tours_label.configure(text=f"Tours: {self.tours}")

    def end_game(self):
        # Efface tout sur l'écran
        self.canvas.delete("all")
        self.time_label.pack_forget()
        self.tours_label.pack_forget()

        # Affiche le nombre de tours en grand une fois le temps écoulé
        final_tours_label = ctk.CTkLabel(self.root, text=f"Final Tours: {self.tours}", font=("Helvetica", 36))
        final_tours_label.pack(pady=20)

if __name__ == "__main__":
    # Lancer le jeu
    root = ctk.CTk()
    game = App(root)
    root.mainloop()