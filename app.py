from typing import Sized
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


@app.route("/")
def index_page():

    return render_template("index.html")


@app.route("/api/cupcakes")
def list_cupcakes():
    """Returns JSON with all cupcakes."""

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=all_cupcakes)


@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """Return single cupcake."""

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create a cupcake."""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]

    #  if image is null, DEFAULT_PHOTO is used
    image = request.json["image"] or None

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    response_json = jsonify(cupcake=new_cupcake.serialize())

    return (response_json, 201)


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    """Update cupcake details."""

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json["flavor"]
    cupcake.rating = request.json["rating"]
    cupcake.size = request.json["size"]
    cupcake.image = request.json["image"]

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """Delete todo."""

    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")