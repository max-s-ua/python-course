from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class EditProfileForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    about_me = TextAreaField('About user', validators=[Length(min=0,max=140)])
    submit = SubmitField('Submit')
