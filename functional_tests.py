from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
		
# A user can enter a To-do items
        self.assertEqual(
            inputbox.get.attribute('placeholder'),
                'Enter a to-do item'
        )
            
# Let her enter "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
	
# Upon entry, page updates and the page lists:
# 1: Buy peacock feathers" as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
	
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
	
# There is another text box awaiting further items
# She enters "Use peacock feathers to make a fly"
        self.fail('Finish the Test!')
	
# page updates again

# site generates unique url for saved to-do list

# returning to the unique url gets the saved to do list

# satisfied, our user goes to sleep

if __name__ == '__main__':
    unittest.main(warnings= 'ignore')