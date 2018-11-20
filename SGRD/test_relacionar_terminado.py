from unittest import TestCase
from selenium import webdriver
from django.test import TestCase
from .models.archivo import Archivo
from selenium.webdriver.common.by import By
import os

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('D:/chromedriver.exe')
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000/recurso/1')
        self.assertIn('Recurso ', self.browser.title)

    def test_string_representation(self):
        entry = Archivo(descripcion="descripcion de prueba")
        self.assertEqual(str(entry), entry.descripcion)
