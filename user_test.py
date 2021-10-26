import unittest
from user import User

class TestUser(unittest.TestCase):
  """
  defines test cases
  """
  def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User() 


  def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"morrison")
        self.assertEqual(self.new_user.password,"5430")


  def test_save_user(self):
        '''
        test_save_user test case to test if the contact object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

        def test_account_exist(self):
          self.new_user.save_user()
          test_user =User("charles","wayhome")
          test_user.save_user
          user_exists -User.user_exists("charles")

          self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
