class Torta:
    def __init__(self, sabor):
        self.sabor = sabor
    
    def bañar(self, sabor):
        self.bañado = sabor
    
    def colorante(self, color):
        self.color = color

    def mostrar_torta(self):
        print(f"La torta es de sabor {self.sabor}, con una cobertura de {self.bañado} de color {self.color}")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


def saludar(nombre, edad):
    print(f'Hola {nombre} tenés {edad} años')


bebitita = Persona(nombre="Mechi", edad=17)
saludar(bebitita.nombre, bebitita.edad)


tortita = Torta("Crema")
tortita.bañar("Leche")
tortita.colorante("Rosa")

tortita.mostrar_torta()


lista = [3, 2, 5, 6]


'''
suma = 0
for elemento in lista:
    suma += elemento

lista = [3, 2, 5, 6]
'''

promedio = sum(lista) / len(lista)
print(promedio)

