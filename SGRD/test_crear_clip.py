import os
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver.exe'))
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_navigation_to_form(self):
        self.browser.get('http://localhost:8000/recursos/')
        self.browser.find_element_by_link_text('Detalle').click()
        link = self.browser.find_element_by_link_text('Crear clip')
        self.assertTrue(link.is_displayed())

if __name__ == "__main__":
    unittest.main()
