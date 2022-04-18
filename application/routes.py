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
         owner = Owners(first_name=form.first_name.data, last_name=form.last_name.data, description=form.description.data)
         db.session.add(owner)
         db.session.commit()
         return redirect(url_for('index'))


     return render_template('add_owner.html', form=form)

@app.route('/delete/<int:id>')
def delete_owner(id):
    owner = Owners.query.get(id)
    db.session.delete(owner)
    db.session.commit()
    return redirect(url_for('index'))