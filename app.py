from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask service.
app = Flask(__name__)

# Add local database to app config.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Remove unused sqlalchemy event system. Defaul is None, which is falsy.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create database object using app config dictionary
db = SQLAlchemy(app)

# Class for template of table: publicacion. Lista de publicaciones con sus atributos
class Publicacion(db.Model):

	# Columna identidad e índice (sin valores repetidos)
    id = db.Column(db.Integer, primary_key = True)

	# Columna con el título de cada publicación.
    titulo = db.Column( db.String(50) )

	# Columna con el contenido de la publicación 
    contenido = db.Column( db.String(255) )

# Main execute
if __name__ == '__main__':

	# Desplegar el servicio
    app.run(debug=True)