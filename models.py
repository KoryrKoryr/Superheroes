from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db= SQLAlchemy(metadata=metadata)

# Model representing the Hero
class Hero(db.Model):
    __tablename__ = "heroes"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    # One-to-many relationship with HeroPower
    hero_powers = db.relationship('HeroPower', backref='heroes', cascade='all, delete')
    
    def __repr__(self):
        return f'<Hero id={self.id} name={self.name} super_name={self.super_name}>'