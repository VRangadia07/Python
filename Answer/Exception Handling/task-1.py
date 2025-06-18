class Invalid_PasswordException(Exception):
    pass


class SignUp:
    def __init__(self):
        self.fn = input("Enter Name: ")
        self.ln = input("Enter Last Name: ")
        self.un = input("Enter Username: ")
        
        while True:
            try:
                self.pwd = input("Enter Password: ")
                self.validate_password(self.pwd)
                print("Signup Successful")
                break
            except Invalid_PasswordException as e:
                print(e)
        
    
    def validate_password(self, password):
        if len(password) < 8:
            raise Invalid_PasswordException("Password must be at minmum 8 characters.")
        if len(password) > 16:
            raise Invalid_PasswordException("Password must be at maximum 16 characters.")
        if not any(char.islower() for char in password):
            raise Invalid_PasswordException("Password must contain at least one lowercase letter.")
        if not any(char.isupper() for char in password):
            raise Invalid_PasswordException("Password must contain at least one uppercase letter.")
        if not any(char.isdigit() for char in password):
            raise Invalid_PasswordException("Password must contain at least one digit.")
        if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
            raise Invalid_PasswordException("Password must contain at least one special character.")
        
        
SignUp()
