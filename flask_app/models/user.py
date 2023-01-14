from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        users_recipes = []

    @classmethod
    def register_user(query, data):
        query = """
            INSERT INTO users (first_name, last_name, email)
            VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        return connectToMySQL('users_recipes').query_db(query, data)