from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Model representing the Hero
class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    # One-to-many relationship with HeroPower
    hero_powers = db.relationship('HeroPower', backref='heroes', cascade='all, delete')

    # Serialize the fields and relationships you want (avoid circular reference)
    serialize_rules = ('-hero_powers.heroes',)

    def __repr__(self):
        return f'<Hero id={self.id} name={self.name} super_name={self.super_name}>'

# Model representing the Power
class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    # One-to-many relationship with HeroPower
    hero_powers = db.relationship('HeroPower', backref='powers', cascade='all, delete')

    # Serialize specific fields
    serialize_only = ('id', 'name', 'description')

    def __repr__(self):
        return f'<Power id={self.id} name={self.name} description={self.description}>'

# Table representing the association between Hero and Power
class HeroPower(db.Model, SerializerMixin):
    __tablename__= "hero_powers"
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    # Nested serialization for HeroPower's related objects (Hero and Power)
    serialize_rules = ('-heroes.hero_powers', '-powers.hero_powers')

    def __repr__(self):
        return f'<HeroPower id={self.id} strength={self.strength} hero_id={self.hero_id} power_id={self.power_id}>'
