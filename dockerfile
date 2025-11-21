# Usar imagen base oficial de Python 3.12-slim
FROM python:3.12-slim

# Información del mantenedor
LABEL maintainer="yagooramos"
LABEL description="Tienda Online - Sistema de gestión con Python"

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar primero requirements.txt para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al contenedor
COPY tienda_online/ /app/tienda_online/

# Crear un usuario no privilegiado para ejecutar la aplicación
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app && \
    chmod -R 755 /app

# Cambiar al usuario no privilegiado
USER appuser

# Configurar variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

# Exponer puerto (opcional, preparado para futuras implementaciones de API)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "tienda_online/main.py"]
