from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO recipes (name, description, instructions, date_cooked, under_30, user_id)
            VALUES  (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s);
        """
        return connectToMySQL('users_recipes').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM recipes
            JOIN users on recipes.user_id = users.id;
        """
        results = connectToMySQL('users_recipes').query_db(query)
        recipes = []
        for row in results:
            this_recipe = cls(row)
            user_data = {
                "id": row['users.id'], 
                "first_name": row['first_name'], 
                "last_name": row['last_name'],
                "email": row['email'], 
                "password": "",
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            this_recipe.creator = user.User(user_data)
            recipes.append(this_recipe)
        return recipes
    
    @classmethod
    def get_one_recipe_with_user(cls, data):
        query = """
            SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
            WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL('users_recipes').query_db(query, data)
        one_recipe = cls(results[0])
        user_data = {
            "id":results[0] ['users_id'],
            "first_name":results[0]['first_name'],
            "last_name":results[0]['last_name'],
            "email":results[0]['email'],
            "password":results[0]['password'],
            "created_at":results[0]['users.created_at'],
            "updated_at":results[0]['users.updated_at']
        }
        one_recipe.creator = user.User(user_data)
        return one_recipe

    @classmethod
    def update_recipe(cls,data):
        query = """
            UPDATE recipes SET name = %(name)s, description = %(description)s, 
            instructions = %(instructions)s, date_cooked = %(date_cooked)s, 
            under_30 = %(under_30)s
            WHERE recipes.id = %(id)s;
        """
        return connectToMySQL('users_recipes').query_db(query, data)