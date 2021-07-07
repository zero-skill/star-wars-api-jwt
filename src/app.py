from flask import Flask, json, jsonify, request
from flask_migrate import Migrate
from models import Character, Favorite_Characters, Favorite_Planets, Planet, db, User
from flask_jwt_extended import create_access_token,  jwt_required, get_jwt_identity, JWTManager
app = Flask(__name__)
app.config['DEBUG']=True
app.config['ENV']='development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = "ULTRA-SECRET"

jwt=JWTManager(app)
db.init_app(app)
Migrate(app,db)



@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username, password=password).one_or_none()
    if user is None:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"token" :access_token, "user_id" : user.id})

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify(
        id=user.id,
        email=user.email,
        username=user.username,
    ),200

#POST, DELETE FAVORITE PlANETS
@app.route("/favorite/planet/<int:planet_id>",methods=["POST","DELETE"])
@jwt_required()
def favorite_planet(planet_id):
    current_user = get_jwt_identity()
    if request.method == 'POST':
        planet = Planet.query.get(planet_id)
        #favorite_planet = Favorite_Planets.query.filter_by(user_id=current_user,planet_id=planet_id).one_or_none()
        if planet is None:
            return jsonify({"msg": "Planet not founded"}),403
        #if favorite_planet is None:
        #    return jsonify({"msg": "Planet already exists in your favorites"}), 406
        user_id = request.json.get('user_id', current_user)
        planet_id = request.json.get('planet_id', planet_id)
        favorite_planet = Favorite_Planets()
        favorite_planet.user_id=user_id
        favorite_planet.planet_id=planet_id
        favorite_planet.save()
        return jsonify(favorite_planet.serialize()),201
    if request.method == 'DELETE':
        favorite_planet = Favorite_Planets.query.filter_by(user_id=current_user,planet_id=planet_id).one_or_none()
        if favorite_planet is None:
            return jsonify({"msg": "Character not founded"}), 403
        favorite_planet.delete()
        return jsonify({"success": "Character eliminated from your favorites"}), 201

#POST, DELETE FAVORITE PEOPLE
@app.route("/favorite/people/<int:people_id>", methods=["POST","DELETE"])
@jwt_required()
def favorite_people(people_id):
    current_user = get_jwt_identity()
    if request.method == 'POST':
        character = Character.query.get(people_id)
        #favorite_character = Favorite_Characters.query.filter_by(user_id=current_user,character_id=people_id).one_or_none()
        if character is None:
            return jsonify({"msg": "Character not founded"}), 403
        #if favorite_character is None:
        #    return jsonify({"msg": "Character already exists in your favorites"}), 406
        user_id = request.json.get('user_id', current_user)
        character_id = request.json.get('character_id', people_id)
        favorite_character = Favorite_Characters()
        favorite_character.user_id= user_id
        favorite_character.character_id=character_id

        favorite_character.save()
        return jsonify(favorite_character.serialize()),201
    if request.method=='DELETE':
        favorite_character = Favorite_Characters.query.filter_by(user_id=current_user,character_id=people_id).one_or_none()
        if favorite_character is None:
            return jsonify({"msg": "Character not founded"}), 403
        favorite_character.delete()
        return jsonify({"success": "Character eliminated from your favorites"}), 201

#GET, POST, PUT, DELETE USERS
@app.route('/users', methods=['GET','POST'])
@app.route('/users/<int:id>',methods=['GET','PUT','DELETE'])
def users(id=None):
    if request.method == 'GET':
        if id is not None:
            user= User.query.get(id)
            return jsonify(user.serialize()),200
        users = User.query.all()
        users = list(map(lambda user: user.serialize(),users))
        return jsonify(users),200
        
    if request.method=='POST':
        password=request.json.get('password','')
        email=request.json.get('email','')
        username=request.json.get('username','')
        user= User()
        user.password=password
        user.email=email
        user.username=username
        user.save()
        return jsonify(user.serialize()),201
    if request.method=='DELETE':
        user = User.query.get(id)
        user.delete()
        return jsonify({"success":"user deleted"}) ,200

#GET, POST, PUT, DELETE PEOPLE
@app.route('/people',methods=['GET','POST'])
@app.route('/people/<int:id>',methods=['GET','PUT','DELETE'])
def people(id=None):
    if request.method == 'GET':
        if id is not None:
            character = Character.query.get(id)
            return jsonify(character.serialize()),200
        people = Character.query.all()
        people = list(map(lambda character: character.serialize(),people))
        return jsonify(people),200
    if request.method=='POST':
        height= request.json.get('height','')
        mass = request.json.get('mass','')
        hair_color = request.json.get('hair_color','')
        eye = request.json.get('eye','')
        birth_year = request.json.get('birth_year','')
        gender = request.json.get('gender','')
        character = Character()
        character.height= height
        character.mass=mass
        character.hair_color=hair_color
        character.eye=eye
        character.birth_year=birth_year
        character.gender=gender
        character.save()
        return jsonify(character.serialize()),201
    if request.method == 'PUT':
        height= request.json.get('height','')
        mass = request.json.get('mass','')
        hair_color = request.json.get('hair_color','')
        eye = request.json.get('eye','')
        birth_year = request.json.get('birth_year','')
        gender = request.json.get('gender','')
        character = Character.query.get(id)
        character.height= height
        character.mass=mass
        character.hair_color=hair_color
        character.eye=eye
        character.birth_year=birth_year
        character.gender=gender
        character.update()
        return jsonify({"success":"character modified"},character.serialize()) ,200
    if request.method == 'DELETE':
        character = Character.query.get(id)
        character.delete()
        return jsonify({"success":"character deleted"}),200

#GET, POST, PUT, DELETE PLANETS
@app.route('/planets', methods=['GET','POST'])
@app.route('/planets/<int:id>',methods=['GET','PUT','DELETE'])
def planets(id=None):
    if request.method == 'GET':
        if id is not None:
            planet = Planet.query.get(id)
            return jsonify(planet.serialize()),200
        planets = Planet.query.all()
        planets = list(map(lambda planet: planet.serialize(),planets))
        return jsonify(planets),200
    if request.method=='POST':
        model = request.json.get('model','')
        starship = request.json.get('starship','')
        cost_in_credits = request.json.get('cost_in_credits','')
        length = request.json.get('length','')
        crew = request.json.get('crew','')
        passengers = request.json.get('passengers','')
        max_atmosphering_speed=request.json.get('max_atmosphering_speed','')
        hyperdrive_rating =request.json.get('hyperdrive_rating','')
        mGLT = request.json.get('mGLT','')
        cargo_capacity = request.json.get('cargo_capacity','')
        consumables =request.json.get('consumables','')
        planet = Planet()
        planet.model=model
        planet.starship=starship
        planet.cost_in_credits=cost_in_credits
        planet.length=length
        planet.crew=crew
        planet.passengers=passengers
        planet.max_atmosphering_speed=max_atmosphering_speed
        planet.hyperdrive_rating=hyperdrive_rating
        planet.mGLT=mGLT
        planet.cargo_capacity=cargo_capacity
        planet.consumables=consumables
        planet.save()
        return jsonify(planet.serialize()),201
    if request.method == 'PUT':
        model = request.json.get('model','')
        starship = request.json.get('starship','')
        cost_in_credits = request.json.get('cost_in_credits','')
        length = request.json.get('length','')
        crew = request.json.get('crew','')
        passengers = request.json.get('passengers','')
        max_atmosphering_speed=request.json.get('max_atmosphering_speed','')
        hyperdrive_rating =request.json.get('hyperdrive_rating','')
        mGLT = request.json.get('mGLT','')
        cargo_capacity = request.json.get('cargo_capacity','')
        consumables =request.json.get('consumables','')
        planet = Planet.query.get(id)
        planet.model=model
        planet.starship=starship
        planet.cost_in_credits=cost_in_credits
        planet.length=length
        planet.crew=crew
        planet.passengers=passengers
        planet.max_atmosphering_speed=max_atmosphering_speed
        planet.hyperdrive_rating=hyperdrive_rating
        planet.mGLT=mGLT
        planet.cargo_capacity=cargo_capacity
        planet.consumables=consumables
        planet.update()
        return jsonify({"success":"planet modified"},planet.serialize()) ,200
    if request.method=='DELETE':
        planet = Planet.query.get(id)
        planet.delete()
        return jsonify({"success":"planet deleted"}) ,200
if __name__ == '__main__':
    app.run(host='127.0.0.1')