class User :
  """
  class for initiating new users
  """
  user_list=[]

def __init__(self, user_name,password):
  self.userName = user_name
  self.password =password

  def save_user(self):
    """
    saves user in the user_list
    """
    User.user_list.append(self)

  @classmethod
  def user_exists(cls,user_name,password):
    default_user =""
    for user in cls.user_list:
      if user.user_name ==user_name and user.password ==password:
        default_user =user.user_name
        return default_user