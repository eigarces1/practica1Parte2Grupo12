# 🎬 API Práctica #1 - Parte 2  

## API para Recomendación de Películas

Esta API recomienda películas según el género solicitado por el usuario o puede sugerir títulos aleatorios. Está diseñada para ejecutarse en un contenedor Docker y permite realizar consultas sobre una colección de películas.

---

## 🐳 Construcción y Ejecución del Contenedor en Docker

Para crear la imagen en Docker se utilizó el siguiente comando: **docker build -t apimovies:v1 .**

Para crear y ejecutar un contenedor a partir de la imagen creada se utilizó el siguiente comando: **docker run -p 8080:8080 apimovies:v1**

![Docker run](<imagenes/Docker run.png>)

![Contenedor e imagen](<imagenes/contenedor e imagen generada.PNG>)

![Contenedor activo](imagenes/Docker.png)

## 🔍 Consultas realizadas al API

🔹 **Obtener todas las películas**

- Comando: curl http://localhost:8080/api/movies

![apimovie](imagenes/apimovie.png)

🔹 **Filtrar por género**

- Comando: curl http://localhost:8080/api/movies/Drama

![genero drama](imagenes/drama.png)

🔹 **Agregar una nueva película**

- Comando: curl -X POST http://localhost:8080/api/movies -H "Content-Type: application/json" -d "{\"title\":\"Gladiator\",\"genre\":\"Action\"}" 

![agregar movie](imagenes/Action.png)

🔹 **Actualizar una película** (ej: id=3)

- Comando: curl -X PUT http://localhost:8080/api/movies/3 -H "Content-Type: application/json" -d "{\"title\":\"The Dark Knight Rises\",\"genre\":\"Action\"}" 

![Actualizar](imagenes/actualizar.png)

🔹 **Eliminar una película** (ej: id=10)

- Comando: curl -X DELETE http://localhost:8080/api/movies/10

![eliminar pelicula](imagenes/Deleted.png)

## 🌐 Visualización de la API en la Web

![banner de bienvenida](<imagenes/prueba web.png>)


![consulta random movie](imagenes/random.png)

## 🚀 Tecnologías utilizadas para la práctica
 - Python + Flask
 - Docker
 - Curl

## 📌 Recomendaciones
Asegúrase de tener Docker instalado y activo antes de construir la imagen.

