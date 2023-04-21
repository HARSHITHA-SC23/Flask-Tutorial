from flask import Flask
from blueprint.movies import movies

app = Flask(__name__)

app.register_blueprint(movies)
app.run()
