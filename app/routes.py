from flask import request, jsonify
from app import app, db
from app.models import User, PersonSchema, Activity, ActivitySchema

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)


@app.route('/')
@app.route('/index')
def index() -> str:
    return "Hello, World!"


@app.route('/person', methods=["POST"])
def add_person() -> str:
    username: str = request.json['username']
    email: str = request.json['email']

    new_person: User = User(username=username, email=email)
    db.session.add(new_person)
    db.session.commit()

    result = person_schema.dump(new_person)
    return jsonify(result.data)


@app.route('/person', methods=["GET"])
def get_people() -> str:
    all_people = User.query.all()
    result = people_schema.dump(all_people)
    return jsonify(result.data)


@app.route("/person/<user_id>", methods=["GET"])
def user_detail(user_id: str) -> str:
    user: User = User.query.get(user_id)
    return person_schema.jsonify(user)


@app.route("/person/<user_id>", methods=["PUT"])
def user_update(user_id: str) -> str:
    person: User = User.query.get(user_id)
    username: str = request.json['username']
    email: str = request.json['email']

    person.email = email
    person.username = username

    db.session.commit()
    return person_schema.jsonify(person)


@app.route("/person/<user_id>", methods=["DELETE"])
def user_delete(user_id: str) -> str:
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return person_schema.jsonify(user)


@app.route("/activity", methods=["POST"])
def new_activity() -> str:
    activity: str = request.json['activity']
    user_id: int = request.json['userId']

    new_scrum_activity: Activity = Activity(activity=activity, user_id=user_id)
    db.session.add(new_scrum_activity)
    db.session.commit()

    result = activity_schema.dump(new_scrum_activity)
    return jsonify(result.data)


@app.route('/activity/<associated_user>', methods=["GET"])
def get_activities(associated_user: str) -> str:
    all_activities = Activity.query.filter_by(user_id=associated_user).all()
    result = activities_schema.dump(all_activities)
    return jsonify(result.data)


@app.route('/activity/<activity_id>', methods=["PUT"])
def update_activity(activity_id: str) -> str:
    activity: Activity = Activity.query.get(activity_id)

    activity_content: str = request.json['activity']

    activity.activity = activity_content
    db.session.commit()

    return activity_schema.jsonify(activity)


@app.route('/activity/<activity_id>', methods=["DELETE"])
def delete_activity(activity_id: str) -> str:
    activity: Activity = Activity.query.get(activity_id)

    db.session.delete(activity)
    db.session.commit()

    return activity_schema.jsonify(activity)
