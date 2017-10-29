from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Email

import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somerelativelysecurepassword'
app.debug = True


class twitterForm(FlaskForm):
	username = StringField("Enter a username to search for on twitter", validators = [Required()])
	submit = SubmitField('Submit')

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/index')
def index():
    simpleForm = twitterForm()

    return render_template('twitterform.html',form = simpleForm)



@app.route('/result', methods = ['GET', 'POST'])
def result():
    form = twitterForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        
        return render_template('twitterresult.html',name = username)
    





















if __name__ == '__main__':
  
    app.run()