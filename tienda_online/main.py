# Punto de entrada para probar el sistema de la tienda
from Services import TiendaService
from models import Producto, ProductoElectronico, ProductoRopa

def main():
	tienda = TiendaService()

	# Paso 1: Registrar usuarios (3 clientes y 1 administrador)
	print('Registrar usuarios')
	clientes = [
		tienda.registrar_usuario('cli1', 'Ana García', 'ana@email.com', 'cliente', 'Calle 1, Ciudad'),
		tienda.registrar_usuario('cli2', 'Luis Pérez', 'luis@email.com', 'cliente', 'Calle 2, Ciudad'),
		tienda.registrar_usuario('cli3', 'Marta López', 'marta@email.com', 'cliente', 'Calle 3, Ciudad'),
	]
	admin = tienda.registrar_usuario('admin1', 'Admin User', 'admin@email.com', 'administrador')
	for u in clientes + [admin]:
		print(f"  - {u.id_unico}: {u.nombre} ({'admin' if u.is_admin() else 'cliente'})")

	# Paso 2: Crear y añadir 5 productos
	print('Crear y añadir 5 productos al inventario')
	productos = [
		ProductoElectronico('Portátil', 1200.0, 10, 24),
		ProductoElectronico('Auriculares', 150.0, 20, 12),
		ProductoRopa('Camiseta', 20.0, 50, 'M', 'Azul'),
		ProductoRopa('Pantalón', 35.0, 30, 'L', 'Negro'),
		Producto('Libro', 18.5, 40),
	]
	for prod in productos:
		tienda.añadir_producto(prod)
		print(f". - añadido: {prod.nombre} (id={prod.id})")

	# Paso 3: Listar productos para comprobar inventario
	print('Inventario actual')
	for prod in tienda.listar_productos():
		print(f"  - {prod}")

	# Preparar mapeo nombre->id para pedidos de demostración
	nombre_a_id = {p.nombre: p.id for p in tienda.listar_productos()}

	# Paso 4: Simular 3 pedidos hechos por distintos clientes
	print('Simular 3 pedidos de distintos clientes')
	pedidos = []
	try:
		p1 = tienda.realizar_pedido('cli1', [(nombre_a_id['Portátil'], 1), (nombre_a_id['Libro'], 2)])
		print(f"  - Pedido creado para cli1: {p1.id_pedido} (total ${p1.calcular_total():.2f})")
		pedidos.append(p1)
		p2 = tienda.realizar_pedido('cli2', [(nombre_a_id['Camiseta'], 3), (nombre_a_id['Auriculares'], 2)])
		print(f"  - Pedido creado para cli2: {p2.id_pedido} (total ${p2.calcular_total():.2f})")
		pedidos.append(p2)
		p3 = tienda.realizar_pedido('cli3', [(nombre_a_id['Pantalón'], 1), (nombre_a_id['Libro'], 1), (nombre_a_id['Camiseta'], 1)])
		print(f"  - Pedido creado para cli3: {p3.id_pedido} (total ${p3.calcular_total():.2f})")
		pedidos.append(p3)
	except Exception as e:
		print(f"Error al realizar pedido: {e}")

	# Paso 5: Comprobar histórico de pedidos de un cliente (cli1)
	print('Histórico de pedidos de Ana García (cli1)')
	historico = tienda.listar_pedidos_usuario('cli1')
	for pedido in historico:
		print('  - Resumen pedido:')
		print('    ' + str(pedido).replace('\n', '\n    '))
		print('    ' + '-' * 30)

	# Paso 6: Mostrar resumen del último pedido y stock actualizado
	print('Resumen del último pedido y stock actualizado')
	if pedidos:
		print('\nResumen del último pedido:')
		print(pedidos[-1])

	print('Stock actualizado:')
	for prod in tienda.listar_productos():
		print(f"  - {prod}")

if __name__ == '__main__':
	main()
