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

# Main execute
if __name__ == '__main__':

    app.run(debug=True)