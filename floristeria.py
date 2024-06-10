from flor1 import Margarita
from flor2 import FlorDeCuruba
from flor3 import CorazonSangrante
from flor4 import RosaConTallo
from flor5 import Tulipan

class Floristeria:
    def __init__(self):
        self.flores = {
            "margarita": Margarita,
            "passiflora": FlorDeCuruba,
            "corazon sangrante": CorazonSangrante, 
            "rosa": RosaConTallo,
            "tulipan": Tulipan
        }

    def pedir_flor(self, nombre_flor):
        nombre_flor = nombre_flor.lower()
        if nombre_flor in self.flores:
            flor_clase = self.flores[nombre_flor]
            flor = flor_clase()
            flor.dibujar_flor()
        else:
            print("Lo siento, no tenemos esa flor disponible.")

    def mostrar_flores_disponibles(self):
        print("Flores disponibles:")
        for flor in self.flores:
            print(f"- {flor.capitalize()}")

    def elegir_flor(self):
        while True:
            self.mostrar_flores_disponibles()
            nombre_flor = input("Por favor, elija una flor de la lista anterior: ")
            if nombre_flor.lower() in self.flores:
                return nombre_flor.lower()
            else:
                print("Por favor, elija una flor válida de la lista.")


floristeria = Floristeria()
nombre_flor = floristeria.elegir_flor()
floristeria.pedir_flor(nombre_flor)
