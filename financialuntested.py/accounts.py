import re

class User:
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        return f"User(Name: {self.name}, Email: {self.email}, Username: {self.username})"

class AccountManager:
    def __init__(self):
        self.existing_passwords = []

    def validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))

    def validate_password(self, password):
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{6,}$'
        return bool(re.match(password_regex, password))

    def check_password_uniqueness(self, password):
        if password in self.existing_passwords:
            return False
        self.existing_passwords.append(password)
        return True

    def create_account(self):
        print("Welcome to the app! Let's create your account.")
        name = input("Enter your full name: ")

        while True:
            email = input("Enter your email: ")
            if self.validate_email(email):
                break
            print("Invalid email format!")

        while True:
            username = input("Choose a username: ")
            if username:
                break
            print("Username cannot be empty.")

        while True:
            password = input("Create a password: ")
            if self.validate_password(password) and self.check_password_uniqueness(password):
                break
            print("Invalid or previously used password.")

        return User(name, email, username, password)
