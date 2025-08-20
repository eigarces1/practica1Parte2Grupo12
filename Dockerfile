# Imagen base de Python
FROM python:3.10-slim    

#Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt 

# Exponer el puerto de la API
EXPOSE 8080

# Comando para ejecutar la API
CMD ["python", "app_movies.py"]
