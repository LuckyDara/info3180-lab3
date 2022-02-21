from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email, length

class ContactForm(FlaskForm):
    name = StringField('Please enter your name', validators=[DataRequired()])
    email = EmailField('Please enter your e-mail address',validators=[DataRequired(), Email()])
    subject = StringField('Please enter the subject of your message', validators=[DataRequired()])
    message = TextAreaField('Please enter the message you\'d like to send',  validators=[DataRequired(), length(max=500)])
    submit=SubmitField("Send")