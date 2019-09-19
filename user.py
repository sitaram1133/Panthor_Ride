import json
from system_en import Mains
from session import Session
class User:


    def __init__(self, name="Shivay", age=None, weight=None, height=None, username="Shivay", password="99999"):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.username = username
        self.password = password

    def get(self):
        return self.name, self.age, self.weight, self.height, self.username, self.password

    def set(self, name):
        self.name = name

    def set(self, age):
        self.age = age

    def set(self, weight):
        self.weight = weight

    def set(self, height):
        self.height = height

    def set(self, username):
        self.username = username

    def set(self, password):
        self.password = password

    def __delete__(self):
        del self.name
        del self.age
        del self.weight
        del self.height
        del self.username
        del self.password

    def _check_(self, username, password, id_no=None):
        if(self.username == username):
            self.username = True
            if(self.password == password):
                self.password = True
                if(self.username==True and self.password==True):
                    print("Login Succesful")
                    call = Session()
                    call.check(session_ID= id_no)
                    id_no = 21


            else:
                self.password = False
        else:
            self.username = False
            print("Invalid Username and Password")




