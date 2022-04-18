from application import app, db
from application.forms import OwnersForm, ShoesForm
from application.models import Owners, Shoes
from flask import render_template, request , redirect, url_for


@app.route('/index')
def index():
    
    all_owners = Owners.query.all()
    return render_template('index.html', all_owners=all_owners)

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
     form=OwnersForm()

     if request.method == "POST":
         owner = Owners(first_name=form.first_name.data, last_name=form.last_name.data)
         db.session.add(owner)
         db.session.commit()


     return render_template('add_owner.html', form=form)

@app.route('/add_shoe', methods=['GET', 'POST'])
def add_shoe():
    form=ShoesForm()
    
    if request.method == 'POST':
        shoe = Shoes(shoe_name=form.shoe_name.data, shoes_size=form.shoe_size.data, shoe_colour=form.shoe_colour.data)
        db.session.add(shoe)
        db.session.commit()
         
    return render_template('add_shoe', form=form)