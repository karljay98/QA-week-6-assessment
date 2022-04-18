from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class OwnersForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last name', validators=[Length(max=70)])
    submit = SubmitField('Add Owner')


class ShoesForm(FlaskForm):
    shoe_name = StringField('Shoe name', validators=[DataRequired(), Length(max=40)])
    shoe_size = StringField('Shoe size',validators=[DataRequired(), Length(max=20)])
    shoe_colour = StringField('Shoe colour', validators=[Length(max=20)])
    submit = SubmitField("Add shoe") 