# coding=UTF-8
'''
Created on 2022.07.07
Updated on 2022.07.19
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
from selenium.common.exceptions import TimeoutException

from hago_testcase.book_login import TestBook

test_dir = "./Automation Test/hago_testcase/"
CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\hago_testcase\\"

class TestBookSOPC04(unittest.TestCase):

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

    def testbooksopc0400(self):
        try:
            print("Book SOPC04-00 Read Application Notes start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            cancel_button = user_data['cancel_button'][app_lang]

            ## User is not Log in; directly goes to Landing page
            #TestBook.testbook_login(self)
            print("Go to apps landing page without Log in")
            self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click HA Go logon text
            print("Click HA Go logon text")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]").click()
            time.sleep(2)

            ## Click Book for others
            print("Book for others")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]").click()
            time.sleep(2)

            ## Display Declaration pop-up window
            self.driver.save_screenshot(test_dir+"04_00_declaration.png")
            print("Screenshot 04_00_declaration is taken")
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Decide if the patient has received healthcare services from any hospitals / clinics under Hospital Anthority (HA)
            ## Yes in this case
            self.driver.save_screenshot(test_dir+"04_00_yes_received_healthcare_service.png")
            print("Screenshot 04_00_yes_received_healthcare_service is taken")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(2)

            ## Application Notes is shown
            print("Book SOPC04-00 Scenario 01 Application Notes is shown")
            self.driver.save_screenshot(test_dir+"04_00_Application_Notes.png")
            print("Screenshot 04_00_Application_Notes is taken")
            time.sleep(5)

            ## Click scroll icon to scroll down
            print("Book SOPC04-00 Scenario 02 Click scroll icon to scroll down")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            self.driver.save_screenshot(test_dir+"04_00_Application_Notes.png")
            print("Screenshot 04_00_Application_Notes is taken")
            time.sleep(2)

            ## Click Cancel button to close Application Notes
            print("Book SOPC04-00 Scenario 03 Click Cancel button to close Application Notes")
            self.driver.find_element_by_xpath("//*[@text='"+cancel_button+"']").click()
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC04-00 Read Application Notes Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC04-00 Read Application Notes Exception")
            assert(False)
        finally:
            print("Book SOPC04-00 Read Application Notes finish")

    def testbooksopc0401(self):
        try:
            print("Book SOPC04-01 Input Patient's information in application process start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_02_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_04_01']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_04_01']
            patient_surname = user_data['patient_surname_04_01'][app_lang]
            patient_givenname = user_data['patient_givenname_04_01'][app_lang]
            patient_mobilenumber = user_data['patient_mobilenumber_04_01']

            ## User is not Log in; directly goes to Landing page
            #TestBook.testbook_login(self)
            print("Go to apps landing page without Log in")
            self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click HA Go logon text
            print("Click HA Go logon text")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]").click()
            time.sleep(2)

            ## Click Book for others in Submit Application screen
            print("Book for others in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]").click()
            time.sleep(2)

            ## Display Declaration pop-up window
            self.driver.save_screenshot(test_dir+"04_01_declaration.png")
            print("Screenshot 04_01_declaration is taken")
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Decide if the patient has received healthcare services from any hospitals / clinics under Hospital Anthority (HA)
            ## Yes in this case
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## The Progress Bar with 1st icon highlighted is displayed
            print("Book SOPC04-01 Scenario 01 The Progress Bar with 1st icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"04_01_Progress_bar_1st_icon.png")
            print("Screenshot 04_01_Progress_bar_1st_icon is taken")
            time.sleep(2)

            ## Patient's data in 4 input fields: HKID/Birth Certificate, Surname, Given Name, HK mobile phone number are blanked
            print("Book SOPC04_01 Scenario 02 Patient's data in 4 input fields: HKID/Birth Certificate, Surname, Given Name, HK mobile phone number are blank")
            time.sleep(2)

            self.driver.save_screenshot(test_dir+"04_01_Patient_data_blank.png")
            print("Screenshot 04_01_Patient_data_blank is taken")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Input Patient Surname
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_surname)
            time.sleep(2)

            ## Input Patient given name
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[4]").send_keys(patient_givenname)
            time.sleep(2)

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[5]").send_keys(patient_mobilenumber)
            time.sleep(2)

            ## The Patient information is input
            print("The Patient information is input")
            self.driver.save_screenshot(test_dir+"04_01_Patient_data_input.png")
            print("Screenshot 04_01_Patient_data_input is taken")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()
            time.sleep(2)

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()
            time.sleep(2)

            ## The Specialty and Hospital can be input by user
            print("Book SOPC04_01 Scenario 03 The Specialty and Hospital can be input by user")
            self.driver.save_screenshot(test_dir+"04_01_Specialty_Hospital.png")
            print("Screenshot 04_01_Specialty_Hospital is taken")
            time.sleep(2)

            ## Click Next Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()

            ## Click Next Button to go to next screen
            print("Book SOPC04_01 Scenario 04 Click Next Button to go to next screen")
            self.driver.save_screenshot(test_dir+"04_01_Next_Button.png")
            print("Screenshot 04_01_Next_Button is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC04-01 Input Patient's information in application process Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC04-01 Input Patient's information in application process Exception")
            assert(False)
        finally:
            print("Book SOPC04-01 Input Patient's information in application process finish")

    def testbooksopc0402(self):
        try:
            print("Book SOPC04-02 Take Photo in Submit Document page in application process start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            CONFIRM_button = user_data['CONFIRM_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_02_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_02_01']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_02_01']
            patient_surname = user_data['patient_surname_02_01'][app_lang]
            patient_givenname = user_data['patient_givenname_02_01'][app_lang]
            patient_mobilenumber = user_data['patient_mobilenumber_02_01']
            patient_address = user_data['patient_address_02_01'][app_lang]

            ## User is not Log in; directly goes to Landing page
            #TestBook.testbook_login(self)
            print("Go to apps landing page without Log in")
            self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click HA Go logon text
            print("Click HA Go logon text")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]").click()
            time.sleep(2)

            ## Click Book for others in Submit Application screen
            print("Book for others in Submit Application screen")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Decide if the patient has received healthcare services from any hospitals / clinics under Hospital Anthority (HA)
            ## Yes in this case
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## The Progress Bar with 1st icon highlighted is displayed
            print("Book SOPC04-01 Scenario 01 The Progress Bar with 1st icon highlighted is displayed")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Input Patient Surname
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_surname)
            time.sleep(2)

            ## Input Patient given name
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[4]").send_keys(patient_givenname)
            time.sleep(2)

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[5]").send_keys(patient_mobilenumber)
            time.sleep(2)

            ## The Patient information is input
            print("The Patient information is input")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Click Next Button to remove cursor
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()
            time.sleep(2)

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()
            time.sleep(2)

            ## Click Next Button to go to next page
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Submit Document screen is shown
            print("Submit Document screen is shown")
            time.sleep(2)

            ## The Progress Bar with 2nd icon highlighted is displayed
            print("Book SOPC04-02 Scenario 01 The Progress Bar with 2nd icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"04-02_Progress_bar_2nd_icon.png")
            print("Screenshot 04-02_Progress_bar_2nd_icon is taken")
            time.sleep(2)

            ## Take Photo in Submit Document page
            print("Take Photo in Submit Document page")

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            ## Functions of buttons of taking photo and inputing address
            print("Book SOPC04-02 Scenario 02 Functions of buttons of taking photo and inputing address")
            self.driver.save_screenshot(test_dir+"04-02_take_photo_interface.png")
            print("Screenshot 04-02_take_photo_interface is taken")
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Display of Photo interface pages for taking photo of Patient's Address
            print("Book SOPC04-02 Scenario 03 Display of Photo interface pages for taking photo of Patient's Address")
            self.driver.save_screenshot(test_dir+"04-02_take_photo_document_done.png")
            print("Screenshot 04-02_take_photo_document_done is taken")
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+OK_button+"']").click()
            time.sleep(3)

            ## Change outlook of icons in Patient's Address after the process of Take Photo
            print("Book SOPC04-02 Scenario 04 Change outlook of icons in Patient's Address after the process of Take Photo")
            self.driver.save_screenshot(test_dir+"04-02_patient_address_after_taking_photo_document.png")
            print("Screenshot 04-02_patient_address_after_taking_photo_document is taken")
            time.sleep(2)

            ## Type In Patient's Address
            print("Book SOPC04-02 Type In Patient's Address")

            ## Delete Photo in Submit Document page in application process
            print("Click delete button")
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]]").click()
            time.sleep(4)

            ## Click CONFIRM to confirm delete photo
            print("Click CONFIRM to confirm delete photo")
            self.driver.find_element_by_xpath("//*[@text='"+CONFIRM_button+"']").click()
            time.sleep(2)

            ## Type in Patient's Address in Submit Document page in application process
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[2]").click()
            time.sleep(2)
            print("Book SOPC04-02 Scenario 05 Change of interface when clicking 'Pen' button")
            self.driver.save_screenshot(test_dir+"04_02_typing_patient_address_box.png")
            print("Screenshot 04_02_typing_patient_address_box is taken")
            time.sleep(2)

            ## Input Patient's address
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']").send_keys(patient_address)
            time.sleep(2)
            self.driver.hide_keyboard
            time.sleep(2)
            print("Book SOPC04-02 Scenario 06 Input data to patient's address box")
            self.driver.save_screenshot(test_dir+"04_02_typing_patient_address_box.png")
            print("Screenshot 04_02_typing_patient_address_box is taken")
            
            ## Click Take Photo button to remove cursor
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Click Next Button to go to next screen
            print("Book SOPC04-02 Scenario 07 Click Next Button to go to next screen")
            self.driver.save_screenshot(test_dir+"04_02_Next_Button.png")
            print("Screenshot 04_02_Next_Button is taken")
            time.sleep(2)

            ## Click Next to go next page
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC04-02 Take Photo in Submit Document page in application process Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC04-02 Take Photo in Submit Document page in application process Exception")
            assert(False)
        finally:
            print("Book SOPC04-02 Take Photo in Submit Document page in application process finish")

    def testbooksopc0403(self):
        try:
            print("Book SOPC04-03 Scanning QR code on Referral letter start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_04_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_04_01']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_04_01']
            patient_surname = user_data['patient_surname_04_01'][app_lang]
            patient_givenname = user_data['patient_givenname_04_01'][app_lang]
            patient_mobilenumber = user_data['patient_mobilenumber_04_01']
            scan_qr_code_user_guide_text = user_data['scan_qr_code_user_guide_text'][app_lang]

            ## User is not Log in; directly goes to Landing page
            #TestBook.testbook_login(self)
            print("Go to apps landing page without Log in")
            self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click HA Go logon text
            print("Click HA Go logon text")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]").click()
            time.sleep(2)

            ## Click Book for others in Submit Application screen
            print("Book for others in Submit Application screen")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Decide if the patient has received healthcare services from any hospitals / clinics under Hospital Anthority (HA)
            ## Yes in this case
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Input Patient Surname
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_surname)
            time.sleep(2)

            ## Input Patient given name
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[4]").send_keys(patient_givenname)
            time.sleep(2)

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[5]").send_keys(patient_mobilenumber)
            time.sleep(2)

            ## The Patient information is input
            print("The Patient information is input")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Click Next Button to remove cursor
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()
            time.sleep(2)

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()
            time.sleep(2)

            ## Click Next Button to go to next page
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Submit Document screen is shown
            print("Submit Document screen is shown")
            time.sleep(2)

            ## Take Photo in Submit Document page
            print("Take Photo in Submit Document page")

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+OK_button+"']").click()
            time.sleep(3)

            ## Click Next to go next page
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on Referral letter
            print("User is on Referral letter screen")
            time.sleep(2)

            ## The Progress Bar with 3rd icon highlighted is displayed
            print("Book SOPC04-03 Scenario 01 The Progress Bar with 3rd icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"04_03_Progress_bar_3rd_icon.png")
            print("Screenshot 04_03_Progress_bar_3rd_icon is taken")
            time.sleep(2)

            ## Screen of scanning QR code
            print("Book SOPC04-03 Scenario 02 Screen of scanning QR code")
            time.sleep(2)

            ## Click User Guide link
            print("Click User Guide link")
            self.driver.find_element_by_xpath("xpath=//*[@text='"+scan_qr_code_user_guide_text+"']").click()
            time.sleep(2)

            ## User Guide in scanning QR code on Referral letter
            print("Book SOPC04-03 Scenario 03 Read User Guide in scanning QR code of Referral letter")
            self.driver.save_screenshot(test_dir+"04_03_User_guide_scanning_qr_code_referral_letter.png")
            print("Screenshot 04_03_User_guide_scanning_qr_code_referral_letter is taken")
            time.sleep(2)

            ## Close User Guide pop-up
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ScrollView']]]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ScrollView']]]").click()
            time.sleep(2)
            print("User Guide in scanning QR code on Referral letter is closed")
            self.driver.save_screenshot(test_dir+"04_03_user_guide_closed.png")
            print("Screenshot 04_03_user_guide_closed is taken")

            ## Wait 20 seconds for manually scanning invalid QR code
            print("Book SOPC04-03 Scenario 04 Process when displayed pop-up of scanning QR code failed")
            time.sleep(2)
            print("Invalid QR code is scanned")
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            self.driver.save_screenshot(test_dir+"04_03_invalid_QR_code.png")
            print("Screenshot 04_03_invalid_QR_code is taken")

            ## Clicked Re-scan button
            self.driver.find_element_by_xpath("//*[@id='button1']").click()
            time.sleep(2)
            print("Clicked Re-scan button")
            self.driver.save_screenshot(test_dir+"04_03_rescan_QR_code.png")
            print("Screenshot 04_03_rescan_QR_code is taken")

            ## Wait 20 seconds for manually scanning QR code with unmatched HKID
            time.sleep(2)
            print("QR code with unmatched HKID is scanned")
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            self.driver.save_screenshot(test_dir+"04_03_unmatched_HKID_QR_code.png")
            print("Screenshot 04_03_unmatched_HKID_QR_code is taken")

            ## Clicked Re-input button to go back input data screen
            self.driver.find_element_by_xpath("//*[@id='button2']").click()
            time.sleep(2)
            print("Clicked Re-input button to go back input data screen")

            ## Re-input HKID/HK Birth Certificate number 
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_02_03']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_02_03']

            ## Clear HKID digits and re-input
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").clear()
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)

            ## Clear HKID last digit and re-input
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Re-input HKID/HK Birth Certificate number in input data screen
            print("Re-input HKID/HK Birth Certificate number in input data screen")
            self.driver.save_screenshot(test_dir+"04_03_reinput_HKID.png")
            print("Screenshot 04_03_reinput_HKID is taken")

            ## Click section Title to remove cursor
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Click Next Button to go to next screen
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Click Next Button to go to next screen
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Wait 20 seconds for manually scanning QR code with unmatched Speciality
            time.sleep(2)
            print("QR code with unmatched Speciality is scanned")
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            self.driver.save_screenshot(test_dir+"04_03_unmatched_Speciality_QR_code.png")
            print("Screenshot 04_03_unmatched_Speciality_QR_code is taken")

            ## Clicked Re-select button to go back input data screen
            self.driver.find_element_by_xpath("//*[@id='button2']").click()
            time.sleep(2)
            print("Clicked Re-select button to go back input data screen")

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Re-input specialty and hospital
            spinner_specialty = user_data['spinner_specialty_02_03'][app_lang]
            spinner_hospital = user_data['spinner_hospital_02_03'][app_lang]

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            time.sleep(2)
            self.driver.execute_script("seetest:client.swipe(\"Up\", 800, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()
            time.sleep(2)

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            time.sleep(2)
            self.driver.execute_script("seetest:client.swipe(\"Up\", 800, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()
            time.sleep(2)

            ## Click Next Button to go to next page
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Click Next Button to go to next screen
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Click YES button to confirm re-scan
            print("Click YES button to confirm re-scan")
            self.driver.find_element_by_xpath("//*[@id='button1']").click()
            time.sleep(2)

            ## Wait 20 seconds for manually scanning valid QR code
            print("Book SOPC04-03 Scenario 04 Process when displayed pop-up of scanning QR code success")
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            time.sleep(2)
            print("QR code is scanned successfully")
            self.driver.save_screenshot(test_dir+"04_03_valid_QR_code_scanned.png")
            print("Screenshot 04_03_valid_QR_code_scanned is taken")
            time.sleep(2)

            ## Clicked Close button to go Check data page
            self.driver.find_element_by_xpath("//*[@id='button1']").click()
            time.sleep(5)

            ## User is on check data page
            print("Book SOPC04-03 Scenario 05 Display of information of patient in patient information screen")
            print("User is on check data page which shows information of patient")
            self.driver.save_screenshot(test_dir+"04_03_check_data_page_from_QR_code_scanned.png")
            print("Screenshot 04_03_check_data_page_from_QR_code_scanned is taken")
            time.sleep(3)

        except TimeoutException:
            print("Book SOPC04-03 Scanning QR code on Referral letter Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC04-03 Scanning QR code on Referral letter Exception")
            assert(False)
        finally:
            print("Book SOPC04-03 Scanning QR code on Referral letter finish")

    def testbooksopc040301(self):
        try:
            print("Book SOPC04-03-01 Take Photo in other Referral letter in application process start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_02_03']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_02_03']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_02_03']
            patient_surname = user_data['patient_surname_02_03'][app_lang]
            patient_givenname = user_data['patient_givenname_02_03'][app_lang]
            patient_mobilenumber = user_data['patient_mobilenumber_02_03']
            Photo_OK_button = user_data['Photo_OK_button'][app_lang]

            ## User is not Log in; directly goes to Landing page
            #TestBook.testbook_login(self)
            print("Go to apps landing page without Log in")
            self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click HA Go logon text
            print("Click HA Go logon text")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]").click()
            time.sleep(2)

            ## Click Book for others in Submit Application screen
            print("Book for others in Submit Application screen")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Decide if the patient has received healthcare services from any hospitals / clinics under Hospital Anthority (HA)
            ## Yes in this case
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Input Patient Surname
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_surname)
            time.sleep(2)

            ## Input Patient given name
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[4]").send_keys(patient_givenname)
            time.sleep(2)

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[5]").send_keys(patient_mobilenumber)
            time.sleep(2)

            ## The Patient information is input
            print("The Patient information is input")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Click Next Button to remove cursor
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()
            time.sleep(2)

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()
            time.sleep(2)

            ## Click Next Button to go to next page
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Submit Document screen is shown
            print("Submit Document screen is shown")
            time.sleep(2)

            ## Take Photo in Submit Document page
            print("Take Photo in Submit Document page")

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+OK_button+"']").click()
            time.sleep(3)

            ## Click Next to go next page
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on Referral letter
            print("User is on Referral letter screen")
            time.sleep(2)

            ## Click Photo-taking on referral letter page
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup").click()
            time.sleep(2)
            print("Book SOPC04-03-01 Scenario 01 Functions of buttons related to taking photo in other Referral letter")
            self.driver.save_screenshot(test_dir+"04_03_01_take_photo_referral_letter.png")
            print("Screenshot 04_03_01_take_photo_referral_letter is taken")
            time.sleep(2)

            ## Click on Doctor's Referral Letter 1st page referral letter page
            print("Click on Doctor's Referral Letter 1st page referral letter page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup").click()
            time.sleep(2)

            ## User is on Photo interface screen
            print("Book SOPC04-03-01 Scenario 02 Functions of different buttons in Take Photo interface")
            self.driver.save_screenshot(test_dir+"04_03_01_Photo_interface_screen.png")
            print("Screenshot 04_03_01_Photo_interface_screen is taken")
            time.sleep(2)

            ## Take Photo in Photo interface screen
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]")))
            self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(2)

            ## Confirm photo taken
            print("Confirm photo taken")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Photo_OK_button+"']]").click()
            time.sleep(2)

            ## Photo taken is added
            print("Book SOPC04-03-01 Scenario 03 Change outlook of icons in other Referral letter after the process of Take Photo")
            self.driver.save_screenshot(test_dir+"04_03_01_Photo_taken_on_referral_letter_page.png")
            print("Screenshot 04_03_01_Photo_taken_on_referral_letter_page is taken")
            time.sleep(3)

            ## Tap Zoom button
            print("Tap Zoom button to open photo page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[5]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[5]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"04_03_01_Zoom_Photo_taken_page.png")
            print("Screenshot 04_03_01_Zoom_Photo_taken_page is taken")
            time.sleep(2)

            ## Return to Submit Referral letter page
            print("Return to Submit Referral Letter page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text]]]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text]]]").click()
            time.sleep(2)

            ## Swipe down to show Next button to click
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)

            ## Click Next Button to go to next screen
            print("Book SOPC04-03-01 Scenario 04 Next button")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on check data page
            print("User is on check data page which shows information of patient")
            self.driver.save_screenshot(test_dir+"04_03_01_check_data_page_from_QR_code_scanned.png")
            print("Screenshot 04_03_01_check_data_page_from_QR_code_scanned is taken")
            time.sleep(3)

        except TimeoutException:
            print("Book SOPC04-03-01 Take Photo in other Referral letter in application process Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC04-03-01 Take Photo in other Referral letter in application process Exception")
            assert(False)
        finally:
            print("Book SOPC04-03-01 Take Photo in other Referral letter in application process finish")

    def testbooksopc0404(self):
        try:
            print("Book SOPC04-04 Review and Submit Application start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_02_03']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_02_03']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_02_03']
            patient_surname = user_data['patient_surname_02_03'][app_lang]
            patient_givenname = user_data['patient_givenname_02_03'][app_lang]
            patient_mobilenumber = user_data['patient_mobilenumber_02_03']
            Photo_OK_button = user_data['Photo_OK_button'][app_lang]
            edit_button = user_data['edit_button'][app_lang]
            edit_prefix_text = user_data['edit_prefix_text'][app_lang]
            cancel_button = user_data['cancel_button'][app_lang]
            CONFIRM_button = user_data['CONFIRM_button'][app_lang]
            patient_address = user_data['patient_address_02_03'][app_lang]
            Complete_button = user_data['Complete_button'][app_lang]

            ## User is not Log in; directly goes to Landing page
            #TestBook.testbook_login(self)
            print("Go to apps landing page without Log in")
            self.driver.find_element_by_xpath("//*[@text='Go to apps landing page']").click()
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click HA Go logon text
            print("Click HA Go logon text")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+submit_application_button+"']]").click()
            time.sleep(2)

            ## Click Book for others in Submit Application screen
            print("Book for others in Submit Application screen")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Decide if the patient has received healthcare services from any hospitals / clinics under Hospital Anthority (HA)
            ## Yes in this case
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Input Patient Surname
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_surname)
            time.sleep(2)

            ## Input Patient given name
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[4]").send_keys(patient_givenname)
            time.sleep(2)

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[5]").send_keys(patient_mobilenumber)
            time.sleep(2)

            ## The Patient information is input
            print("The Patient information is input")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Click Next Button to remove cursor
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()
            time.sleep(2)

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()
            time.sleep(2)

            ## Click Next Button to go to next page
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Submit Document screen is shown
            print("Submit Document screen is shown")
            time.sleep(2)

            ## Take Photo in Submit Document page
            print("Take Photo in Submit Document page")

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+OK_button+"']").click()
            time.sleep(3)

            ## Click Next to go next page
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on Referral letter
            print("User is on Referral letter screen")
            time.sleep(2)

            ## Click Photo-taking on referral letter page
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup").click()
            time.sleep(2)

            ## Click on Doctor's Referral Letter 1st page referral letter page
            print("Click on Doctor's Referral Letter 1st page referral letter page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup").click()
            time.sleep(2)

            ## Take Photo in Photo interface screen
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]")))
            self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(2)

            ## Confirm photo taken
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Photo_OK_button+"']]").click()
            time.sleep(2)

            ## Swipe down to show Next button to click
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on check data page
            print("User is on check data page which shows information of patient")
            time.sleep(2)

            ## The Progress Bar with 4th icon highlighted is displayed
            print("Book SOPC04-04 Scenario 01 The Progress Bar with 4th icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"04_04_Progress_bar_4th_icon.png")
            print("Screenshot 04_04_Progress_bar_4th_icon is taken")
            time.sleep(2)

            ## Correct patient's data displayed in patient document review pages
            print("Book SOPC04-04 Scenario 02 Correct patient's data displayed in patient document review pages")
            self.driver.save_screenshot(test_dir+"04_04_patient_data_check_data_page.png")
            print("Screenshot 04_04_patient_data_check_data_page is taken")
            time.sleep(2)

            ## Review page scroll
            print("Book SOPC04-04 Scenario 03 Review page scroll")
            ## Swipe down to show Next button to click
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"04_04_review_page_scroll.png")
            print("Screenshot 04_04_review_page_scroll is taken")
            time.sleep(2)

            ## Function of Edit and Submit button in Review page
            print("Book SOPC04-04 Scenario 04 Function of Edit and Submit button in Review page")
            time.sleep(2)

            ## Click Edit Button
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+edit_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"04_04_edit_input_data_page.png")
            print("Screenshot 04_04_edit_input_data_page is taken")
            time.sleep(2)

            ## Swipe down to show Appointment options
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)

            ## Tap Specialty
            time.sleep(2)
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*/*[@class='android.widget.Spinner'])[1]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"04_04_edit_specialty.png")
            print("Screenshot 04_04_edit_specialty is taken")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)

            ## Tap Hospital
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*/*[@class='android.widget.Spinner'])[2]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"04_04_edit_hospital.png")
            print("Screenshot 04_04_edit_hospital is taken")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)

            ## Click Next button to enter Edit Submit document screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)

            ## Delete Photo in Submit Document page in application process
            print("Click delete button")
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]]").click()
            time.sleep(4)

             ## Click CONFIRM to confirm quit application
            print("Click CONFIRM to confirm quit application")
            self.driver.find_element_by_xpath("//*[@text='"+CONFIRM_button+"']").click()
            time.sleep(2)

            ## Type in Patient's Address in Submit Document page in application process
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[2]").click()
            time.sleep(2)
 
            ## Input Patient's address
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']").send_keys(patient_address)
            time.sleep(2)
            self.driver.hide_keyboard
            time.sleep(2)
            
            ## Submit document page is edited
            self.driver.save_screenshot(test_dir+"04_04_edit_submit_document_page.png")
            print("Screenshot 04_04_edit_submit_document_page is taken")
            time.sleep(2)

            ## Click Next button to enter Edit Submit Referral Letter screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)

            ## Tap on Photo icon to try to take another photo but cancel
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[6]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[6]").click()
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"04_04_edit_referral_letter.png")
            print("Screenshot 04_04_edit_referral_letter is taken")
            time.sleep(2)
            self.driver.find_element_by_partial_link_text(cancel_button).click()
            time.sleep(2)

            ## Submit Referral Letter is edited
            self.driver.save_screenshot(test_dir+"04_04_edit_submit_referral_letter_page.png")
            print("Screenshot 04_04_edit_submit_referral_letter_page is taken")
            time.sleep(2)

            ## Swipe down to show Next button to click and enter Check Data screen again
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"04_04_return_check_data_from_edit.png")
            print("Screenshot 04_04_return_check_data_from_edit is taken")
            time.sleep(3)

            ## Swipe down to show Submit button and click submit button to Submit the Application
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]").click()
            time.sleep(6)

            ## Display of Complete page and Reference code
            print("Book SOPC04-04 Scenario 05 Display of Complete page and Reference code")
            time.sleep(2)

            ## Check if Information button is displayed in Complete page
            assert(self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").is_displayed), "Cannot find Information button"
            print("Information button is displayed in Complete page")
            time.sleep(2)

            ## Check if Complete button is displayed in Complete page
            assert(self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Complete_button+"' and @class='android.widget.TextView']]").is_displayed), "Cannot find Complete button"
            print("Complete button is displayed in Complete page")
            time.sleep(2)

            ## Check if Reference Number is displayed in Complete page
            assert(self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]").is_displayed), "Cannot find Reference Code"
            reference_code = self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]").text
            print("Reference Number"+ reference_code +" is displayed in Complete page")
            time.sleep(2)

            self.driver.save_screenshot(test_dir+"04_04_progress_bar_buttons_reference_code.png")
            print("Screenshot 04_04_progress_bar_buttons_reference_code is taken")
            time.sleep(2)

            ## Function of buttons in Complete page
            print("Book SOPC04-04 Scenario 06 Function of buttons in Complete page")
            time.sleep(2)

            ## Display of information pop-up window when clicked info icon
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()
            time.sleep(2)
            print("Display of information pop-up window when clicked info icon")
            self.driver.save_screenshot(test_dir+"04-04_information_pop_up_reference_number.png")
            print("Screenshot 04-04_information_pop_up_reference_number is taken")
            time.sleep(2)

            ## Clicked OK button to close information pop-up window
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            self.driver.find_element_by_xpath("//*[@id='button1']").click()
            time.sleep(2)

            ## Leave Complete screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Complete_button+"' and @class='android.widget.TextView']]").click()
            time.sleep(2)
            
            print("Book SOPC04-04 Scenario 07 [CURRENTLY NOT ENABLED] Display of Pop-up of promotion of '喜程' if enabled")
            time.sleep(2)
            print("Book SOPC04-04 Scenario 08 Go back to Book SOPC home screen after clicking Submit Application button")
            self.driver.save_screenshot(test_dir+"04-04_back_book_sopc_home_screen.png")
            print("Screenshot 04-04_back_book_sopc_home_screen is taken")
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT UNTIL BUG FIXED START
            ## Check if It goes back Book SOPC Home screen
            #assert(self.driver.find_element_by_xpath("//*[@text='"+sopc_booking_title+"']").is_displayed), "Cannot find SOPC booking title"
            #time.sleep(2)
            #### TEMPORARILY COMMENT OUT UNTIL BUG FIXED END

        except TimeoutException:
            print("Book SOPC04-04 Review and Submit Application Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC04-04 Review and Submit Application Exception")
            assert(False)
        finally:
            print("Book SOPC04-04 Review and Submit Application finish")


    def tearDown(self):
        self.driver.quit()