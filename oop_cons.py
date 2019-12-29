class User:
    name = ''
    email = ''
    password = ''
    login = 'False'  
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def login(self):
        email = input("Enter email: ")
        password = input("Enter Password: ")
        
        if email == self.email and password == self.password:
            login = True
            print("Login Successful!")
        else:
            print("Login Faild!")            
    def logout(self):
        login = False
        print("Logged Out!")        
    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False    
    def profile(self):
        if self.isLoggedIn():
            print(self.name,"\n",self.email)
        else:
            print("User is not Logged in!")
user1 = User('Kishor', 'kishorkm5@gmail.com', '1234')

user1.login()
user1.profile()
hello = input()


    
        