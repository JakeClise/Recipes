from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


@app.route('/recipes/new')
def new_recipes_form():
    return render_template('new_recipes_form.html')

@app.route('/create/recipe', methods = ["POST"])
def save_recipe():
    data = {
        'user_id': session['user_id'], 
        'name': request.form['name'],
        'description': request.form['description'], 
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'],
        'under_30': request.form['under_30']
    }
    Recipe.save(data)
    return redirect('/welcome')

@app.route('/edit/<int:id>')
def edit_recipe(id):
    data = {
        "id": session['user_id']
    }
    recipe_id = {
        "id": id
    }
    one_recipe = Recipe.get_one_recipe_with_user(recipe_id)
    return render_template('edit_recipe.html', one_recipe = one_recipe, user = User.get_by_id(data))

@app.route('/update/<int:id>', methods = ["POST"])
def update_recipe(id):
    recipe_data = {
        "id": id,
        'user_id': session['user_id'], 
        'name': request.form['name'],
        'description': request.form['description'], 
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'],
        'under_30': request.form['under_30']
    }
    Recipe.update_recipe(recipe_data)
    return redirect('/welcome')

