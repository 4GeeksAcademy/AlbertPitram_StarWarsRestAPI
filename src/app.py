from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Dades simulades a memòria
people = [
    { "id": 1, "name": "Luke Skywalker" },
    { "id": 2, "name": "Leia Organa" }
]

planets = [
    { "id": 1, "name": "Tatooine" },
    { "id": 2, "name": "Alderaan" }
]

users = [
    { "id": 1, "username": "anakin" }
]

favorites = []  # [{ user_id: 1, type: "planet"/"people", id: 2 }]


# ---------- PEOPLE ----------
@app.route("/people", methods=["GET"])
def get_people():
    return jsonify(people)

@app.route("/people/<int:people_id>", methods=["GET"])
def get_one_person(people_id):
    person = next((p for p in people if p["id"] == people_id), None)
    if person:
        return jsonify(person)
    return jsonify({"error": "Person not found"}), 404


# ---------- PLANETS ----------
@app.route("/planets", methods=["GET"])
def get_planets():
    return jsonify(planets)

@app.route("/planets/<int:planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = next((p for p in planets if p["id"] == planet_id), None)
    if planet:
        return jsonify(planet)
    return jsonify({"error": "Planet not found"}), 404


# ---------- USERS ----------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/favorites", methods=["GET"])
def get_user_favorites():
    user_favs = [f for f in favorites if f["user_id"] == 1]
    return jsonify(user_favs)


# ---------- FAVORITES ----------
@app.route("/favorite/planet/<int:planet_id>", methods=["POST"])
def add_fav_planet(planet_id):
    favorites.append({ "user_id": 1, "type": "planet", "id": planet_id })
    return jsonify(favorites)

@app.route("/favorite/people/<int:people_id>", methods=["POST"])
def add_fav_people(people_id):
    favorites.append({ "user_id": 1, "type": "people", "id": people_id })
    return jsonify(favorites)

@app.route("/favorite/planet/<int:planet_id>", methods=["DELETE"])
def delete_fav_planet(planet_id):
    global favorites
    favorites = [f for f in favorites if not (f["user_id"] == 1 and f["type"] == "planet" and f["id"] == planet_id)]
    return jsonify(favorites)

@app.route("/favorite/people/<int:people_id>", methods=["DELETE"])
def delete_fav_people(people_id):
    global favorites
    favorites = [f for f in favorites if not (f["user_id"] == 1 and f["type"] == "people" and f["id"] == people_id)]
    return jsonify(favorites)
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
