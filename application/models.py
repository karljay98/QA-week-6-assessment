from application import db

class Owners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(70), nullable=False)
    shoes = db.relationship('Shoes', backref='owner')

class Shoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shoe_name = db.Column(db.String(40), nullable=False)
    shoe_size = db.Column(db.Integer, nullable=False)
    shoe_colour = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)