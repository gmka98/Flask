from flask import Flask, jsonify, request, abort, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)

mangas = [
    {'id': 1, 'title': 'Dragon ball', 'author': 'Akira Toriyama', 'year': '1984'},
    {'id': 2, 'title': 'One Piece', 'author': 'Eiichirō Oda', 'year': '1997'},
    {'id': 3, 'title': 'Kuroko No Basket', 'author': 'Tadatoshi Fujimaki', 'year': '2008'},
    {'id': 4, 'title': 'Attack on Titans', 'author': 'Hajime Isayama', 'year': '2009'},
    {'id': 5, 'title': 'Hajime No Ippo', 'author': 'George Morikawa', 'year': '1989'},
    {'id': 6, 'title': 'Bleach', 'author': 'Tite Kubo', 'year': '2001'},
    {'id': 7, 'title': 'Naruto', 'author': 'Masashi Kishimoto', 'year': '1999'},
]

@app.route("/api/mangas", methods=["GET"])
def get_all_mangas():
    return jsonify({"mangas": mangas})

@app.route("/api/mangas/<int:id>", methods=["GET"])
def get_manga(id):
    data = [manga for manga in mangas if manga['id'] == id]
    if len(data) == 0:
        abort(404)
    return jsonify({"manga": data[0]})

@app.route("/api/mangas", methods=["POST"])
def add_manga():
    if not request.json or not "title" in request.json:
        abort(400)
    manga = {
        "id": mangas[-1]["id"] + 1,
        "title": request.json["title"],
        "author": request.json.get('author', ''),
        "year": request.json.get('year', '')
    }
    mangas.append(manga)
    return jsonify({"manga": manga})

@app.route("/api/mangas/<int:id>", methods=["PUT"])
def update_manga(id):
    data = [manga for manga in mangas if manga["id"] == id]
    if len(data) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if "title" in request.json and not isinstance(request.json['title'], str):
        abort(400)
    if "author" in request.json and not isinstance(request.json['author'], str):
        abort(400)
    if "year" in request.json and not isinstance(request.json['year'], int):
        abort(400)
    data[0]['title'] = request.json.get('title', data[0]['title'])
    data[0]['author'] = request.json.get('author', data[0]['author'])
    data[0]['year'] = request.json.get('year', data[0]['year'])
    return jsonify({'manga': data[0]})

@app.route("/api/mangas/<int:id>", methods=['DELETE'])
def delete_manga(id):
    data = [manga for manga in mangas if manga['id'] == id]
    if len(data) == 0:
        abort(404)


if __name__ == '__main--':
    app.run(debug=True)
