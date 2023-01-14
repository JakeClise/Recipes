from flask_app import app
from flask import render_template, redirect

@app.route('/')
def home():
    return render_template('login_and_register.html')
#REMEMBER TO REMOVE BYPASS
@app.route('/bypass')
def skip_to_welcome():
    return redirect('/welcome')

@app.route('/welcome')
def welcome_user():
    return render_template ('welcome.html')

@app.route('/recipes/new')
def new_recipes_form():
    return render_template('new_recipes_form.html')