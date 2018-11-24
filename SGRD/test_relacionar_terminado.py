from unittest import TestCase
from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.by import By
import os

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000/recurso/1')
        self.assertIn('Recursos', self.browser.title)

    def test_boton_cargar(self):
        self.browser.get('http://localhost:8000/recurso/1')
        link = self.browser.find_element_by_link_text('Cargar producto final')
        self.assertTrue(link.is_displayed())

    def test_title_cargar(self):
        self.browser.get('http://localhost:8000/crear-archivo/1/1')
        self.assertIn('Crear archivo terminado', self.browser.title)
        btn = self.browser.find_element_by_xpath("//input[@value='Cargar archivo terminado']")
        self.assertTrue(btn.is_displayed())
