from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogPostForm(FlaskForm):

    category = StringField('Article category', validators=[Required()])
    title = StringField('Article title', validators=[Required()])
    description = StringField('Description title', validators=[Required()])
    article = TextAreaField('Type your article here', validators=[Required()])
    submit = SubmitField('Add Article')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Update')


class SubscriptionForm(FlaskForm):

    name = StringField('Pitch genre', validators=[Required()])
    title = StringField('Pitch title', validators=[Required()])
    pitch = TextAreaField('Type your pitch here', validators=[Required()])
    submit = SubmitField('Subscribe')
