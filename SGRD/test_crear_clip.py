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

    def test_create_clip(self):
        self.browser.get('http://localhost:8000/recursos/')
        self.browser.find_element_by_link_text('Detalle').click()
        link = self.browser.find_element_by_link_text('Crear clip')
        self.assertTrue(link.is_displayed())
        link.click()

        name = self.browser.find_element_by_id('nombre')
        name.send_keys('Clip 1')

        time_start = self.browser.find_element_by_id('tiempo_inicio')
        time_start.send_keys(0)

        time_end = self.browser.find_element_by_id('tiempo_fin')
        time_end.send_keys(20)

        button_create_clip = self.browser.find_element_by_id('create_clip')
        button_create_clip.click()

if __name__ == "__main__":
    unittest.main()
