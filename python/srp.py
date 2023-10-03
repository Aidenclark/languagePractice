class UserDatabase:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def store_user(self):
        # Logic to store user details in a database
        pass

class UserEmailer:
    def __init__(self, user_email):
        self.user_email = user_email

    def send_welcome_email(self):
        # Logic to send a welcome email to the user
        pass  

class UserProfile:
    def __init__(self, user_data):
        self.user_data = user_data

    def display_user_profile(self):
        # Logic to display the user's profile in a UI
        pass
