from flask import Flask, request, jsonify, render_template
from forms import CupcakeForm
from models import Cupcake, db, connect_db


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "oh-so-secret"

connect_db(app)


@app.route("/")
def home_page():
    form = CupcakeForm()
    return render_template("index.html", form=form)


@app.route("/api/cupcakes")
def list_cupcakes():
    cupcakes = Cupcake.query.all()
    response = jsonify(cupcakes=[cupcake.serialize() for cupcake in cupcakes])
    return response


@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    response = jsonify(cupcake=cupcake.serialize())
    return response


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    new_cupcake = Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=request.json.get("image", None),
    )
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    db.session.commit()
    response = jsonify(cupcake=cupcake.serialize())
    return response


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
