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
        self.new_user = User("morrison","5430") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.userName,"morrison")
        self.assertEqual(self.new_user.password,"5430")
       


if __name__ == '__main__':
    unittest.main()
