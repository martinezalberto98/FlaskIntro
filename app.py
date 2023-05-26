from flask import Flask
app = flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_Home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_black():
    return 'welcome back'