from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # a user can locate, Get and Display Homepage 
        self.browser.get('http://localhost:8000')
        # Make sure home page loads and is correct one
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# A user can enter a To-do items

# Let her enter "Buy peacock feathers" into a text box

# Upon entry, page updates and the page lists:
# 1: Buy peacock feathers" as an item in the to-do list

# There is another text box awaiting further items
# She enters "Use peacock feathers to make a fly"

# page updates again

# site generates unique url for saved to-do list

# returning to the unique url gets the saved to do list

# satisfied, our user goes to sleep

if __name__ == '__main__':
    unittest.main(warnings= 'ignore')