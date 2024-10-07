from flask import jsonify, request
from app import app, db
from models import Hero, Power, HeroPower

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Super Hero API"}), 200

# a. Route to get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes]), 200

# b. Route to get a specific hero by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    # Serialize hero_powers and include the associated power for each hero_power
    hero_powers = [
        {
            "id": hp.id,
            "hero_id": hp.hero_id,
            "power_id": hp.power_id,
            "strength": hp.strength,
            "power": hp.powers.to_dict(only=('id', 'name', 'description'))  # Serialize the associated power
        }
        for hp in hero.hero_powers
    ]

    # Return the full hero details, including the serialized hero_powers
    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": hero_powers  # Use the custom serialization
    }), 200

# c. Route to get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict(only=('id', 'name', 'description')) for power in powers]), 200

# d. Route to get a specific power by ID
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict(only=('id', 'name', 'description'))), 200

# e. Route to update a power's description
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.get_json()
    if "description" in data and len(data['description']) >= 20:
        power.description = data["description"]
        db.session.commit()
        return jsonify(power.to_dict(only=('id', 'name', 'description'))), 200
    return jsonify({"errors": ["validation errors"]}), 400

# f. Route to create a new hero power association
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    if data["strength"] not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["validation errors"]}), 400
    hero_power = HeroPower(hero_id=data["hero_id"], power_id=data["power_id"], strength=data["strength"])
    db.session.add(hero_power)
    db.session.commit()
    return jsonify({
        "id": hero_power.id,
        "hero_id": hero_power.hero_id,
        "power_id": hero_power.power_id,
        "strength": hero_power.strength,
        "hero": hero_power.heroes.to_dict(only=('id', 'name', 'super_name')),
        "power": hero_power.powers.to_dict(only=('id', 'name', 'description'))
    }), 201
