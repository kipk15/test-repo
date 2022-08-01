
class User:
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is a {self.age}"
        f" year old {self.occupation}")
    def greet_user(self):
        print(f"\nHey {self.first_name}, what's poppin")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def show_privileges(self, privileges = 
        ['can add post', 
        'can delete post', 
        'can ban user']):
        print(f"Your account has admin rights and can: ")
        for item in privileges:
            print(f"\t-{item}")


class Admin(User):
    def __init__(self, first_name, last_name, age, occupation):
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = Privileges()
        
user1 = User('Steven', 'Gerrad', 13, 'baller')
user1.describe_user()
admin1 = Admin('Seth', 'Jackson', 22, 'Actor')
admin1.privileges.show_privileges()
admin1.describe_user()
