class Venta:
    def __init__(self):
        self.ventas = []
        self.tipos = {}
        self.total = 0
        self.total_tipo_a = 0
        self.total_tipo_b = 0
        self.total_tipo_c = 0
        pedidos = True
        print("-------------------------")
        print(f"Bienvenido a tu tienda.!")
        print("-------------------------\n")
        while pedidos:
            self.registrar_venta()
            otro_pedido = input("desea agregar otro pedido? SI/NO \n")
            if otro_pedido == "SI":
                pedidos
            else:
                pedidos = False
                print("----------------------------")
                print(f"hoy hiciste {len(self.ventas)} ventas")
                print("----------------------------\n")
                # print(f"{self.tipos}")
                # print(f"el tipo de pantalon mas vendido fue: ")
                print(f"cantidad vendida por cada pantalon: ")
                print("----------------------------")
                print(f"Pantalon Tipo A: ${self.total_tipo_a}")
                print(f"Pantalon Tipo B: ${self.total_tipo_b}")
                print(f"Pantalon Tipo C: ${self.total_tipo_c}")
                print("----------------------------\n")
                print(f"total vendido:  ${self.total}")
                print("----------------------------\n")

        

    def obtener_datos_venta(self):
        tipo = input("que tipo de pantalon vendiste: ")
        if self.validar_tipo(tipo):
            self.obtener_cantidad
            return tipo
        else:
            return self.registrar_venta()

    def obtener_cantidad(self):
        cantidad = input("cuantos pantalones de este modelo vendiste: ")
        if self.validar_cantidad(cantidad):
            return cantidad
        else:
            return self.obtener_cantidad()

    def validar_tipo(self, tipo):
        if tipo == 'A' or tipo == 'B' or tipo == 'C':
            return True
        else:
            print("Por favor ingrese un tipo valido (tipo A, tipo B, tipo C)\n")
            return False

    def validar_cantidad(self, cantidad):
        try:
            numero = int(cantidad)
        except ValueError:
            print("Por favor ingrese un valor numerico\n")
            return False
        if numero <= 0:
            print("Por favor ingrese un numero positivo\n")
            return False
        else:
            return True


