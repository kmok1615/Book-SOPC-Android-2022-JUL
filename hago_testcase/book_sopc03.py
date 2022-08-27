# coding=UTF-8
'''
Created on 2022.07.07
Updated on 2022.07.18
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

class TestBookSOPC03(unittest.TestCase):

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

    def testbooksopc0300(self):
        try:
            print("Book SOPC03-00 Ready Application Notes start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            cancel_button = user_data['cancel_button'][app_lang]
            no_button = user_data['no_button'][app_lang]
            #not_sure_button = user_data['not_sure_button'][app_lang]
            booking_in_person_button = user_data['booking_in_person_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
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
            print("Book SOPC03-00 Scenario 01 Access to related Precaution page by selecting related values in Declaration")
            self.driver.save_screenshot(test_dir+"03_00_declaration.png")
            print("Screenshot 03_00_declaration is taken")
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Decide if the patient has received healthcare services from any hospitals / clinics under Hospital Anthority (HA)
            ## No/Not Sure in this case
            ## Select No here
            print("Book SOPC03-00 Scenario 02 Display related information and buttons in Precaution page")
            print("Select No here")
            self.driver.find_element_by_xpath("//*[@text='"+no_button+"']").click()
            time.sleep(4)
            self.driver.save_screenshot(test_dir+"03_00_No_received_healthcare_service.png")
            print("Screenshot 03_00_no_received_healthcare_service is taken")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(2)

            ## Notice to patient is shown
            print("Book SOPC03-00 Scenario 03 Process of clicking 'Book in person' and 'Continue' buttons")
            self.driver.save_screenshot(test_dir+"03_00_Notice_to_patient.png")
            print("Screenshot 03_00_Notice_to_patient is taken")
            time.sleep(4)

            ## Click Booking in person it goes back to Submit Applicaiton Index screen
            print("Click Booking in person it goes back to Submit Applicaiton Index screen")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+booking_in_person_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+booking_in_person_button+"']]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_00_booking_in_person_back_to_submit_application_index.png")
            print("Screenshot 03_00_booking_in_person_back_to_submit_application_index is taken")
            time.sleep(2)

            ## Go to Notice to patient screen again
            print("Go to Notice to patient screen again")

            ## Click Book for others
            print("Book for others")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_others_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Select No here
            self.driver.find_element_by_xpath("//*[@text='"+no_button+"']").click()
            time.sleep(4)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Application Notes content display
            print("Book SOPC03-00 Scenario 04 Application Notes content display")
            self.driver.save_screenshot(test_dir+"03_00_Application_Notes.png")
            print("Screenshot 03_00_Application_Notes is taken")
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)
            ## Application Notes content display
            print("Book SOPC03-00 Scenario 05 Application Notes scroll")
            self.driver.save_screenshot(test_dir+"03_00_Application_Notes_scroll.png")
            print("Screenshot 03_00_Application_Notes_scroll is taken")
            time.sleep(4)
            ## Application Notes content display
            print("Book SOPC03-00 Scenario 06 Application Notes buttons")

            ## Click Cancel to close Application Notes 
            print("Click Cancel to close Application Notes")
            self.driver.find_element_by_xpath("//*[@text='"+cancel_button+"']").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_00_Application_Notes_Cancel.png")
            print("Screenshot 03_00_Application_Notes_Cancel is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC03-00 Read Application Notes Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC03-00 Read Application Notes Exception")
            assert(False)
        finally:
            print("Book SOPC03-00 Read Application Notes finish")

    def testbooksopc0301(self):
        try:
            print("Book SOPC03-01 Input Patient's information in application process start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            no_button = user_data['no_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_03_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_03_01']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_03_01']
            patient_mobilenumber = user_data['patient_mobilenumber_03_01']

            ## Log in
            TestBook.testbook_login(self)
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

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Select No here
            self.driver.find_element_by_xpath("//*[@text='"+no_button+"']").click()
            time.sleep(4)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Input Patient's information in application process
            print("Input Patient's information in application process")
            time.sleep(2)

            ## The Progress Bar with 1st icon highlighted is displayed
            print("Book SOPC03-01 Scenario 01 Progress bar display")
            self.driver.save_screenshot(test_dir+"03_01_Progress_bar_1st_icon.png")
            print("Screenshot 03_01_Progress_bar_1st_icon is taken")
            time.sleep(2)

            ## Patient's data in 2 input fields: HKID/Birth Certificate, HK mobile phone number are blanked
            print("Book SOPC03_01 Scenario 02 Patient's data in 2 input fields: HKID/Birth Certificate, HK mobile phone number are blank")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click section Title to remove cursor
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_mobilenumber)
            time.sleep(2)

            ## The Patient information is input
            print("The Patient information is input")
            self.driver.save_screenshot(test_dir+"03_01_Patient_data_input.png")
            print("Screenshot 03_01_Patient_data_input is taken")
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
            print("Book SOPC03_01 Scenario 03 Specialty and Hospital spinner field")
            self.driver.save_screenshot(test_dir+"03_01_Specialty_Hospital.png")
            print("Screenshot 03_01_Specialty_Hospital is taken")
            time.sleep(2)

            ## Click Next Button to go to next screen
            print("Book SOPC03_01 Scenario 04 Click Next Button to go to next screen")

            ## Click Next Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            self.driver.save_screenshot(test_dir+"03_01_Next_Button.png")
            print("Screenshot 03_01_Next_Button is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC03-01 Input Patient's information in application process Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC03-01 Input Patient's information in application process Exception")
            assert(False)
        finally:
            print("Book SOPC03-01 Input Patient's information in application process finish")

    def testbooksopc0302(self):
        try:
            print("Book SOPC03-02 Submit Document page in application process start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            Photo_OK_button = user_data['Photo_OK_button'][app_lang]
            CONFIRM_button = user_data['CONFIRM_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            no_button = user_data['no_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_03_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_03_01']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_03_01']
            patient_mobilenumber = user_data['patient_mobilenumber_03_01']
            patient_address = user_data['patient_address_03_01'][app_lang]
            submit_docuement_user_guide_text = user_data['submit_docuement_user_guide_text'][app_lang]
            submit_docuement_guidelines_text = user_data['submit_docuement_guidelines_text'][app_lang]
            HKBC_option = user_data['HKBC_option'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
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

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Select No here
            self.driver.find_element_by_xpath("//*[@text='"+no_button+"']").click()
            time.sleep(4)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Input Patient's information in application process
            print("Input Patient's information in application process")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click section Title to remove cursor
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_mobilenumber)
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

            ## Click Next Button to go to next screen
            print("Click Next Button to go to next screen")
            time.sleep(2)

            ## Click Next Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Submit Document screen is shown
            print("Submit Document screen is shown")
            time.sleep(2)

            ## The Progress Bar with 2nd icon highlighted is displayed
            print("Book SOPC03-02 Scenario 01 The Progress Bar with 2nd icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"03_02_Progress_bar_2nd_icon.png")
            print("Screenshot 03_02_Progress_bar_2nd_icon is taken")
            time.sleep(2)

            ## Click User Guide link
            print("Click User Guide link")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+submit_docuement_user_guide_text+"']").click()

            ## Submit Document User Guide pop-up window can be opened and closed
            print("Book SOPC03-02 Scenario 02 Submit Document User Guide pop-up window can be opened and closed")
            time.sleep(2)

            ## Submit Document User Guide Content can be displayed
            print("Book SOPC03-02 Scenario 03 Submit Document User Guide Content can be displayed")
            self.driver.save_screenshot(test_dir+"03_02_user_guide_content.png")
            print("Screenshot 03_02_user_guide_content is taken")
            time.sleep(2)

            ## Close User Guide pop-up
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+submit_docuement_guidelines_text+"']]]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+submit_docuement_guidelines_text+"']]]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_02_user_guide_closed.png")
            print("Screenshot 03_02_user_guide_closed is taken")

            ## Take Photo in Submit Document page
            print("Take Photo in Submit Document page")

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            ## Select Box of patient's identity document
            print("Book SOPC03-02-01 Scenario 01 Functions of buttons related to taking photo")
            self.driver.save_screenshot(test_dir+"03_02_01_function_take_photo.png")
            print("Screenshot 03_02_01_function_take_photo is taken")
            time.sleep(2)

            # Default option is Hong Kong Identity Card and click Confirm
            print("Click Confirm with selecting Hong Kong Identity Card")
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()

            ## Functions of buttons related to taking photo in Patient's Address
            print("Book SOPC03-02-01 Scenario 02 Display of Photo interface page for taking photo of Patient's HKID after selecting HKID")
            self.driver.save_screenshot(test_dir+"03_02_01_take_photo_interface_HKID.png")
            print("Screenshot 03_02_01_take_photo_interface_HKID is taken")
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Photo of document can be taken
            self.driver.save_screenshot(test_dir+"03_02_01_take_photo_document_HKID_done.png")
            print("Screenshot 03_02_01_take_photo_document_HKID_done is taken")
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+Photo_OK_button+"']")))
            self.driver.find_element_by_xpath("//*[@text='"+Photo_OK_button+"']").click()
            time.sleep(3)

            ## Change outlook of icons in Patient's Address after the process of Take Photo
            print("Book SOPC03-02-01 Scenario 03 Section of HKID/Birth Certificate after taking photo of Patient's HKID")
            self.driver.save_screenshot(test_dir+"03_02_01_patient_address_after_taking_photo_HKID_document.png")
            print("Screenshot 03_02_01_patient_address_after_taking_photo_HKID_document is taken")
            time.sleep(2)

            ## Functions of buttons related to taking photo in Patient's Address
            print("Book SOPC03-02-01 Scenario 04 Functions of buttons related to taking photo in Patient's Address")

            ## Click Take Photo button to take photo of document
            print("Click Take Photo button to take photo of document")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(2)

            ## Functions of different buttons in Take Photo interface
            print("Book SOPC03-02-01 Scenario 05 Functions of different buttons in Take Photo interface")
            self.driver.save_screenshot(test_dir+"03_02_01_take_photo_interface.png")
            print("Screenshot 03_02_01_take_photo_interface is taken")
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+Photo_OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+Photo_OK_button+"']").click()
            time.sleep(3)

            ## Change outlook of icons in Patient's Address after the process of Take Photo
            print("Book SOPC03-02-01 Scenario 06 Change outlook of icons in Patient's Address after the process of Take Photo")
            self.driver.save_screenshot(test_dir+"03_02_01_patient_address_after_taking_photo_document.png")
            print("Screenshot 03_02_01_patient_address_after_taking_photo_document is taken")
            time.sleep(2)

            ## Delete Photo in Submit Document page in application process
            print("Click delete button")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()
            time.sleep(4)

            ## Click CONFIRM to confirm delete photo
            print("Click CONFIRM to confirm delete photo")
            self.driver.find_element_by_xpath("//*[@text='"+CONFIRM_button+"']").click()
            time.sleep(2)

            ## Type in Patient's Address in Submit Document page in application process
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[3]").click()
            time.sleep(2)
            print("Book SOPC03-02-01 Scenario 07 Change of interface when clicking 'Pen' button")
            self.driver.save_screenshot(test_dir+"03_02_01_typing_patient_address_box.png")
            print("Screenshot 03_02_01_typing_patient_address_box is taken")
            time.sleep(2)

            ## Input Patient's address
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']").send_keys(patient_address)
            time.sleep(2)
            self.driver.hide_keyboard
            time.sleep(2)
            print("Book SOPC03-02-01 Scenario 08 Input data to patient's address box")
            self.driver.save_screenshot(test_dir+"03_02_01_typing_patient_address_box.png")
            print("Screenshot 03_02_01_typing_patient_address_box is taken")

            ## Click Next Button to go to next screen
            print("Book SOPC03-02-01 Scenario 09 Click Next Button to go to next screen")

            ## Click Next to go next page
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_02_01_Next_Button.png")
            print("Screenshot 03_02_01_Next_Button is taken")
            time.sleep(2)

            ## Go back to previous screen
            self.driver.press_keycode(4)
            time.sleep(2)

            ## Delete HKID Photo
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()
            time.sleep(2)

            ## Click CONFIRM to confirm delete photo
            print("Click CONFIRM to confirm delete photo")
            self.driver.find_element_by_xpath("//*[@text='"+CONFIRM_button+"']").click()
            time.sleep(2)

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            # Click option Hong Kong Birth Certificate and click Confirm
            print("Book SOPC03-02-01-01 Scenario 01 Display of Photo interface page for taking photo of Patient's HKID after selecting HKID")
            print("Click Confirm with selecting Hong Kong Birth Certificate")

            self.driver.find_element_by_xpath("//*[@text='"+HKBC_option+"']").click()
            time.sleep(4)

            ## Select Box of patient's identity document
            self.driver.save_screenshot(test_dir+"03_02_01_01_select_HKBC.png")
            print("Screenshot 03_02_01_01_select_HKBC is taken")
            time.sleep(2)

            ## Click Confirm
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(4)

            ## Section of HKID/Birth Certificate after taking photo of Patient's Birth Certificate
            self.driver.save_screenshot(test_dir+"03_02_01_01_take_photo_interface_HKBC.png")
            print("Screenshot 03_02_01_01_take_photo_interface_HKBC is taken")
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Photo of document can be taken
            self.driver.save_screenshot(test_dir+"03_02_01_01_take_photo_document_HKBC_done.png")
            print("Screenshot 03_02_01_01_take_photo_document_HKBC_done is taken")
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+Photo_OK_button+"']")))
            self.driver.find_element_by_xpath("//*[@text='"+Photo_OK_button+"']").click()
            time.sleep(3)

            ## Section of HKID/Birth Certificate after taking photo of Patient's Birth Certificate
            print("Book SOPC03-02-01-01 Scenario 02 Section of HKID/Birth Certificate after taking photo of Patient's HKBC")
            self.driver.save_screenshot(test_dir+"03_02_01_01_patient_address_after_taking_photo_HKBC_document.png")
            print("Screenshot 03_02_01_01_patient_address_after_taking_photo_HKBC_document is taken")
            time.sleep(2)

            

        except TimeoutException:
            print("Book SOPC03-02 Submit Document page in application process Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC03-02 Submit Document page in application process Exception")
            assert(False)
        finally:
            print("Book SOPC03-02 Submit Document page in application process finish")

    def testbooksopc0303(self):
        try:
            print("Book SOPC03-03 Take Photo of Other Referral letter start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            Photo_OK_button = user_data['Photo_OK_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            no_button = user_data['no_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_03_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_03_01']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_03_01']
            patient_mobilenumber = user_data['patient_mobilenumber_03_01']

            ## Log in
            TestBook.testbook_login(self)
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

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Select No here
            self.driver.find_element_by_xpath("//*[@text='"+no_button+"']").click()
            time.sleep(4)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Input Patient's information in application process
            print("Input Patient's information in application process")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click section Title to remove cursor
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_mobilenumber)
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

            ## Click Next Button to go to next screen
            print("Click Next Button to go to next screen")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Submit Document screen is shown
            print("Submit Document screen is shown")
            time.sleep(2)

            ## Take Photo in Submit Document page
            print("Take Photo in Submit Document page")

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            # Default option is Hong Kong Identity Card and click Confirm
            print("Click Confirm with selecting Hong Kong Identity Card")
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+Photo_OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+Photo_OK_button+"']").click()
            time.sleep(3)

            ## Click Take Photo button to take photo of document
            print("Click Take Photo button to take photo of document")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+OK_button+"']").click()
            time.sleep(3)

            ## Click Next Button to go to next screen
            print("Click Next Button to go to next screen")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## User is on Referral letter
            print("User is on Referral letter screen")
            time.sleep(2)

            ## The Progress Bar with 3rd icon highlighted is displayed
            print("Book SOPC03-03 Scenario 01 The Progress Bar with 3rd icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"03_03_Progress_bar_3rd_icon.png")
            print("Screenshot 03_03_Progress_bar_3rd_icon is taken")
            time.sleep(2)

            ## Display of Other Referral letter screen
            print("Book SOPC03-03 Scenario 02 Display of Other Referral letter screen")
            time.sleep(2)

            ## Click on Doctor's Referral Letter 1st page referral letter page
            print("Click on Doctor's Referral Letter 1st page referral letter page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup").click()
            time.sleep(2)

            ## User is on Photo interface screen
            print("Book SOPC03-03 Scenario 03 Display of Photo interface page for taking photo after clicking photo icon")
            self.driver.save_screenshot(test_dir+"03_03_Photo_interface_screen.png")
            print("Screenshot 03_03_Photo_interface_screen is taken")
            time.sleep(2)

            ## Take Photo in Photo interface screen
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]")))
            self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(2)

            ## User is on Photo interface screen
            print("Book SOPC03-03 Scenario 04 Functions of different buttons in Take Photo interfaces")
            self.driver.save_screenshot(test_dir+"03_03_Photo_taken_screen.png")
            print("Screenshot 03_03_Photo_taken_screen is taken")
            time.sleep(2)

            ## Confirm photo taken
            print("Confirm photo taken")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Photo_OK_button+"']]").click()
            time.sleep(2)

            ## Photo taken is added
            print("Book SOPC03-03 Scenario 05 Change outlook of icons in Other Referral letter after the process of Take Photo")
            self.driver.save_screenshot(test_dir+"03_03_Photo_taken_on_referral_letter_page.png")
            print("Screenshot 03_03_Photo_taken_on_referral_letter_page is taken")
            time.sleep(3)

            ## Tap Zoom button
            print("Tap Zoom button to open photo page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[5]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[5]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_03_Zoom_Photo_taken_page.png")
            print("Screenshot 02_03_01_Zoom_Photo_taken_page is taken")
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
            print("Book SOPC02-03-01 Scenario 05 Next button")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on check data page
            print("Book SOPC03-03 Scenario 06 Display of information of patient in patient information screen")
            print("User is on check data page which shows information of patient")
            self.driver.save_screenshot(test_dir+"03_03_check_data_page_from_QR_code_scanned.png")
            print("Screenshot 03_03_check_data_page_from_QR_code_scanned is taken")
            time.sleep(3)

        except TimeoutException:
            print("Book SOPC03-03 Take Photo of Other Referral letter Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC03-03 Take Photo of Other Referral letter Exception")
            assert(False)
        finally:
            print("Book SOPC03-03 Take Photo of Other Referral letter finish")

    def testbooksopc0304(self):
        try:
            print("Book SOPC03-04 Review and Submit Application start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_others_button = user_data['book_for_others_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            Photo_OK_button = user_data['Photo_OK_button'][app_lang]
            accept_button = user_data['accept_button'][app_lang]
            no_button = user_data['no_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_03_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_03_01']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_03_01']
            patient_address = user_data['patient_address'][app_lang]
            patient_mobilenumber = user_data['patient_mobilenumber_03_01']
            edit_button = user_data['edit_button'][app_lang]
            edit_prefix_text = user_data['edit_prefix_text'][app_lang]
            cancel_button = user_data['cancel_button'][app_lang]
            CONFIRM_button = user_data['CONFIRM_button'][app_lang]
            Complete_button = user_data['Complete_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
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

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Accept button for Declaration
            self.driver.find_element_by_xpath("//*[@text='"+accept_button+"']").click()
            time.sleep(4)

            ## Select No here
            self.driver.find_element_by_xpath("//*[@text='"+no_button+"']").click()
            time.sleep(4)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Confirm here
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Click scroll icon to scroll down
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start application
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## Input Patient's information in application process
            print("Input Patient's information in application process")
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click section Title to remove cursor
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView").click()

            ## Input Patient mobile number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[3]").send_keys(patient_mobilenumber)
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

            ## Click Next Button to go to next screen
            print("Click Next Button to go to next screen")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Submit Document screen is shown
            print("Submit Document screen is shown")
            time.sleep(2)

            ## Take Photo in Submit Document page
            print("Take Photo in Submit Document page")

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            # Default option is Hong Kong Identity Card and click Confirm
            print("Click Confirm with selecting Hong Kong Identity Card")
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+Photo_OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+Photo_OK_button+"']").click()
            time.sleep(3)

            ## Click Take Photo button to take photo of document
            print("Click Take Photo button to take photo of document")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+OK_button+"']").click()
            time.sleep(3)

            ## Click Next Button to go to next screen
            print("Click Next Button to go to next screen")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## User is on Referral letter
            print("User is on Referral letter screen")
            time.sleep(2)

            ## Click on Doctor's Referral Letter 1st page referral letter page
            print("Click on Doctor's Referral Letter 1st page referral letter page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup").click()
            time.sleep(2)

             ## Take Photo in Photo interface screen
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]")))
            self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(2)

            ## Confirm photo taken
            print("Confirm photo taken")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Photo_OK_button+"']]").click()
            time.sleep(2)

            ## Swipe down to show Next button to click
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)

            ## Click Next Button to go to next screen
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on check data page
            print("Book SOPC03-04 Review and Submit Application")
            print("User is on check data page which shows information of patient")

            ## The Progress Bar with 4th icon highlighted is displayed
            print("Book SOPC03-04 Scenario 01 The Progress Bar with 4th icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"03_04_Progress_bar_4th_icon.png")
            print("Screenshot 03_04_Progress_bar_4th_icon is taken")
            time.sleep(2)

            ## Swipe down to show Next button to click
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)

            ## Correct patient's data displayed in patient document review pages
            print("Book SOPC03-04 Scenario 02 Correct patient's data displayed in patient document review pages")
            self.driver.save_screenshot(test_dir+"03_04_patient_data_check_data_page.png")
            print("Screenshot 03_04_patient_data_check_data_page is taken")
            time.sleep(2)

            ## Function of Edit and Submit button in Review page
            print("Book SOPC03-04 Scenario 03 Function of Edit and Submit button in Review page")
            time.sleep(2)

            ## Click Edit Button
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+edit_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_04_edit_input_data_page.png")
            print("Screenshot 03_04_edit_input_data_page is taken")
            time.sleep(2)

            ## Swipe down to show Appointment options
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)

            ## Tap Specialty
            time.sleep(2)
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*/*[@class='android.widget.Spinner'])[1]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_04_edit_specialty.png")
            print("Screenshot 03_04_edit_specialty is taken")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)

            ## Tap Hospital
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*/*[@class='android.widget.Spinner'])[2]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_04_edit_hospital.png")
            print("Screenshot 03_04_edit_hospital is taken")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)

            ## Click Next button to enter Edit Submit document screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)

            ## Delete HKID Photo in Submit Document page in application process
            print("Click delete HKID button")
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]]").click()
            time.sleep(4)

             ## Click CONFIRM to confirm delete photo
            print("Click CONFIRM to confirm delete photo")
            self.driver.find_element_by_xpath("//*[@text='"+CONFIRM_button+"']").click()
            time.sleep(2)

            ## Click Open Take Photo interface button in (Edit)Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            # Default option is Hong Kong Identity Card and click Confirm
            print("Click Confirm with selecting Hong Kong Identity Card")
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+Photo_OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+Photo_OK_button+"']").click()
            time.sleep(3)

            ## Click Take Photo button to take photo of document
            print("Click Take Photo button to take photo of document")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(2)

            ## HKID Photo is updated
            print("HKID Photo is updated")

            ## Submit document page is edited
            self.driver.save_screenshot(test_dir+"03_04_edit_submit_document_page.png")
            print("Screenshot 03_04_edit_submit_document_page is taken")
            time.sleep(2)

            ## Click Next button to enter Edit Submit Referral Letter screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)

            ## Tap on Photo icon to try to take another photo but cancel
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]").click()
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"03_04_edit_referral_letter.png")
            print("Screenshot 03_04_edit_referral_letter is taken")
            time.sleep(2)
            self.driver.find_element_by_partial_link_text(cancel_button).click()
            time.sleep(2)

            ## Submit Referral Letter is edited
            self.driver.save_screenshot(test_dir+"03_04_edit_submit_referral_letter_page.png")
            print("Screenshot 03_04_edit_submit_referral_letter_page is taken")
            time.sleep(2)

            ## Swipe down to show Next button to click and enter Check Data screen again
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"03_04_return_check_data_from_edit.png")
            print("Screenshot 03_04_return_check_data_from_edit is taken")
            time.sleep(3)

            ## Swipe down to show Submit button and click submit button to Submit the Application
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]").click()
            time.sleep(6)

            ## Display of Complete page and Reference code
            print("Book SOPC03-04 Scenario 04 Display of Complete page and Reference code")
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

            self.driver.save_screenshot(test_dir+"03_04_progress_bar_buttons_reference_code.png")
            print("Screenshot 03_04_progress_bar_buttons_reference_code is taken")
            time.sleep(2)

            ## Function of buttons in Complete page
            print("Book SOPC03-04 Scenario 05 Function of buttons in Complete page")
            time.sleep(2)

            ## Leave Complete screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Complete_button+"' and @class='android.widget.TextView']]").click()
            time.sleep(2)
            print("Book SOPC03-04 Scenario 06 Go back to Book SOPC home screen after clicking Submit Application button")
            self.driver.save_screenshot(test_dir+"03_04_back_book_sopc_home_screen.png")
            print("Screenshot 03-04_back_book_sopc_home_screen is taken")
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT UNTIL BUG FIXED START
            ## Check if It goes back Book SOPC Home screen
            #assert(self.driver.find_element_by_xpath("//*[@text='"+sopc_booking_title+"']").is_displayed), "Cannot find SOPC booking title"
            #time.sleep(2)
            #### TEMPORARILY COMMENT OUT UNTIL BUG FIXED END

        except TimeoutException:
            print("Book SOPC03-04 Review and Submit Application Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC03-04 Review and Submit Application Exception")
            assert(False)
        finally:
            print("Book SOPC03-04 Review and Submit Application finish")


    def tearDown(self):
        self.driver.quit()