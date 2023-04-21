import json

from bson.json_util import dumps
from flask import Blueprint, request

from config import dbConnection

movies = Blueprint('movies', __name__)
CONTACTS = 'contacts'


@movies.route("/movies", methods=['GET'])
def get_all_contact():
    try:
        contacts = dbConnection[CONTACTS].find()
        return dumps(contacts)
    except Exception as e:
        return dumps({'error': str(e)})


@movies.route("/add_movies", methods=['POST'])
def add_contact():
    try:
        data = json.loads(request.data)
        user_name = data['name']
        user_contact = data['contact']
        if user_name and user_contact:
            status = dbConnection[CONTACTS].insert_one({
                "name": user_name,
                "contact": user_contact
            })
        return dumps({'message': 'SUCCESS'})
    except Exception as e:
        return dumps({'error': str(e)})
