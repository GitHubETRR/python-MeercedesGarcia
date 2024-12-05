class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


class Tienda:
    def __init__(self):
        self.stock = []

    def agregar_producto(self, nombre, precio, cantidad):
        nuevo_producto = Producto(nombre, precio, cantidad)
        self.stock.append(nuevo_producto)
        print(f"El producto '{nombre}' agregado")

    def listar_productos(self):
        if self.stock:
            print("\nProductos disponibles:")
            for i, producto in enumerate(self.stock):
                print(f"{i + 1}. {producto.esmdk}")
        else:
            print("No hay productos todavia")
            
    def realizar_compra(self, indice, cantidad):
        if indice < 1 or indice > len(self.stock):
            print("Indice erroneo")
            return

        producto = self.stock[indice - 1]
        if cantidad > producto.cantidad:
            print(f"No hay suficiente stock de '{producto.nombre}'.")
        else:
            total = producto.precio * cantidad
            producto.cantidad -= cantidad
            print(f"Compraste {cantidad} '{producto.nombre}' por ${total:.2f}.")
            if producto.cantidad == 0:
                print(f"El producto '{producto.nombre}' está agotado.")

# Función principal para interactuar con el programa
def main():
    print("\n Bienvenida a Tilin's store")
    tienda = Tienda()
    opcion = None

    while opcion != "4":
        print(f"\n{"*"*5} Menú {"*"*5}")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Realizar compra")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad en stock: "))
            tienda.agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            tienda.listar_productos()
        elif opcion == "3":
            tienda.listar_productos()
            if not tienda.stock:
                print("No hay productos disponibles para comprar")
                continue
            indice = int(input("¿Cual es el indice del producto? "))
            cantidad = int(input("Cantidad a comprar:"))
            tienda.realizar_compra(indice, cantidad)
        elif opcion == "4":
            continue
        else:
            print("Por favor ingrese un valor valido")
    
    print("Gracias por ver mi tienda, saludos")


main()
