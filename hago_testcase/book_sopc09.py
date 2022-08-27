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

class TestBookSOPC09(unittest.TestCase):

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

    def testbooksopc0900(self):
        try:
            print("Book SOPC09-00 Select Specialty/Hospital in English")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            patient = user_data['patient']
            font_size = user_data['font_size']
            app_lang = 'ENGLISH'
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_self_button = user_data['book_for_self_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]

            ## Log in in English
            ## Click HA Go logon text
            print("Click HA Go logon text")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='HA Go logon']")))
            self.driver.find_element_by_xpath("//*[@text='HA Go logon']").click()
            time.sleep(2)

            ## Select type of Patient
            print("Select type of Patient")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+patient+"']")))
            self.driver.find_element_by_xpath("//*[@text='"+patient+"']").click()
            time.sleep(6)

            ## Click OK
            print("Click OK")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='OK']")))
            self.driver.find_element_by_xpath("//*[@text='OK']").click()
            time.sleep(2)

            ## Click English as App Language
            print("Click English as App Language")
            self.driver.find_element_by_xpath("//*[@text='ENGLISH']").click()
            time.sleep(2)

            ## Select Font Size
            print("Select Font Size")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+font_size+"']")))
            self.driver.find_element_by_xpath("//*[@text='"+font_size+"']").click()
            time.sleep(2)

            ## Go to apps landing page
            print("Go to apps landing page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='Go to apps landing page']")))
            self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
            time.sleep(2)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click HA Go logon text
            print("Click HA Go logon text")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]").click()
            time.sleep(2)

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start Application
            print("Click Continue button to start Application")
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            time.sleep(4)

            ## Check if the options for selecting Specialty are relevant between Chinese and English
            print("Book SOPC09_00 Scenario 01 Check if the options for selecting Specialty are relevant between Chinese and English")
            self.driver.save_screenshot(test_dir+"09_00_Specialty_in_English.png")
            print("Screenshot 09_00_Specialty_in_English is taken")
            time.sleep(2)

            ## Select any option of Specialty
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()
            time.sleep(2)

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()

            ## Check if the options for selecting Hospital are relevant between Chinese and English
            print("Book SOPC09_00 Scenario 02 Check if the options for selecting Hospital are relevant between Chinese and English")
            self.driver.save_screenshot(test_dir+"09_00_Hospital_in_English.png")
            print("Screenshot 09_00_Hospital_in_English is taken")
            time.sleep(2)

            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC09-00 Select Specialty/Hospital in English Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC09-00 Select Specialty/Hospital in English Exception")
            assert(False)
        finally:
            print("Book SOPC09-00 Select Specialty/Hospital in English finish")

    def testbooksopc0901(self):
        try:
            print("Book SOPC09-01 Review Details Input in English")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            patient = user_data['patient']
            font_size = user_data['font_size']
            app_lang = 'ENGLISH'
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_self_button = user_data['book_for_self_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            Photo_OK_button = user_data['Photo_OK_button'][app_lang]
            patient_address = user_data['patient_address'][app_lang]

            ## Log in in English
            ## Click HA Go logon text
            print("Click HA Go logon text")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='HA Go logon']")))
            self.driver.find_element_by_xpath("//*[@text='HA Go logon']").click()
            time.sleep(2)

            ## Select type of Patient
            print("Select type of Patient")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+patient+"']")))
            self.driver.find_element_by_xpath("//*[@text='"+patient+"']").click()
            time.sleep(6)

            ## Click OK
            print("Click OK")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='OK']")))
            self.driver.find_element_by_xpath("//*[@text='OK']").click()
            time.sleep(2)

            ## Click English as App Language
            print("Click English as App Language")
            self.driver.find_element_by_xpath("//*[@text='ENGLISH']").click()
            time.sleep(2)

            ## Select Font Size
            print("Select Font Size")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+font_size+"']")))
            self.driver.find_element_by_xpath("//*[@text='"+font_size+"']").click()
            time.sleep(2)

            ## Go to apps landing page
            print("Go to apps landing page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='Go to apps landing page']")))
            self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
            time.sleep(2)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click HA Go logon text
            print("Click HA Go logon text")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]").click()
            time.sleep(2)

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start Application
            print("Click Continue button to start Application")
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            time.sleep(4)

            ## Select any option of Specialty
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()
            time.sleep(2)

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            time.sleep(2)

            ## Select any option of Hospital
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()
            time.sleep(2)

            ## Click Next Button to go to next screen
            print("Click Next Button to go to next screen")
            time.sleep(2)

            ## Click Next Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()

            ## Submit Document screen is shown
            print("Submit Document screen is shown")
            time.sleep(2)

            ## Tap Type in Patient's Address icon in Submit Document page
            self.driver.find_element_by_xpath("xpath=((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[2]").click()
            time.sleep(2)

            ## Input Patient's address
            self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.EditText']").send_keys(patient_address)
            time.sleep(2)
            self.driver.hide_keyboard
            time.sleep(2)
            
            ## Click Next to go next page
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on Referral letter
            print("User is on Referral letter screen")
            time.sleep(2)

            ## Click Photo-taking on referral letter page
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup").click()
            time.sleep(2)

            ## Tap on Photo icon to take 1st photo
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[6]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[6]").click()
            time.sleep(3)

            ## User is on Photo interface screen
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]")))
            self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(3)

            ## Confirm photo taken
            print("Confirm photo taken")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Photo_OK_button+"']]").click()
            time.sleep(2)

            ## Swipe down to show Next button to click and enter Check Data screen
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Check if the information displayed in Patient's Detail page are relevant between Chinese and English
            print("Book SOPC09-01 Scenario 01 Check if the information displayed in Patient's Detail page are relevant between Chinese and English")
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"09_01_check_data_in_English_01.png")
            print("Screenshot 09_01_check_data_in_English_01 is taken")
            time.sleep(2)

            ## Swipe down to show Please click here to check link
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"09_01_check_data_in_English_01.png")
            print("Screenshot 09_01_check_data_in_English_01 is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC09-01 Select Specialty/Hospital in English Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC09-01 Select Specialty/Hospital in English Exception")
            assert(False)
        finally:
            print("Book SOPC09-01 Select Specialty/Hospital in English finish")

    def tearDown(self):
        self.driver.quit()