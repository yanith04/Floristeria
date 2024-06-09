import numpy as np
import matplotlib.pyplot as plt

class Margarita:
    def __init__(self):
        self.numero_de_petalos = 6
        self.factor = 2

    def petalo(self, t, n, d):
        r = np.sin(n * t + np.pi / d)
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y

    def dibujar_flor(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        plt.figure(figsize=(6, 6))

        for i in range(self.numero_de_petalos):
            x, y = self.petalo(t, self.numero_de_petalos, self.factor)
            plt.plot(x, y, color="black")
        
        plt.scatter(0, 0, color='yellow', s=3500)  
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.text(0, -1.2, "ACA ESTA TU MARGARITA", ha='center', fontsize=12, color='black')

        plt.show()
flor = Margarita()
flor.dibujar_flor()