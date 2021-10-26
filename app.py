from user import User
from credentials import Credentials

def create_user(userName,password):
  """
  creating a new password locker account.
  """
  new_user =User(userName,password)
  return new_user