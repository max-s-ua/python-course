from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=50)])
    post = TextAreaField('Post text', validators=[DataRequired(), Length(min=0,max=140)])
    submit = SubmitField('Submit')
