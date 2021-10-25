import string
import random

class Credentials:
  """
  class having user credentials
  """
  credentials_list=[]
  def __init__(self,account,user_id,usercode):
    self.account =account
    self.user =user
    self.usercode =usercode

    def save_credentials(self)
    """
    save user credentials in the credential list
    """
    Credentials.credentials_list.append(self)

    def delete_credentials(self)
    """
    removes user credentials from the list
    """
    Credentials.credentials_list.remove(self)

  