import os
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver.exe'))
        # self.browser = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver'))
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

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
        time_start.send_keys(10)

        time_end = self.browser.find_element_by_id('id_final')
        time_end.send_keys(20)

        self.browser.find_element_by_xpath("//select/option[1]").click()

        button_create_clip = self.browser.find_element_by_id('create_clip')
        button_create_clip.click()

        h5 = self.browser.find_element(By.XPATH, '//h5[text()="Archivos asociados"]')
        self.assertIn('Archivos asociados', h5.text)

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


if __name__ == "__main__":
    unittest.main()
