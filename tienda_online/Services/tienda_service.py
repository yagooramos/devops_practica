# Servicio centralizado para la gestión de la tienda
from models.Usuario import Usuario, Cliente, Administrador
from models.Producto import Producto
from models.Pedido import Pedido
from datetime import datetime

class TiendaService:
	def __init__(self):
		self.usuarios = {}  # id_unico: Usuario
		self.productos = {}  # id_producto: Producto
		self.pedidos = []  # lista de objetos Pedido

	def registrar_usuario(self, id_unico, nombre, correo, tipo, direccion_postal=None):
		if id_unico in self.usuarios:
			raise ValueError("El usuario ya existe")
		if tipo == 'cliente':
			usuario = Cliente(id_unico, nombre, correo, direccion_postal)
		elif tipo == 'administrador':
			usuario = Administrador(id_unico, nombre, correo)
		else:
			raise ValueError("Tipo de usuario no válido")
		self.usuarios[id_unico] = usuario
		return usuario

	def añadir_producto(self, producto):
		if producto.id in self.productos:
			raise ValueError("El producto ya existe")
		self.productos[producto.id] = producto
		return producto

	def eliminar_producto(self, nombre_producto):
		# eliminar por id
		if nombre_producto not in self.productos:
			raise ValueError("Producto no encontrado")
		del self.productos[nombre_producto]

	def listar_productos(self):
		return list(self.productos.values())

	def realizar_pedido(self, id_usuario, productos_cantidades):
		# productos_cantidades: lista de tuplas (id_producto, cantidad)
		if id_usuario not in self.usuarios:
			raise ValueError("Usuario no encontrado")
		usuario = self.usuarios[id_usuario]
		if not isinstance(usuario, Cliente):
			raise ValueError("Solo los clientes pueden realizar pedidos")
		productos_obj_cant = []
		# Verificar stock
		for id_producto, cantidad in productos_cantidades:
			if id_producto not in self.productos:
				raise ValueError(f"Producto '{id_producto}' no existe")
			producto = self.productos[id_producto]
			if not producto.tiene_stock(cantidad):
				raise ValueError(f"No hay suficiente stock de '{producto.nombre}'")
			productos_obj_cant.append((producto, cantidad))
		# Descontar stock
		for producto, cantidad in productos_obj_cant:
			producto.actualizar_stock(-cantidad)
		# Crear pedido
		pedido = Pedido(usuario, productos_obj_cant)
		self.pedidos.append(pedido)
		return pedido

	def listar_pedidos_usuario(self, id_usuario):
		pedidos_usuario = [p for p in self.pedidos if p.cliente.id_unico == id_usuario]
		pedidos_usuario.sort(key=lambda p: p.fecha_pedido)
		return pedidos_usuario
