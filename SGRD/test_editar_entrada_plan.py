from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('', self.browser.title)

    def test_title(self):
        self.browser.get('http://localhost:8000/editar-entrada-plan/1')
        self.assertIn('Editar entrada', self.browser.title)