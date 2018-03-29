from flask_wtf import FlaskForm
from wtforms import BooleanField,TextAreaField,PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name =TextAreaField('Name', validators=[DataRequired()])
    password =PasswordField('PassWord',validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
