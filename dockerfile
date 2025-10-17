# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY tienda_online/ /app/tienda_online/

# Establecer la variable de entorno PYTHONPATH
ENV PYTHONPATH=/app

# Exponer un puerto (opcional, si fuera una API web)
# EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "tienda_online/main.py"]
