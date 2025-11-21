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

Para ejecutar la aplicación:

```bash
python tienda_online/main.py
```

### Objetivo Académico

Este proyecto forma parte de las prácticas de la asignatura **Arquitectura del Software**, donde se aplican conceptos de:
- Control de versiones con Git
- Gestión de repositorios con GitHub
- Flujos de trabajo con ramas (branching)
- Integración continua y DevOps
- Containerización con Docker

---

**Repositorio**: https://github.com/yagooramos/devops_practica
