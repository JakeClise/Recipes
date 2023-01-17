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

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO recipes (name, description, instructions, date_cooked, under_30, user_id)
            VALUES  (%(name)s, %(description)s, %(instruction)s, %(date_cooked)s, %(under_30)s, %(user_id)s);
        """
        return connectToMySQL('users_recipes').query_db(query, data)
