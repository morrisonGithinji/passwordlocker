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