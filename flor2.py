import numpy as np
import matplotlib.pyplot as plt

class FlorDeCuruba:
    def __init__(self):
        self.numero_de_petalos = 10
        self.factor = 3

    def petalo(self, t, n, d):
        r = 3 * np.cos((7 / 2) * t) + 1
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y

    def dibujar_flor(self):
        t = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        plt.figure(figsize=(6, 6))

        for i in range(self.numero_de_petalos):
            x, y = self.petalo(t + i * np.pi / self.numero_de_petalos, self.numero_de_petalos, self.factor)
            plt.plot(x, y, color="violet")

        plt.scatter(0, 0, color='yellow', s=3000)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.text(0, -4.5, "Acá está tu flor de curuba", ha='center', fontsize=12, color='green')

        plt.show()
