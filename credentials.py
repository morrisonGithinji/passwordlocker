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

    """
    function to generate password
    """

    def gen-usercode(size=7) :
        usercode = string.ascii_uppercase + string.ascii_lowercase + string.digits
        gen_pass = ''.join(random.choice(usercode) for i in range(size))
        returm gen_pass



  