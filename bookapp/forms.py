from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField,FileAllowed,FileRequired


class SignupForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="hello, full name required")])
    email = StringField("Your Email",validators=[Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[EqualTo("password",message="Must match password")])
    
    btn = SubmitField("Sign Up!")


class ProfileForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="hello, full name required")])
    pix= FileField("Display Picture",validators=[FileRequired(),FileAllowed(['jpg','png'],'Images only!')])
    btn = SubmitField("Update Profile!")
  
    
    
    
    
    
     
    

