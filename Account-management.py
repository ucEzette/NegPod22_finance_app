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
        # This list will store previously used passwords to check for uniqueness
        self.existing_passwords = []

    def validate_email(self, email):
        # Basic email validation using regex
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email):
            return True
        else:
            print("Invalid email format. Please enter a valid email address.")
            return False

    def validate_password(self, password):
        # Password validation: at least 6 characters, contains lowercase, uppercase, and special characters
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{6,}$'
        if re.match(password_regex, password):
            return True
        else:
            print("Password must be at least 6 characters long, include at least one uppercase letter, one lowercase letter, one number, and one special character.")
            return False

    def check_password_uniqueness(self, password):
        # Ensure the password is unique (not previously used)
        if password in self.existing_passwords:
            print("This password has already been used by another account. Please choose a different one.")
            return False
        else:
            # Add the password to the list of existing passwords
            self.existing_passwords.append(password)
            return True

    def create_account(self):
        print("Welcome to our app! Please create your account.")
        
        name = input("Enter your full name: ")

        # Get a valid email
        while True:
            email = input("Enter your email: ")
            if self.validate_email(email):
                break
        
        # Get a valid username
        while True:
            username = input("Choose a username: ")
            if len(username) > 0:
                break
            else:
                print("Username cannot be empty.")
        
        # Get a valid password with uniqueness check
        while True:
            password = input("Create a password: ")
            if self.validate_password(password) and self.check_password_uniqueness(password):
                break
        
        # Create a User object
        new_user = User(name, email, username, password)
        print(f"Account created successfully! Welcome, {new_user.name}.")
        
        # Return the user object for future use (e.g., storing in a database)
        return new_user

def main():
    account_manager = AccountManager()

    # Create the account
    user = account_manager.create_account()
    print(user)  # Display user details for confirmation

if __name__ == "__main__":
    main()
