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
    """
    verify user
    """
    verify = User.user_exists(userName,password)
    return verify

def generate_usercode():
  '''
  autogenerates usercode
  '''
  gen_code =Credentials.gen_usercode()
  return gen_code

def main():
  print ("Hello and welcome to Password Locker. Please enter your name")
  user_name = input()
  
  print(f"Welcome {user_name},how do you wanna continue")
  print('\n') 
  while True:
    print("Enter one of these short codes to go forward : ca - create an account, lg - to login, ex - to exit, cc - to create your credentials,  del  - to delete your credentials, dc - to display contacts, ex - to exit")
    
    short_code = input().lower()
    
    if short_code == 'ca':
          print("New User")
          print("-"*10)
          print ("create username")
          created_username = input()
          
          print ("create password")
          created_password = input ()
          
          print ("confirm password")
          confirm_password = input()
          
          if created_password == confirm_password :
            
            save_user(create_user(created_username, created_password))
            print(f"New_User")
            
            print(f"Account for {created_username} successfully created. Proceed to Login using lg shortcode")
            

          else:
            print ("invalid username or password")
            
    elif short_code == 'lg':
            print("Enter your Username and password below")
            print("Username")
            entered_username = input()
            print("Password")
            entered_password = input()
            user_verified = check_existing_user(entered_username,entered_password)
            
            if entered_username == user_verified :
              print(f"Karibu {entered_username} to your account. Please select one of these short codes to go on : cc - to create your credentials,  del  - to delete your credentials, dc - to display contacts, ex - to exit") 
            
            else:
              print ("try again later") 
     
                
    elif  short_code == 'cc':
          print("Enter the account whose password you want to save")
          created_account =input()
          
          print("Enter account User_id")
          account_user_id = input ()
          while True:
          
                  print("enter account password or choose to have it generated for you 'ep' : to enter password, 'gp' : to have it generated")
                  account_passcode_choice = input()
                  if account_usercode_choice == 'ep':
                      usercode = input('Enter usercode: ')
                      break
                    
                  elif account_passcode_choice == 'gp':
                      usercode = generate_usercode()
                      break
                    
                    
            

