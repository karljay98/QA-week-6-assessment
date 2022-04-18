from application import app, db
from application.forms import OwnersForm, ShoesForm
#from application.models import Owners, Shoes
from flask import render_template #, request, redirect, url_for


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
     form=OwnersForm()
     return render_template('add_owner.html', form=form)

@app.route('/add_shoe', methods=['GET', 'POST'])
def add_shoe():
    form=ShoesForm()
    return render_template('add_shoe', form=form)