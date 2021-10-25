class User :
"""
class for initiating new users
"""
user_list[]

def __init__(self, userName,password):
  self.userName = userName
  self.password =password

  def save_user(self)
  """
  saves user in the user_list
  """
  User.user_list.append(self)

  @classmethod
  def user-exists(cls,userName),password:
    default_user =""
    for user in cls.user_list:
      if user.userName ==userName and user.password ==password:
        default_user =user.userName
        return default_user