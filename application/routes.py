from application import app, db
from application.forms import OwnersForm, ShoesForm
from application.models import owners, Shoes
from flask import render_template, request, redirect, url_for


@app.route('/index')
def index():
    all_owners = Owners.query.all()
    return render_template('index.html', all_owners=all_owners)