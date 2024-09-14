from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twittydb.sqlite'
app.config['SECRET_KEY'] = b'diekdieikdiei90049olfk'

db = SQLAlchemy(app)


from twitty import routes, models