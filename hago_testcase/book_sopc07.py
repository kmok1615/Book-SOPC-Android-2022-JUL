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

class TestBookSOPC07(unittest.TestCase):

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

    def testbooksopc0700(self):
        try:
            print("Book SOPC07-00 Service Guide start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            service_guide_button = user_data['service_guide_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Open external web browser to webpage of Service Guide
            print("Book SOPC07-00 Scenario 01 Open external web browser to webpage of Service Guide")
            print("Click Service Guide Button")
            self.driver.save_screenshot(test_dir+"07_00_Click_Service_Guide_button.png")
            print("Screenshot 07_00_Click_Service_Guide_button is taken")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+service_guide_button+"']]").click()
            time.sleep(8)

            ## External web browser to webpage of Service Guide is opened
            print("External web browser to webpage of Service Guide is opened")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"07_00_Service_Guide_webpage.png")
            print("Screenshot 07_00_Service_Guide_webpage is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC07-00 Service Guide Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC07-00 Service Guide Exception")
            assert(False)
        finally:
            print("Book SOPC07-00 Service Guide finish")

    def tearDown(self):
        self.driver.quit()