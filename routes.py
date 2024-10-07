from flask import jsonify, request
from app import app, db
from models import Hero, Power, HeroPower

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Super Hero API"}), 200

# Route to get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes])

# Route to get a specific hero by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    hero_powers = [{"strength": hp.strength, "power": {"id": hp.power.id, "name": hp.power.name, "description": hp.power.description}} for hp in hero.hero_powers]
    return jsonify({"id": hero.id, "name": hero.name, "super_name": hero.super_name, "hero_powers": hero_powers})

# Route to get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{"id": power.id, "name": power.name, "description": power.description} for power in powers])

# Route to update a power's description
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.get_json()
    if "description" in data and len(data['description']) >= 20:
        power.description = data["description"]
        db.session.commit()
        return jsonify({"id": power.id, "name": power.name, "description": power.description})
    return jsonify({"errors": ["Validation errors"]}), 400

# Route to create a new hero power association
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    if data["strength"] not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["Validation errors"]}), 400
    hero_power = HeroPower(hero_id=data["hero_id"], power_id=data["power_id"], strength=data["strength"])
    db.session.add(hero_power)
    db.session.commit()
    return jsonify({"id": hero_power.id, "hero_id": hero_power.hero_id, "power_id": hero_power.power_id, "strength": hero_power.strength})
