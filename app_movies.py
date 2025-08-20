import random
from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {"id": 1, "title": "The Matrix", "genre": "Sci-Fi"},
    {"id": 2, "title": "Inception", "genre": "Sci-Fi"},
    {"id": 3, "title": "The Dark Knight", "genre": "Action"},
    {"id": 4, "title": "Interstellar", "genre": "Sci-Fi"},
    {"id": 5, "title": "The Godfather", "genre": "Drama"},
    {"id": 6, "title": "Pulp Fiction", "genre": "Crime"},
    {"id": 7, "title": "Forrest Gump", "genre": "Drama"},
    {"id": 8, "title": "Fight Club", "genre": "Drama"},
    {"id": 9, "title": "Avengers: Endgame", "genre": "Action"},
    {"id": 10, "title": "Coco", "genre": "Animation"},
]

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API de Recomendacion de Peliculas"})

# GET: todas las películas
@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

# GET: películas por género
@app.route('/api/movies/<genre>', methods=['GET'])
def get_movies_by_genre(genre):
    filtered = [m for m in movies if m["genre"].lower() == genre.lower()]
    if not filtered:
        return jsonify({"error": "No se encontraron películas para ese género"}), 404
    return jsonify(filtered)

# POST: añadir nueva película
@app.route('/api/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    if not data or "title" not in data or "genre" not in data:
        return jsonify({"error": "Se requiere 'title' y 'genre'"}), 400
    
    new_movie = {
        "id": len(movies) + 1,
        "title": data["title"],
        "genre": data["genre"]
    }
    movies.append(new_movie)
    return jsonify(new_movie), 201

# PUT: actualizar película por ID
@app.route('/api/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if not movie:
        return jsonify({"error": "Película no encontrada"}), 404

    data = request.get_json()
    movie["title"] = data.get("title", movie["title"])
    movie["genre"] = data.get("genre", movie["genre"])
    return jsonify(movie)

# DELETE: eliminar película por ID
@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if not movie:
        return jsonify({"error": "Película no encontrada"}), 404

    movies = [m for m in movies if m["id"] != movie_id]
    return jsonify({"message": f"Película con id {movie_id} eliminada"}), 200

# Nuevo feature: obtener una película aleatoria DESDE LA BRANCH
@app.route('/api/movies/random', methods=['GET'])
def get_random_movie():
    if not movies:
        return jsonify({"error": "No hay películas registradas"}), 404
    return jsonify(random.choice(movies))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
