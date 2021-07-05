from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(250),nullable=False)
    email = db.Column(db.String(250),nullable=False)
    username = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "password": self.password,
            "email": self.email,
            "username": self.username       
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Character(db.Model):
    __tablename__= 'character'
    id= db.Column(db.Integer, primary_key=True)
    height= db.Column(db.String(250))
    mass = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    eye = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    def serialize(self):
        return {
            "id": self.id,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "eye":self.eye,
            "birth_year":self.birth_year,       
            "gender":self.gender    
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planet(db.Model):
    __tablename__= 'planet'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250))
    starship = db.Column(db.String(250))
    cost_in_credits = db.Column(db.String(250))
    length = db.Column(db.String(250))
    crew = db.Column(db.String(250))
    passengers = db.Column(db.String(250)) 
    max_atmosphering_speed = db.Column(db.String(250))
    hyperdrive_rating = db.Column(db.String(250))
    mGLT = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    consumables = db.Column(db.String(250))

    def serialize(self):
        return {
            "id":self.id,
            "model":self.model,
            "starship":self.starship,
            "cost_in_credits":self.cost_in_credits,
            "length":self.length,
            "crew":self.crew,
            "passengers":self.passengers,
            "max_atmosphering_speed":self.max_atmosphering_speed,
            "hyperdrive_rating":self.hyperdrive_rating,
            "mGLT":self.mGLT,
            "cargo_capacity":self.cargo_capacity,
            "consumables":self.consumables 
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()