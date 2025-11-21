# Usar imagen base oficial de Python 3.11
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el código de la aplicación al contenedor
COPY tienda_online/ /app/tienda_online/

# Instalar dependencias del sistema si son necesarias (opcional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Crear un usuario no privilegiado para ejecutar la aplicación
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Configurar variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Exponer puerto (por si en el futuro se convierte en API)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "-m", "tienda_online.main"]
