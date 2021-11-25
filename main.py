from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import copy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/lab6.2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


class Chainsaw(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False)
    power = db.Column(db.Integer, unique=False)
    price = db.Column(db.Integer, unique=False)

    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price


class ChainsawSchema(ma.Schema):
    class Meta:
        fields = ('name', 'power', 'price')


chainsaw_schema = ChainsawSchema()
chainsaws_schema = ChainsawSchema(many=True)


@app.route('/')
def index():
    return 'hi'


@app.route('/chainsaw', methods=['POST'])
def add_chainsaw():
    deserialized_data = ChainsawSchema().load(request.json)
    new_chainsaw = ChainsawSchema(**deserialized_data)
    db.session.add(new_chainsaw)
    db.session.commit()
    return chainsaw_schema.jsonify(new_chainsaw)


@app.route("/chainsaw", methods=["GET"])
def get_chainsaw():
    all_chainsaw = Chainsaw.query.all()
    result = chainsaws_schema.dump(all_chainsaw)
    return jsonify({'chainsaws': result})


@app.route("/chainsaw/<id>", methods=["GET"])
def chainsaw_detail(id):
    chainsaw = Chainsaw.query.get(id)
    if not chainsaw:
        abort(404)
    return chainsaw_schema.jsonify(chainsaw)


@app.route("/chainsaw/<id>", methods=["PUT"])
def chainsaw_update(id):
    chainsaw = Chainsaw.query.get(id)
    if not chainsaw:
        abort(404)
    old_chainsaw = copy.deepcopy(chainsaw)
    deserialized_data = ChainsawSchema().load(request.json)
    chainsaw.name = deserialized_data["name"]
    chainsaw.power = deserialized_data["power"]
    chainsaw.price = deserialized_data["price"]

    db.session.commit()
    return chainsaw_schema.jsonify(old_chainsaw)


@app.route("/chainsaw/<id>", methods=["DELETE"])
def chainsaw_delete(id):
    chainsaw = Chainsaw.query.get(id)
    if not chainsaw:
        abort(404)
    db.session.delete(chainsaw)
    db.session.commit()
    return chainsaw_schema.jsonify(chainsaw)


if __name__ == "__main__":
    app.run(debug=True)
