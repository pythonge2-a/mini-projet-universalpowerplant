import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fonction pour générer une courbe sinus
def generate_sinus(amplitude, frequency, x_values):
    return amplitude * np.sin(2 * np.pi * frequency * x_values)

# Classe principale du jeu
class SinusMatchingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Correspondance de Sinus")
        
        # Configuration principale de la fenêtre
        self.frame = ctk.CTkFrame(root)
        self.frame.pack(pady=50, padx=50, fill="both", expand=True)

        # Génération de la courbe cible
        self.x_values = np.linspace(0, 1, 500)
        # Liste des valeurs possibles
        self.possible_amplitudes = [0.5, 1.0, 1.5,2.0]
        self.possible_frequencies = [1.0,1.5,2.0,2.5,3.0]

        # Générer les valeurs restreintes
        self.target_amplitude = np.random.choice(self.possible_amplitudes)
        self.target_frequency = np.random.choice(self.possible_frequencies)
        self.target_y_values = generate_sinus(self.target_amplitude, self.target_frequency, self.x_values)

        # Initialisation des paramètres utilisateur
        self.user_amplitude = self.possible_amplitudes[0]
        self.user_frequency = self.possible_frequencies[0]
        self.user_y_values = generate_sinus(self.user_amplitude, self.user_frequency, self.x_values)

        # Création de la figure Matplotlib
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_title("Ajustez l'Amplitude et la Fréquence")
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(-2.5, 2.5)
        self.target_line, = self.ax.plot(self.x_values, self.target_y_values, label="Cible", color="blue")
        self.user_line, = self.ax.plot(self.x_values, self.user_y_values, label="Votre Sinus", color="red", linestyle="--")
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

       # Slider pour ajuster l'amplitude
        self.amplitude_slider = ctk.CTkSlider(
            self.frame, from_=0, to=len(self.possible_amplitudes) - 1,
            number_of_steps=len(self.possible_amplitudes) - 1,
            command=self.update_amplitude
        )
        self.amplitude_slider.pack(pady=10)
        self.amplitude_slider.set(0)

        # Label to show amplitude value
        self.amplitude_label = ctk.CTkLabel(self.frame, text=f"Amplitude: {self.user_amplitude}")
        self.amplitude_label.pack(pady=5)

        # Slider pour ajuster la fréquence
        self.frequency_slider = ctk.CTkSlider(
            self.frame, from_=0, to=len(self.possible_frequencies) - 1,
            number_of_steps=len(self.possible_frequencies) - 1,
            command=self.update_frequency
        )
        self.frequency_slider.pack(pady=10)
        self.frequency_slider.set(0)

        # Label to show frequency value
        self.frequency_label = ctk.CTkLabel(self.frame, text=f"Fréquence: {self.user_frequency}")
        self.frequency_label.pack(pady=5)

        # Bouton pour vérifier la correspondance
        self.check_button = ctk.CTkButton(self.frame, text="Vérifier", command=self.check_match)
        self.check_button.pack(pady=10)

        # Label pour afficher le résultat
        self.result_label = ctk.CTkLabel(self.frame, text="Ajustez les valeurs pour correspondre à la courbe cible.")
        self.result_label.pack(pady=10)

        # Gérer la fermeture proprement
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_amplitude(self, value):
        self.user_amplitude = value
        self.update_user_sinus()
        # Update amplitude label
        self.amplitude_label.configure(text=f"Amplitude: {self.user_amplitude:.1f}")

    def update_frequency(self, value):
        self.user_frequency = value
        self.update_user_sinus()
        # Update frequency label
        self.frequency_label.configure(text=f"Fréquence: {self.user_frequency:.1f}")

    def update_user_sinus(self):
        self.user_y_values = generate_sinus(self.user_amplitude, self.user_frequency, self.x_values)
        self.user_line.set_ydata(self.user_y_values)
        self.canvas.draw()

    def check_match(self):
        diff = np.sum(np.abs(self.target_y_values - self.user_y_values))
        if diff < 0.1:
            self.result_label.configure(text="Bravo ! Vous avez correspondu au sinus cible !", text_color="green")
        else:
            self.result_label.configure(text=f"Encore un peu... Différence: {diff:.2f}", text_color="red")

    def on_close(self):
        plt.close(self.fig)  # Fermer la figure Matplotlib
        self.root.destroy()

# Lancer le jeu
if __name__ == "__main__":
    root = ctk.CTk()
    game = SinusMatchingGame(root)
    root.mainloop()
