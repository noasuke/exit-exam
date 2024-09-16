from twitty import db
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
import random
from twitty.models import Twitty

twitty_bp = Blueprint('twitty_bp', __name__, url_prefix='/twitty/dashboard')

@twitty_bp.route('/create', methods=['GET', 'POST'])
def create():
  if request.method == 'POST':
    red = random.randint(0, 22)
    green = random.randint(170, 200)
    blue = random.randint(230, 250)

    twitty = Twitty(red=red, green=green, blue=blue, price=float(0))
    twitty.price = twitty.get_price()

    db.session.add(twitty)
    db.session.commit()

    flash('Add new twitty successful.', 'success')

  twitties = db.session.scalars(db.select(Twitty)
                                .where(Twitty.status=='sale')
                                .order_by(Twitty.id.desc())
                                ).all()
  
  session['no_of_twitty'] = len(twitties)
  return render_template('twitty/create.html', 
                         title='Create Twitty',
                         twitties=twitties)


@twitty_bp.route('/sale')
def dashboard():
  twitties = db.session.scalars(db.select(Twitty)
                                .where(Twitty.status=='sale')
                                .order_by(Twitty.id.desc())
                                ).all()
  
  return render_template('twitty/sale.html', 
                         title='Twitty Dashboard',
                         twitties=twitties)


@twitty_bp.route('/sale/<int:id>')
def sale(id):
  twitty = db.session.get(Twitty, id)
  twitty.status = 'sold'

  if not session.get('total_price'):
    session['total_price'] = 0.0

  session['total_price'] += twitty.price

  db.session.commit()
  flash('Sold a twitty', 'warning')
  return redirect(url_for('twitty_bp.dashboard'))