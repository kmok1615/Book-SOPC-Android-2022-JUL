# coding=UTF-8
'''
Created on 2022.07.07
Updated on 2022.07.21
Author: Ken Mok
'''
# -*- coding: utf-8 -*-
# pip install PyYAML

from ast import AsyncFunctionDef
import unittest
import os
import yaml
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

from hago_testcase.book_login import TestBook

test_dir = "./Automation Test/hago_testcase/"
CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\hago_testcase\\"

class TestBookSOPC08(unittest.TestCase):

    def setUp(self):
        conf = yaml.load(open(CONF_PATH + 'config.yml'), Loader=yaml.FullLoader)
        desired_caps={}
        desired_caps['platformName'] = conf['platformName']
        desired_caps['platformVersion'] = conf['platformVersion']
        desired_caps['deviceName'] = conf['deviceName']
        desired_caps['udid'] = conf['udid']
        desired_caps['appPackage'] = conf['appPackage']
        desired_caps['appActivity'] = conf['appActivity']
        self.driver = webdriver.Remote(conf['driver'], desired_caps)

    def testbooksopc0800(self):
        try:
            print("Book SOPC08-00 FAQ start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            faq_link = user_data['faq_link'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Open external web browser to webpage of FAQ
            print("Book SOPC08-00 Scenario 01 Open external web browser to webpage of FAQ")
            print("Click Frequently Asked Questions")
            self.driver.save_screenshot(test_dir+"08_00_Click_FAQ_link.png")
            print("Screenshot 08_00_Click_FAQ_link is taken")
            time.sleep(2)
            self.driver.find_element_by_link_text(faq_link).click()
            time.sleep(8)

            ## External web browser to webpage of Frequently Asked Questions is opened
            print("External web browser to webpage of Frequently Asked Questions is opened")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"08_00_FAQ_webpage.png")
            print("Screenshot 08_00_FAQ_webpage is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC08-00 FAQ Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC08-00 FAQ Exception")
            assert(False)
        finally:
            print("Book SOPC08-00 FAQ finish")

    def tearDown(self):
        self.driver.quit()