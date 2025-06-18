class Invalid_PasswordException(Exception):
    pass

class Invalid_LoginException(Exception):
    def __init__(self, message="Invalid Username and Password. Try Again"):
        self.message = message
        super().__init__(self.message)
    

class SignUp:
    def __init__(self):
        self.fn = input("Enter First Name: ")
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
        
        

class SignIn:
    def __init__(self, sign_up_user):
        self.un = input("Enter Username to login: ")
        self.pwd = input("Enter Password to login: ")
        self.sign_up_user = sign_up_user
        self.login_check()
        
    def login_check(self):
        try:
            if self.un != self.sign_up_user.un or self.pwd != self.sign_up_user.pwd:
                raise Invalid_LoginException()
            else:
                print(f"Welcome {self.sign_up_user.fn} {self.sign_up_user.ln}")
        except Invalid_LoginException as e:
            print(e)


sign_up = SignUp()
sign_in = SignIn(sign_up)
        

        