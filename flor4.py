import numpy as np
import matplotlib.pyplot as plt

class RosaConTallo:
    def __init__(self):
        self.numero_de_petalos = 6
        self.factor = 1.5

    def petalo(self, t, n, d):
        r = 1 + np.cos(n * t) * d
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y

    def dibujar_flor(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        plt.figure(figsize=(6, 12))

        for i in range(self.numero_de_petalos):
            x, y = self.petalo(t + i * 2 * np.pi / self.numero_de_petalos, self.numero_de_petalos, self.factor)
            plt.plot(x, y + 6, color="red")

        plt.plot([0, 0], [0, 6], color='green', linewidth=4)

        # Dibujar las hojas
        hoja_t = np.linspace(0, 2 * np.pi, 1000)
        hoja_x = 0.5 * np.cos(hoja_t)
        hoja_y = 0.5 * np.sin(hoja_t)
        plt.plot(hoja_x - 0.5, hoja_y + 3, color='green')
        plt.plot(hoja_x + 0.5, hoja_y + 4, color='green')

        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.show()

rosa_con_tallo = RosaConTallo()
rosa_con_tallo.dibujar_flor()
