from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email

from wtforms import SelectField, StringField, TextAreaField

class MyForm(FlaskForm):
    choice_field = SelectField(
        'Choose Option',
        choices=[('option1', 'Option 1'), ('option2', 'Option 2')]
    )
    option1_field = StringField('Option 1 Field')
    option2_field = TextAreaField('Option 2 Field')
    submit = SubmitField('Submit')

