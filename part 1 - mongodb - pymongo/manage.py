import json

from bson.json_util import dumps
from flask import Flask, request, Response
from pymongo import MongoClient

from database.db import initialize_db
from database.models import Movie

client = MongoClient('localhost:27017')
db = client['movies_bag']
app = Flask(__name__)

initialize_db(app)


@app.route("/movies", methods=['GET'])
def get_all_contact():
    try:
        contacts = db.Contacts.find()
        return dumps(contacts)
    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/add_movies", methods=['POST'])
def add_contact():
    try:
        data = json.loads(request.data)
        user_name = data['name']
        user_contact = data['contact']
        if user_name and user_contact:
            status = db.Contacts.insert_one({
                "name": user_name,
                "contact": user_contact
            })
        return dumps({'message': 'SUCCESS'})
    except Exception as e:
        return dumps({'error': str(e)})


app.run()
