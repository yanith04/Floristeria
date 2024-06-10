import numpy as np
import matplotlib.pyplot as plt


class Tulipan:
    def __init__(self, numero_de_petalos=6):
        self.numero_de_petalos = numero_de_petalos

    def petalo(self, t, desplazamiento):
        x = 0.3 * np.sin(t + desplazamiento) * np.cos(t / 2)
        y = 0.6 * np.abs(np.cos(t + desplazamiento)) + 0.9
        return x, y

    def rotar_petalos(self, x, y, angulo):
        angulo = np.radians(angulo)
        x_rotado = x * np.cos(angulo) - y * np.sin(angulo)
        y_rotado = x * np.sin(angulo) + y * np.cos(angulo)
        return x_rotado, y_rotado

    def dibujar_flor(self):
        t = np.linspace(0, 2 * np.pi, 1000)
        plt.figure(figsize=(6, 8))

        colores = ["#FF69B4", "#FF1493", "#DB7093"]

        for i in range(self.numero_de_petalos):
            x, y = self.petalo(t, i * 2 * np.pi / self.numero_de_petalos)
            x, y = self.rotar_petalos(x, y, 180)
            plt.fill(x, y, color=colores[i % len(colores)], edgecolor='black')

        # Dibujar el tallo
        plt.plot([0, 0], [-1.5, -2.5], color='green', linewidth=5)

        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.text(0,
                 -2,
                 "ACA ESTA TU TULIPAN",
                 ha='center',
                 fontsize=12,
                 color='black')

        plt.show()


