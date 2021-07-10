import venta

class Tienda(venta.Venta):
    def __init__(self):
        super().__init__()


    def agregar_venta(self, venta):
        self.ventas.append(venta)
        



    def registrar_venta(self):
        
        venta__para_agregar = self.obtener_datos_venta()
        cantidad = int(self.obtener_cantidad())

        if venta__para_agregar == 'A':
            self.ventas.append(venta__para_agregar)
            print(f"total pedido ${30 * cantidad}")
            self.total_tipo_a = self.total_tipo_a + (30 * cantidad)
            self.total = self.total + (30 * cantidad)
            print(f"has hecho {len(self.ventas)} ventas")
        elif venta__para_agregar == 'B':
            self.ventas.append(venta__para_agregar)
            print(f"total pedido ${20 * cantidad}")
            self.total_tipo_b = self.total_tipo_b + (20 * cantidad)
            self.total = self.total + (20 * cantidad)
            print(f"has hecho {len(self.ventas)} ventas")
        else:
            self.ventas.append(venta__para_agregar)
            print(f"total pedido ${10 * cantidad}")
            self.total_tipo_c = self.total_tipo_c + (10 * cantidad)
            self.total = self.total + (10 * cantidad)
            print(f"has hecho {len(self.ventas)} ventas")




