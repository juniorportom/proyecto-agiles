# coding=utf-8
import os
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Tests de la funcionalidad de crear clip de un archivo de video
"""
class FunctionalTest(TestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver.exe'))
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    """
    Test: Existen archivos de tipo video, se puede entrar en detalle y se muestra el botón de crear clip
    """
    def test_navigation_to_form(self):
        self.browser.get('http://localhost:8000/recursos/')
        lista = self.browser.find_elements_by_id('id_type')
        if lista:
            for item in lista:
                if item.text == 'Tipo: Video':
                    parent_element = item.find_element_by_xpath('../../..')
                    parent_element.find_element_by_link_text('Detalle').click()
                    break
            link = self.browser.find_element_by_link_text('Crear clip')
            self.assertTrue(link.is_displayed())

    """
    Test: crear un clip en video
    """
    def test_create_clip(self):
        self.browser.get('http://localhost:8000/recursos/')
        lista = self.browser.find_elements_by_id('id_type')
        if lista:
            for item in lista:
                if item.text == 'Tipo: Video':
                    parent_element = item.find_element_by_xpath('../../..')
                    parent_element.find_element_by_link_text('Detalle').click()
                    break
            link = self.browser.find_element_by_link_text('Crear clip')
            self.assertTrue(link.is_displayed())
        link.click()

        name = self.browser.find_element_by_id('id_nombre')
        name.send_keys('Clip 10')

        time_start = self.browser.find_element_by_id('id_inicio')
        time_start.clear()
        time_start.send_keys(10)

        time_end = self.browser.find_element_by_id('id_final')
        time_end.clear()
        time_end.send_keys(20)

        self.browser.find_element_by_xpath("//select/option[1]").click()

        button_create_clip = self.browser.find_element_by_id('create_clip')
        button_create_clip.click()

        h5 = self.browser.find_element(By.XPATH, '//h5[text()="Etiquetas:"]')
        self.assertIn('Etiquetas:', h5.text)

    """
    Test: no se muestra crear clip en recursos que no son videos
    """
    def test_create_clip_no_video(self):
        self.browser.get('http://localhost:8000/recursos/')

        lista = self.browser.find_elements_by_id('id_type')
        if lista:
            for item in lista:
                if item.text != 'Tipo: Video':
                    parent_element = item.find_element_by_xpath('../../..')
                    parent_element.find_element_by_link_text('Detalle').click()
                    break
            link_list = self.browser.find_element_by_id('id_links')
            self.assertNotEqual(link_list.text, 'Adjuntar Archivo | Crear plan | Crear clip')

    """
    Test: No permite creación de clip sin nombre
    """
    def test_create_clip_vacio(self):
        self.browser.get('http://localhost:8000/recursos/')
        lista = self.browser.find_elements_by_id('id_type')
        if lista:
            for item in lista:
                if item.text == 'Tipo: Video':
                    parent_element = item.find_element_by_xpath('../../..')
                    parent_element.find_element_by_link_text('Detalle').click()
                    break
            link = self.browser.find_element_by_link_text('Crear clip')
            self.assertTrue(link.is_displayed())
            link.click()

            button_create_clip = self.browser.find_element_by_id('create_clip')
            button_create_clip.click()

            li = self.browser.find_element(By.XPATH, '//li[text()="Campo Nombre obligatorio"]')
            self.assertIn('Campo Nombre obligatorio', li.text)

    """
    Test: No permite un clip con tiempo final menor al inicial
    """
    def test_create_clip_tiempo_final_menor(self):
        self.browser.get('http://localhost:8000/recursos/')
        lista = self.browser.find_elements_by_id('id_type')
        if lista:
            for item in lista:
                if item.text == 'Tipo: Video':
                    parent_element = item.find_element_by_xpath('../../..')
                    parent_element.find_element_by_link_text('Detalle').click()
                    break
            link = self.browser.find_element_by_link_text('Crear clip')
            self.assertTrue(link.is_displayed())
            link.click()

            name = self.browser.find_element_by_id('id_nombre')
            name.send_keys('Clip 10')

            time_start = self.browser.find_element_by_id('id_inicio')
            time_start.clear()
            time_start.send_keys(30)

            time_end = self.browser.find_element_by_id('id_final')
            time_end.clear()
            time_end.send_keys(20)

            self.browser.find_element_by_xpath("//select/option[1]").click()

            button_create_clip = self.browser.find_element_by_id('create_clip')
            button_create_clip.click()

            li = self.browser.find_element(By.XPATH, '//li[text()="Tiempo final debe ser mayor al tiempo inicial"]')
            self.assertIn('Tiempo final debe ser mayor al tiempo inicial', li.text)


if __name__ == "__main__":
    unittest.main()
