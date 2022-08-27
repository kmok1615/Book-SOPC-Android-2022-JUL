# coding=UTF-8
'''
Created on 2022.07.07
Author: Ken Mok
'''
# -*- coding: utf-8 -*-
# pip install PyYAML
import unittest
import os
import yaml
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\hago_testcase\\"

class TestBook(unittest.TestCase):

    def testbook_login(self):
        print("Book Login Start")
        user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
        patient = user_data['patient']
        app_lang = user_data['app_lang']
        font_size = user_data['font_size']

        ## Click HA Go logon text
        print("Click HA Go logon text")
        self.driver.find_element_by_xpath("//*[@text='HA Go logon']").click()
        time.sleep(2)

        ## Select type of Patient
        print("Select type of Patient")
        self.driver.find_element_by_xpath("//*[@text='"+patient+"']").click()
        time.sleep(6)

        ## Click OK
        print("Click OK")
        self.driver.find_element_by_xpath("//*[@text='OK']").click()
        time.sleep(2)

        ## Click App Language
        print("Click App Language")
        self.driver.find_element_by_xpath("//*[@text='"+app_lang+"']").click()
        time.sleep(2)

        ## Select Font Size
        print("Select Font Size")
        self.driver.find_element_by_xpath("//*[@text='"+font_size+"']").click()
        time.sleep(2)

        ## Go to apps landing page
        print("Go to apps landing page")
        self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
        time.sleep(2)

        print("Book Login End")
