import string
import random

class Credentials:
  """
  class having user credentials
  """
  credentials_list=[]
  def __init__(self,account,user_id,passcode):
    self.account =account
    self.user =user
    self.passcode =passcode

    def save_credentials(self) :
    
      """
      save user credentials in the credential list
      """
      Credentials.credentials_list.append(self)

    def delete_credentials(self) :
      """
      removes user credentials from the list
      """
      Credentials.credentials_list.remove(self)

      """
      function to generate password
      """

    def gen_passcode(size=7) :
        passcode = string.ascii_uppercase + string.ascii_lowercase + string.digits
        gen_pass = ''.join(random.choice(usercode) for i in range(size))
        return gen_pass

        @classmethod
        def display_credentials(cls):
           """
           displays credentials list
           """
           return  cls.credentials_list


        @classmethod

        def find_by_account(cls,account):
          """
          displays credentials associated with account
          """

          for credentials in cls.credentials_list:
            if credentials.account ==account:
              return credentials



  