from user import User
from credentials import Credentials

def create_user(userName,password):
   """
  creating a new password locker account.
  """
  new_user =User(userName,password)
  return new_user

def save_user(user):
     """
     save user
     """
     user.save_user()

def create_credentials(account,user_id,usercode):
    """
    creating user credentials
    """
    new_credentials=Credentials(account,user_id,usercode)
    return new_credentials

def save_credentials(credentials):
    """
    save credentials
    """
    credentials.save_credentials()   

def delete_credentials(credentials):
    """
    to delete credentials
    """
    credentials.delete_credentials()

def display_credentials(credentials):
    """
    reveals user credentials
    """
    return Credentials.display_credentials()

def find_account(account):  
    """"
    finds account
    """
    return Credentials.find_by_account(account)

def check_existing_user(userName, password):
    verify = User.user_exists(userName,password)
    return verify