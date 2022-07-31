
class User:
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n")
    def greet_user(self):
        print(f"\nHey {self.first_name}, what's poppin")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = ('Steven', 'Gerrad')
user1.describe_user