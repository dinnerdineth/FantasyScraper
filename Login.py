#accept login details

import getpass


# class Book:
#   def __init__(self, title, price, author=None):
#     self.title = title
#     self.price = price

class Login:
  def __init__(self,username,password):
    self.username = username
    self.password = password
    

def get_login():
  username = input("E-mail:\n")
  pw = getpass.getpass()
  login_details = Login(username,pw)
  return login_details

  
#Debugging
#login = get_login()