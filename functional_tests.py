from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        #self.browser.get(self.live_server_url)
        self.browser = webdriver.Firefox()
        #browser.get('http://192.168.186.137:8000')

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage

        #self.browser.get('http://192.168.186.137:8000')
        self.browser.get(self.live_server_url)

        self.assertIn('EDA 5', self.browser.title)
        self.fail('Finish the test!')
