from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User


@app.route('/')
def home():
    return render_template('login_and_register.html')


@app.route('/register/user', methods = ["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect ('/welcome')

@app.route('/login/user', methods = ["POST"])
def login():
    data = {"email": request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("invalid Email/PW")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("invalid Email/PW")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/welcome')


@app.route('/welcome')
def welcome_user():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('welcome.html', user = User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/recipes/new')
def new_recipes_form():
    return render_template('new_recipes_form.html')

@app.route('/create/recipe', methods = ["POST"])
def save_recipe():
    pass