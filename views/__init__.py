from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, DateField

class Books(FlaskForm):
    title = StringField('Title of Book', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    published_on = DateField(id='datepick')
    submit = SubmitField('Add Book')