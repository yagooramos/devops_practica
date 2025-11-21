# DevOps Práctica - Tienda Online

## Autor
**Yago Ramos**

## Descripción del Proyecto

Este proyecto implementa un **sistema de gestión de tienda online** desarrollado en Python utilizando principios de Programación Orientada a Objetos (POO).

### Funcionalidades Principales

- **Gestión de Usuarios**: 
  - Registro de clientes y administradores
  - Autenticación por roles (Cliente/Administrador)
  
- **Gestión de Productos**:
  - Catálogo de productos con diferentes categorías
  - Productos electrónicos con garantía
  - Productos de ropa con tallas y colores
  - Control de inventario y stock en tiempo real

- **Sistema de Pedidos**:
  - Creación de pedidos por clientes
  - Cálculo automático de totales
  - Histórico de pedidos por usuario
  - Actualización automática del stock tras cada pedido

### Estructura del Proyecto

```
tienda_online/
├── main.py                 # Punto de entrada de la aplicación
├── models/                 # Modelos de datos
│   ├── Usuario.py         # Clases Usuario, Cliente, Administrador
│   ├── Producto.py        # Clases Producto, ProductoElectronico, ProductoRopa
│   └── Pedido.py          # Clase Pedido
└── Services/              # Lógica de negocio
    └── tienda_service.py  # Servicio principal de la tienda
```

### Tecnologías Utilizadas

- **Python 3.x**: Lenguaje de programación principal
- **POO**: Diseño orientado a objetos con herencia y encapsulación
- **UUID**: Generación de identificadores únicos
- **Datetime**: Gestión de fechas y timestamps

### Ejecución

#### Ejecución Local

Para ejecutar la aplicación localmente con Python:

```bash
# Desde la raíz del proyecto
python tienda_online/main.py
```

#### Ejecución con Docker

##### 1. Construir la Imagen

Para construir la imagen Docker de la aplicación:

```bash
# Construcción básica
docker build -t tienda-online:latest .

# Construcción con etiqueta de versión
docker build -t tienda-online:1.0.0 .

# Ver la imagen creada
docker images | grep tienda-online
```

##### 2. Ejecutar el Contenedor

Diferentes formas de ejecutar la aplicación en Docker:

```bash
# Ejecución básica (se elimina automáticamente al terminar)
docker run --rm tienda-online:latest

# Ejecución con nombre personalizado
docker run --name mi-tienda --rm tienda-online:latest

# Ejecución en segundo plano (detached mode)
docker run -d --name mi-tienda tienda-online:latest

# Ver logs del contenedor en segundo plano
docker logs mi-tienda

# Ver logs en tiempo real
docker logs -f mi-tienda

# Detener y eliminar el contenedor
docker stop mi-tienda && docker rm mi-tienda
```

##### 3. Variables de Entorno Soportadas

El contenedor soporta las siguientes variables de entorno:

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `PYTHONUNBUFFERED` | Desactiva el buffering de salida | `1` |
| `PYTHONDONTWRITEBYTECODE` | Evita la creación de archivos .pyc | `1` |
| `PYTHONPATH` | Ruta base para imports de Python | `/app` |

Ejemplo de uso con variables de entorno personalizadas:

```bash
docker run --rm \
  -e PYTHONUNBUFFERED=1 \
  tienda-online:latest
```

##### 4. Salida Esperada

Al ejecutar la aplicación, deberías ver la siguiente salida en la consola:

```
Registrar usuarios
  - cli1: Ana García (cliente)
  - cli2: Luis Pérez (cliente)
  - cli3: Marta López (cliente)
  - admin1: Admin User (admin)
Crear y añadir 5 productos al inventario
. - añadido: Portátil (id=...)
. - añadido: Auriculares (id=...)
. - añadido: Camiseta (id=...)
. - añadido: Pantalón (id=...)
. - añadido: Libro (id=...)
Inventario actual
  - Producto Electrónico: Portátil, Precio: $1200.0, Stock: 10.0, Garantía: 24 meses
  - Producto Electrónico: Auriculares, Precio: $150.0, Stock: 20.0, Garantía: 12 meses
  - Producto Ropa: Camiseta, Precio: $20.0, Stock: 50.0, Talla: M, Color: Azul
  - Producto Ropa: Pantalón, Precio: $35.0, Stock: 30.0, Talla: L, Color: Negro
  - Producto (id=...): Libro, Precio: $18.5, Stock: 40.0
Simular 3 pedidos de distintos clientes
  - Pedido creado para cli1: ... (total $...)
  - Pedido creado para cli2: ... (total $...)
  - Pedido creado para cli3: ... (total $...)
Histórico de pedidos de Ana García (cli1)
  - Resumen pedido: ...
Resumen del último pedido y stock actualizado
Stock actualizado:
  - Producto Electrónico: Portátil, Precio: $1200.0, Stock: ... (actualizado)
  ...
```

##### 5. Pasos de Prueba

Para verificar que la aplicación funciona correctamente:

1. **Construir la imagen**:
   ```bash
   docker build -t tienda-online:latest .
   ```
   ✅ Debería completarse sin errores

2. **Ejecutar el contenedor**:
   ```bash
   docker run --rm tienda-online:latest
   ```
   ✅ Debería mostrar la salida completa del programa

3. **Verificar que se crean usuarios**:
   - La salida debe mostrar 3 clientes y 1 administrador

4. **Verificar que se añaden productos**:
   - Deben aparecer 5 productos en el inventario

5. **Verificar que se procesan pedidos**:
   - Deben crearse 3 pedidos exitosamente
   - El stock debe actualizarse correctamente

6. **Verificar que no hay errores**:
   - No deben aparecer mensajes de error o excepciones

##### 6. Limpieza

Para limpiar recursos de Docker:

```bash
# Eliminar la imagen
docker rmi tienda-online:latest

# Eliminar contenedores detenidos
docker container prune -f

# Eliminar todas las imágenes no utilizadas
docker image prune -a -f
```

### Requisitos

- **Python**: 3.12 o superior
- **Docker**: 20.10 o superior (para ejecutar con contenedores)
- **Git**: Para clonar el repositorio

### Instalación de Dependencias

```bash
# Si ejecutas localmente sin Docker
pip install -r requirements.txt
```

> **Nota**: Este proyecto actualmente solo utiliza la biblioteca estándar de Python, por lo que no requiere instalación de dependencias externas.

### Objetivo Académico

Este proyecto forma parte de las prácticas de la asignatura **Arquitectura del Software**, donde se aplican conceptos de:
- Control de versiones con Git
- Gestión de repositorios con GitHub
- Flujos de trabajo con ramas (branching)
- Integración continua y DevOps
- Containerización con Docker

---

**Repositorio**: https://github.com/yagooramos/devops_practica
