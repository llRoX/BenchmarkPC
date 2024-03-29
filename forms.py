from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.fields.html5 import EmailField 
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from bench.models import User

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired('Enter Email'), Email("Please enter your email address.")])
    password = PasswordField("Password", validators=[InputRequired('Enter Password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired("Please Enter A Valid Username")])
    email = EmailField("Email Address", validators=[InputRequired("Please enter a valid email address")])
    password = PasswordField("Password", validators=[InputRequired(), EqualTo('confirm', message="Passwords Should Match")])
    confirm = PasswordField("Confirm Password",validators=[InputRequired()])
    phone_number = StringField("Phone Number", validators=[InputRequired("Please Enter A Phone Number")])
    #confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")

    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).scalar()
        if user is not None:
            raise ValidationError("Please Use Another Email Address")

    def validate_phone(self, phone_number):
        user = User.query.filter_by(phone=phone_number.data).scalar()
        if user is not None:
            raise ValidationError("Phone Number Already In Use")

class bidForm(FlaskForm):
    pass;


#Form is too complex for flask forms,
#Still need form class for CSRF token
class newListingForm(FlaskForm):
    pass
class manageListingForm(FlaskForm):
    pass


