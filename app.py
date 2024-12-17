from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Register')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        age = form.age.data
        gender = form.gender.data
        course = form.course.data
        return f"<h1>Registration Successful!</h1><p>Name: {name}</p><p>Email: {email}</p><p>Age: {age}</p><p>Gender: {gender}</p><p>Course: {course}</p>"
    return render_template('registration.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
