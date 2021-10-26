import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
  
  def setUp(self):
    
    
    self.new_credentials = Credentials("twitter","morris","sirrom")
  def tearDown(self):  
    Credentials.credentials_list=[]  
      
  def test_init(self):
    '''
    tests if the object is initialized properly
    '''
    self.assertEqual(self.new_credentials.account, "twitter")  
    self.assertEqual(self.new_credentials.user_id, "morris")
    self.assertEqual(self.new_credentials.passcode, "sirrom")
    
  def test_save_credentials(self):
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)
    
  def test_save_multiple_credentials(self)  :
    self.new_credentials.save_credentials()
    test_credentials = Credentials("twitter","peter","cdjnjnd")
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),2)
      
  def test_delete_credentials(self):
    '''
    test if we  can remove credentials from our list
    '''
    self.new_credentials.save_credentials()
    test_credentials = Credentials("twitter","peter","cdjnjnd")
    test_credentials.save_credentials()
    self.new_credentials.delete_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)
    
  def test_display_credentials (self):
    '''
    to display the list of all credentials a user may have
    '''
    self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    
  def find_credentials_by_account(self):
    '''
    to check existence of credentials
    '''
    self.new_credentials.save_credentials("twitter","peter","cdjnjnd")
    test_credentials =  Credentials()
    test_credentials.save_credentials
    found_credential = Credentials.find_by_account("twitter")
    
    self.assertEqual(found_credential.user_id,test_credentials.user_id)
    
    
    
  
if __name__=='__main__':
  unittest.main()    
