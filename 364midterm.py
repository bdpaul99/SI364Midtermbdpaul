from flask import Flask, request, render_template, redirect, url_for, flash, abort, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Email
import tweepy
import requests
import json



consumer_key = 'CHgwrlRgRs9EhEAgmkINwhHnO'
consumer_secret = 'IJmlsD2zY6Qo18NHh7yCLHVpJBT8n79e2WHxt0pdUojfdIyr1G'
access_token = '336251929-k0N4ZmLuqnGKacqYiDwF74MuRk663qhIW2LXeVpT'
access_token_secret = 'yhueP8ZVRytRvU7HIrH7WNocjaixS6vtWuSuBIkJDhCxe'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somerelativelysecurepassword'
app.debug = True


class twitterForm(FlaskForm):
	username = StringField("Enter a username to search for on twitter", validators = [Required()])
	submit = SubmitField('Submit')



@app.route('/')
def home():
    return redirect("http://localhost:5000/index")
    

@app.route('/index')
def index():
    simpleForm = twitterForm()

    return render_template('twitterform.html',form = simpleForm)



@app.route('/twitterresult', methods = ['GET', 'POST'])
def result():
    form = twitterForm(request.form)
    if request.method == 'POST':
        username = form.username.data
        resp = make_response(render_template('twitterresult.html', name = username))
        resp.set_cookie('username', username)
        
        return resp
    
@app.route('/<user_name>/tweets')
def twitter_users(user_name):
    try:
        timeline = api.user_timeline(id = user_name)
        
    except:
        abort(500)
    
    
    return render_template('user_tweets.html', result = timeline, name = user_name)

@app.route('/<user_name>/followers')
def twitter_followers(user_name):
    try:
        followers = api.followers(id = user_name)
    except:
        abort(500)
    return render_template('twitter_followers.html', result = followers, name = user_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



@app.errorhandler(500)
def internal_server(e):
    return render_template('500.html')













if __name__ == '__main__':
  
    app.run()