
import uuid
from datetime import datetime
from models.Usuario import Cliente
from models.Producto import Producto

class Pedido:
	def __init__(self, cliente, productos_cantidades, fecha_pedido=None, id_pedido=None):
		
		if not isinstance(cliente, Cliente):
			raise ValueError("El cliente debe ser una instancia de Cliente")
		self.cliente = cliente
		self.productos_cantidades = productos_cantidades  # [(Producto, cantidad), ...]
		self.fecha_pedido = fecha_pedido or datetime.now()
		self.id_pedido = id_pedido or str(uuid.uuid4())

	def calcular_total(self):
		total = 0
		for producto, cantidad in self.productos_cantidades:
			total += producto.precio * cantidad
		return total

	def __str__(self):
		resumen = f"Pedido ID: {self.id_pedido}\n"
		# Muestra la fecha del pedido en formato año-mes-día hora:minuto:segundoresumen += f"Cliente: {self.cliente.nombre}\n"
		resumen += "Productos:\n"
		for producto, cantidad in self.productos_cantidades:
			resumen += f"  - {producto.nombre} x {cantidad} = ${producto.precio * cantidad:.2f}\n"
		resumen += f"Total: ${self.calcular_total():.2f}"
		return resumen

