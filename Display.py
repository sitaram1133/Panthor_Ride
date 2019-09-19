
from user import User
class Display:
    def Login_Screen(self):
        global x, y


        print("Welcome to E-Bicycle")
        x = input("Username:")
        y = input("Password:")


    def Validate(self, name=None, age=None, weight=None, height=None, username = None, password = None):

        if(x != None and  y != None):
            obj = User()
            obj._check_(x, y)


        else:
            print('Please enter usr and password')
start = Display()
start.Login_Screen()
start.Validate()

