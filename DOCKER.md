# Instrucciones Docker

## Construcción de la Imagen Docker

Para construir la imagen Docker de la aplicación, ejecuta:

```bash
docker build -t tienda-online:latest .
```

## Ejecución del Contenedor

Para ejecutar la aplicación en un contenedor Docker:

```bash
docker run --rm tienda-online:latest
```

### Opciones adicionales:

**Modo interactivo** (para ver la salida en tiempo real):
```bash
docker run -it --rm tienda-online:latest
```

**Con nombre personalizado**:
```bash
docker run --name mi-tienda --rm tienda-online:latest
```

**En segundo plano (detached)**:
```bash
docker run -d --name mi-tienda tienda-online:latest
```

Para ver los logs del contenedor en segundo plano:
```bash
docker logs mi-tienda
```

## Verificación de la Imagen

Para listar las imágenes Docker disponibles:
```bash
docker images | grep tienda-online
```

## Limpieza

Para eliminar la imagen:
```bash
docker rmi tienda-online:latest
```

Para eliminar contenedores detenidos:
```bash
docker container prune
```

## Características del Dockerfile

- **Imagen base**: Python 3.11 slim (ligera y optimizada)
- **Usuario no privilegiado**: La aplicación se ejecuta con un usuario sin permisos de root
- **Variables de entorno**: Configuradas para optimizar la ejecución de Python
- **Puerto expuesto**: 8000 (preparado para futuras implementaciones de API)
- **.dockerignore**: Optimiza el tamaño de la imagen excluyendo archivos innecesarios

## Notas

Esta configuración está preparada para:
- Desarrollo y pruebas locales
- Despliegue en entornos de producción
- Futura conversión a API REST (puerto 8000 ya expuesto)
