# coding=utf-8
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

"""
Tests de la funcionalidad de editar entradas de plan de producción
"""
class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    """
    Comprobar el título de la página en editar entrada
    """
    def test_title(self):
        self.browser.get('http://localhost:8000/editar-entrada/1')
        self.assertIn('Editar Entrada', self.browser.title)

    """
    Se puede editar las personas y guardar
    """
    def test_edit(self):
        self.browser.get('http://localhost:8000/editar-entrada/1')
        nombre = self.browser.find_element_by_id('id_personas')
        nombre.clear()
        nombre.send_keys('Juan Daniel')
        botonGrabar = self.browser.find_element_by_id('id_guardar')
        botonGrabar.click()