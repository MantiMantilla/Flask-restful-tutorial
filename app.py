from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow  

# Create Flask service.
app = Flask(__name__)

# Add local database to app config.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Remove unused sqlalchemy event system. Defaul is None, which is falsy.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create database object using app config dictionary
db = SQLAlchemy(app)

# Create JSON deserializer
ma = Marshmallow(app)

# Class for template of table: publicacion. Lista de publicaciones con sus atributos
class Publicacion(db.Model):

	# Columna identidad e índice (sin valores repetidos)
    id = db.Column(db.Integer, primary_key = True)

	# Columna con el título de cada publicación.
    titulo = db.Column( db.String(50) )

	# Columna con el contenido de la publicación 
    contenido = db.Column( db.String(255) )

# Class template of expected JSON structured posts. No fields are excluded but one may wish to not expose confidential fields
class Publicacion_Schema(ma.Schema):

    class Meta:

        fields = ("id", "titulo", "contenido")

# Single schema for single posts
post_schema = Publicacion_Schema()

# Multiple shemas for multiple posts
posts_schema = Publicacion_Schema(many = True)

# Main execute
if __name__ == '__main__':

	# Desplegar el servicio
    app.run(debug=True)