import customtkinter as ctk
import random

class SimonGame(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Simon Game")
        self.geometry("600x600")

        # Initialisation des variables
        self.sequence = []
        self.user_sequence = []
        self.score = 0
        self.time_left = 30
        self.colors = ["red", "blue", "green"]
        self.buttons = {}
        self.sequence_speed = 1000  # Temps initial d'affichage de chaque couleur en ms

        # Création d'un canvas pour dessiner les cercles et les séquences
        self.canvas = ctk.CTkCanvas(self, width=600, height=400)
        self.canvas.pack()

        # Création d'un rectangle pour afficher la séquence
        self.sequence_display = self.canvas.create_rectangle(150, 50, 450, 150, outline="black", width=2, fill="white", tags="sequence_display")

        # Création des boutons de couleur en forme de cercle
        self.create_color_buttons()

        # Création d'un label pour afficher le score
        self.score_label = ctk.CTkLabel(self, text=f"Score: {self.score}", font=("Helvetica", 24))
        self.score_label.pack(pady=20)

        # Création d'un label pour afficher le temps restant
        self.time_label = ctk.CTkLabel(self, text=f"Time left: {self.time_left}s", font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        # Création d'un bouton START pour démarrer le jeu
        self.start_button = ctk.CTkButton(self, text="START", command=self.start_game, font=("Helvetica", 36))
        self.start_button.pack(pady=200)

        # Cache les éléments de jeu au démarrage
        self.canvas.pack_forget()
        self.score_label.pack_forget()
        self.time_label.pack_forget()

    def create_color_buttons(self):
        # Création des boutons de couleur en forme de cercle
        button_radius = 50
        button_spacing = 150
        for i, color in enumerate(self.colors):
            x = 150 + i * button_spacing
            y = 300
            button = self.canvas.create_oval(x - button_radius, y - button_radius, x + button_radius, y + button_radius, fill=color, outline=color, tags=color)
            self.buttons[color] = button
            self.canvas.tag_bind(color, "<Button-1>", lambda event, c=color: self.user_input(c))

    def start_game(self):
        # Cache le bouton START
        self.start_button.pack_forget()
        # Affiche les éléments de jeu
        self.canvas.pack()
        self.score_label.pack(pady=20)
        self.time_label.pack(pady=20)
        # Démarrage du minuteur
        self.update_timer()
        # Démarrage de la première séquence
        self.next_sequence()

    def generate_sequence(self):
        # Génère une nouvelle séquence de 3 couleurs
        self.sequence = [random.choice(self.colors) for _ in range(3)]

    def next_sequence(self):
        # Génère et affiche une nouvelle séquence
        self.generate_sequence()
        self.user_sequence = []
        self.show_sequence(0)

    def show_sequence(self, index):
        if index < len(self.sequence):
            self.disable_buttons()
            self.canvas.delete("sequence")
            color = self.sequence[index]
            self.canvas.create_oval(275, 75, 325, 125, fill=color, outline=color, tags="sequence")
            self.after(500, lambda: self.canvas.delete("sequence"))
            self.after(1000, lambda: self.show_sequence(index + 1))
        else:
            self.enable_buttons()

    def flash_button(self, color):
        # Fait clignoter un bouton de couleur
        self.canvas.itemconfig(self.buttons[color], fill="white")
        self.after(200, lambda: self.canvas.itemconfig(self.buttons[color], fill=color))

    def enable_buttons(self):
        # Active les boutons pour permettre à l'utilisateur de reproduire la séquence
        for color in self.colors:
            self.canvas.itemconfig(self.buttons[color], state="normal")

    def disable_buttons(self):
        # Désactive les boutons
        for color in self.colors:
            self.canvas.itemconfig(self.buttons[color], state="disabled")

    def user_input(self, color):
        # Gère l'entrée de l'utilisateur
        self.user_sequence.append(color)
        self.flash_button(color)
        if self.user_sequence == self.sequence[:len(self.user_sequence)]:
            if len(self.user_sequence) == len(self.sequence):
                self.score += 1
                self.update_score_label()
                self.disable_buttons()
                self.show_feedback("correct")
                self.after(1000, self.next_sequence)
        else:
            self.show_feedback("incorrect")

    def show_feedback(self, result):
        # Affiche une coche verte pour une séquence correcte ou une croix rouge pour une séquence incorrecte
        self.canvas.delete("feedback")
        if result == "correct":
            self.canvas.create_text(300, 100, text="✔", font=("Helvetica", 48), fill="lightgreen", tags="feedback")
            self.after(1000, self.canvas.delete, "feedback")
        else:
            self.canvas.create_text(300, 100, text="✘", font=("Helvetica", 48), fill="red", tags="feedback")
            self.after(1000, self.canvas.delete, "feedback")
            self.after(1000, self.show_sequence_again)

    def show_sequence_again(self):
        # Affiche à nouveau la séquence après une mauvaise séquence
        self.user_sequence = []
        self.show_sequence(0)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.configure(text=f"Time left: {self.time_left}s")
            self.after(1000, self.update_timer)
        else:
            self.end_game()

    def update_score_label(self):
        # Met à jour l'affichage du score
        self.score_label.configure(text=f"Score: {self.score}")

    def end_game(self):
        # Efface tout sur l'écran
        self.canvas.delete("all")
        self.time_label.pack_forget()
        self.score_label.pack_forget()

        # Affiche le score final en grand
        final_score_label = ctk.CTkLabel(self, text=f"Final Score: {self.score}", font=("Helvetica", 36))
        final_score_label.pack(pady=20)

if __name__ == "__main__":
    # Crée et lance l'application
    app = SimonGame()
    app.mainloop()