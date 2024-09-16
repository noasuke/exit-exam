from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twittydb.sqlite'
app.config['SECRET_KEY'] = b'diekdieikdiei90049olfk'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



from twitty import routes