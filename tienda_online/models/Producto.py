# Creamos la clase padre Producto
import uuid


class Producto:
    def __init__(self, nombre, precio, stock, id_producto=None):
        # id único generado automáticamente si no se proporciona
        self.id = id_producto or str(uuid.uuid4())
        self.nombre = nombre
        self.precio = precio
        self.stock = float(stock)

    def tiene_stock(self, cantidad):
        """Devuelve True si hay al menos `cantidad` unidades en stock."""
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad):
        """Aumenta (cantidad>0) o disminuye (cantidad<0) el stock. Imprime ValueError si queda negativo."""
        nuevo = self.stock + cantidad
        if nuevo < 0:
            raise ValueError("Stock insuficiente para la operación")
        self.stock = nuevo
        return self.stock

    def __str__(self):
        return f"Producto (id={self.id}): {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"

# Subclase para productos electrónicos
class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses, id_producto=None):
        super().__init__(nombre, precio, stock, id_producto=id_producto)
        self.garantia_meses = garantia_meses

    def __str__(self):
        return (f"Producto Electrónico: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}, "
                f"Garantía: {self.garantia_meses} meses")

# Subclase para productos de ropa
class ProductoRopa(Producto):
    def __init__(self, nombre, precio, stock, talla, color, id_producto=None):
        super().__init__(nombre, precio, stock, id_producto=id_producto)
        self.talla = talla
        self.color = color

    def __str__(self):
        return (f"Producto Ropa: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}, "
                f"Talla: {self.talla}, Color: {self.color}")
    