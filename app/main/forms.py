from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required,Email
# from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Share your comment:',validators=[Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    text = TextAreaField('Text',validators=[Required()])
    category = SelectField('Type',choices=[('interview','ENTERTAINMENT pitch'),('product','MOTIVATIONAL pitch'),('promotion','LOVE pitch'),('games','SOCCER pitch')],validators=[Required()])
    submit = SubmitField('Submit')