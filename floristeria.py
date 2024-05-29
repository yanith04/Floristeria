from flor1 import Margarita

class Floristeria:
    def __init__(self):
        self.flores = {
            "margarita": Margarita
        }

    def pedir_flor(self, nombre_flor):
        nombre_flor = nombre_flor.lower()  
        if nombre_flor in self.flores:
           flor_clase = self.flores[nombre_flor]
           flor = flor_clase(6,2)
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
floristeria.mostrar_flores_disponibles()
nombre_flor = input("Por favor, elija una flor de la lista anterior: ")
floristeria.pedir_flor(nombre_flor)
