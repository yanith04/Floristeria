import numpy as np
import matplotlib.pyplot as plt

class CorazonSangrante:
    def __init__(self):
        self.numero_de_petalos = 4
    def petalo(self, t):
        x = 16 * np.sin(t)**3
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        return x, y
    def gota(self, t):
        x = 2.2 * np.sin(t)
        y = 6.5 * np.cos(t) - 1
        return x, y
    def dibujar_flor(self):
        t = np.linspace(0, 4 * np.pi, 1000)
        plt.figure(figsize=(6, 6))
        x, y = self.petalo(t)
        plt.fill(x, y, color="deeppink")

        plt.fill([-2, -4, -2], [0, -5, -10], color='deeppink')
        plt.fill([2, 4, 2], [0, -5, -10], color='deeppink')
        plt.fill([-16, -11.5, -1], [-15, -11, -13.5], color='deeppink')
        plt.fill([16, 11.5, 1], [-15, -11, -13.5], color='deeppink')

        t_gota = np.linspace(600, np.pi, 600)
        x_gota, y_gota = self.gota(t_gota)
        plt.fill(x_gota, y_gota - 15, color='pink')
#triangulo
        plt.fill([-2, 2, 0], [-13, -13, 0], color='pink')

        plt.plot([0, 0], [18, 5], color='green', lw=5)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.text(0, -30, "ACA ESTA TU CORAZÓN SANGRANTE", ha='center', fontsize=12, color='black')

        plt.show()