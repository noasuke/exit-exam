from twitty import app, db
from flask import render_template, request, flash, session, redirect, url_for
from twitty.models import Twitty
from twitty.controllers.twitty_route import twitty_bp
import random



@app.route('/') # decorator
def index():
  return render_template('index.html', title='Home Page')


app.register_blueprint(twitty_bp)

# @app.route('/twitty/create', methods=['GET', 'POST'])
# def create():
#   if request.method == 'POST':
#     red = random.randint(0, 22)
#     green = random.randint(170, 200)
#     blue = random.randint(230, 250)

#     twitty = Twitty(red=red, green=green, blue=blue, price=float(0))
#     twitty.price = twitty.get_price()

#     db.session.add(twitty)
#     db.session.commit()

#     flash('Add new twitty successful.', 'success')

#   twitties = db.session.scalars(db.select(Twitty)
#                                 .where(Twitty.status=='sale')
#                                 .order_by(Twitty.id.desc())
#                                 ).all()
#   session['no_of_twitty'] = len(twitties)
#   return render_template('twitty/create.html', 
#                          title='Create Twitty',
#                          twitties=twitties)


# @app.route('/twitty/dashboard/sale')
# def dashboard():
#   twitties = db.session.scalars(db.select(Twitty)
#                                 .where(Twitty.status=='sale')
#                                 .order_by(Twitty.id.desc())
#                                 ).all()
  
#   return render_template('twitty/sale.html', 
#                          title='Twitty Dashboard',
#                          twitties=twitties)


# @app.route('/twitty/dashboard/sale/<int:id>')
# def sale(id):
#   twitty = db.session.get(Twitty, id)
#   twitty.status = 'sold'

#   if not session.get('total_price'):
#     session['total_price'] = 0.0

#   session['total_price'] += twitty.price

#   db.session.commit()
#   flash('Sold a twitty', 'warning')
#   return redirect(url_for('dashboard'))