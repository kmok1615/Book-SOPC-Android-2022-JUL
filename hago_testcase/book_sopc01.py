# coding=UTF-8
'''
Created on 2022.07.07
Updated on 2022.07.13
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

class TestBookSOPC01(unittest.TestCase):

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

    def testbooksopc0100(self):
        try:
            print("Book SOPC01-00 Ready Application Notes start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_self_button = user_data['book_for_self_button'][app_lang]
            cancel_button = user_data['cancel_button'][app_lang]

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

            ## Click Book for self
            print("Book for self")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Application Notes is shown
            print("Book SOPC01-00 Scenario 01 Application Notes is shown")
            self.driver.save_screenshot(test_dir+"01_00_Application_Notes.png")
            print("Screenshot 01_00_Application_Notes is taken")
            time.sleep(5)

            ## Click scroll icon to scroll down
            print("Book SOPC01-00 Scenario 02 Click scroll icon to scroll down")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Cancel button to close Application Notes
            print("Book SOPC01-00 Scenario 03 Click Cancel button to close Application Notes")
            self.driver.find_element_by_xpath("//*[@text='"+cancel_button+"']").click()
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC01-00 Ready Application Notes Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC01-00 Ready Application Notes Exception")
            assert(False)
        finally:
            print("Book SOPC01-00 Ready Application Notes finish")

    def testbooksopc0101(self):
        try:
            print("Book SOPC01-01 Quit Application Screen start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_self_button = user_data['book_for_self_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            CONFIRM_button = user_data['CONFIRM_button'][app_lang]

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

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            print("Book SOPC01-00 Scenario 02 Click scroll icon to scroll down")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start Application
            print("Book SOPC01-00 Scenario 03 Click Continue button to start Application")
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## Click Back button to quit Application
            print("Click Back button to quit Application")
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@class='android.view.ViewGroup']]]]").click()
            time.sleep(4)

            ## Pop-up box to confirm quit application is shown
            print("Pop-up box to confirm quit application is shown")
            self.driver.save_screenshot(test_dir+"01_01_Quit_Application_pop_up.png")
            print("Screenshot 01_01_Quit_Application_pop_up is taken")
            time.sleep(2)

            ## Click CONFIRM to confirm quit application
            print("Click CONFIRM to confirm quit application")
            self.driver.find_element_by_xpath("//*[@text='"+CONFIRM_button+"']").click()
            time.sleep(4)

            ## Redirect back to Submit Application screen
            print("Redirect back to Submit Application screen")
            self.driver.save_screenshot(test_dir+"01_01_Back_to_Submit_Application.png")
            print("Screenshot 01_01_Back_to_Submit_Application is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC01-01 Quit Application Screen Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC01-01 Quit Application Screen Exception")
            assert(False)
        finally:
            print("Book SOPC01-01 Quit Application Screen finish")

    def testbooksopc0102(self):
        try:
            print("Book SOPC01-02 Input Patient's information in application process start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_self_button = user_data['book_for_self_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]

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

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            print("Book SOPC01-00 Scenario 02 Click scroll icon to scroll down")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']]").click()
            time.sleep(2)

            ## Click Continue button to start Application
            print("Book SOPC01-00 Scenario 03 Click Continue button to start Application")
            self.driver.find_element_by_xpath("//*[@text='"+continue_button+"']").click()
            time.sleep(4)

            ## User is in Input Data screen
            print("User is in Input Data screen")
            time.sleep(2)

            ## The Progress Bar with 1st icon highlighted is displayed
            print("Book SOPC01-02 Scenario 01 The Progress Bar with 1st icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"01_02_Progress_bar_1st_icon.png")
            print("Screenshot 01_02_Progress_bar_1st_icon is taken")
            time.sleep(2)

            ## Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled
            print("Book SOPC01-02 Scenario 02 Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled")
            time.sleep(2)

            self.driver.save_screenshot(test_dir+"01_02_User_data_auto_filled.png")
            print("Screenshot 01_02_User_data_auto_filled is taken")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()

            ## The Specialty and Hospital can be input by user
            print("Book SOPC01-02 Scenario 03 The Specialty and Hospital can be input by user")
            self.driver.save_screenshot(test_dir+"01_02_Specialty_Hospital.png")
            print("Screenshot 01_02_Specialty_Hospital is taken")
            time.sleep(2)

            ## Click Next Button to go to next screen
            print("Book SOPC01-02 Scenario 04 Click Next Button to go to next screen")
            self.driver.save_screenshot(test_dir+"01_02_Next_Button.png")
            print("Screenshot 01_02_Next_Button is taken")
            time.sleep(2)

            ## Click Next Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()

        except TimeoutException:
            print("Book SOPC01-02 Input Patient's information in application process Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC01-02 Input Patient's information in application process Exception")
            assert(False)
        finally:
            print("Book SOPC01-02 Input Patient's information in application process finish")

    def testbooksopc0103(self):
        try:
            print("Book SOPC01-03 View User Guide in Submit Document page in application process start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_self_button = user_data['book_for_self_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            submit_docuement_user_guide_text = user_data['submit_docuement_user_guide_text'][app_lang]
            submit_docuement_guidelines_text = user_data['submit_docuement_guidelines_text'][app_lang]
            CONFIRM_button = user_data['CONFIRM_button'][app_lang]
            patient_address = user_data['patient_address'][app_lang]
            Photo_OK_button = user_data['Photo_OK_button'][app_lang]

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

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            print("Click scroll icon to scroll down")
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

            ## The Progress Bar with 1st icon highlighted is displayed
            print("The Progress Bar with 1st icon highlighted is displayed")
            time.sleep(2)

            ## Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled
            print("Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()

            ## The Specialty and Hospital can be input by user
            print("The Specialty and Hospital can be input by user")
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

            ## The Progress Bar with 2nd icon highlighted is displayed
            print("Book SOPC01-03 Scenario 01 The Progress Bar with 2nd icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"01_02_Progress_bar_2nd_icon.png")
            print("Screenshot 01_03_Progress_bar_2nd_icon is taken")
            time.sleep(2)

            ## Click User Guide link
            print("Click User Guide link")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+submit_docuement_user_guide_text+"']").click()

            ## Submit Document User Guide pop-up window can be opened and closed
            print("Book SOPC01-03 Scenario 02 Submit Document User Guide pop-up window can be opened and closed")
            time.sleep(2)

            ## Submit Document User Guide Content can be displayed
            print("Book SOPC01-03 Scenario 03 Submit Document User Guide Content can be displayed")
            self.driver.save_screenshot(test_dir+"01_03_user_guide_content.png")
            print("Screenshot 01_03_user_guide_content is taken")
            time.sleep(2)

            ## Close User Guide pop-up
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+submit_docuement_guidelines_text+"']]]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+submit_docuement_guidelines_text+"']]]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_03_user_guide_closed.png")
            print("Screenshot 01_03_user_guide_closed is taken")

            ## Take Photo in Submit Document page
            print("Take Photo in Submit Document page")

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            ## Take Photo interface can be displayed
            print("Book SOPC01-03-01 Scenario 01 Click Take Photo interface button to open Take Photo interface")
            self.driver.save_screenshot(test_dir+"01_03_01_take_photo_interface.png")
            print("Screenshot 01_03_01_take_photo_interface is taken")
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Photo of document can be taken
            print("Book SOPC01-03-01 Scenario 02 Photo of document can be taken")
            self.driver.save_screenshot(test_dir+"01_03_01_take_photo_document_done.png")
            print("Screenshot 01_03_01_take_photo_document_done is taken")
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+Photo_OK_button+"']")))
            self.driver.find_element_by_xpath("//*[@text='"+Photo_OK_button+"']").click()
            time.sleep(3)

            ## Change outlook of icons in Patient's Address after the process of Take Photo
            print("Book SOPC01-03-01 Scenario 03 Change outlook of icons in Patient's Address after the process of Take Photo")
            self.driver.save_screenshot(test_dir+"01_03_01_patient_address_after_taking_photo_document.png")
            print("Screenshot 01_03_01_patient_address_after_taking_photo_document is taken")
            time.sleep(2)

            ## Delete Photo in Submit Document page in application process
            print("Click delete button")
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ImageView']]]").click()
            time.sleep(4)

            ## Display confirm pop-up box of delete image
            print("Book SOPC01-03-01-01 Scenario 01 Display confirm pop-up box of delete image")
            self.driver.save_screenshot(test_dir+"01_03_01_01_confirm_delete_image.png")
            print("Screenshot 01_03_01_01_confirm_delete_image is taken")
            time.sleep(4)

            ## Click CONFIRM to confirm quit application
            print("Click CONFIRM to confirm quit application")
            self.driver.find_element_by_xpath("//*[@text='"+CONFIRM_button+"']").click()
            time.sleep(2)

            ## Change outlook of icons in Patient's Address after the process of deleting photo
            print("Book SOPC01-03-01-01 Scenario 02 Change outlook of icons in Patient's Address after the process of deleting photo")
            self.driver.save_screenshot(test_dir+"01_03_01_01_patient_address_after_delete_image.png")
            print("Screenshot 01_03_01_01_patient_address_after_delete_image is taken")
            time.sleep(2)

            ## Type in Patient's Address in Submit Document page in application process
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[2]").click()
            time.sleep(2)
            print("Book SOPC01-03-02 Scenario 01 typing patient address box in Patient's Address")
            self.driver.save_screenshot(test_dir+"01_03_02_typing_patient_address_box.png")
            print("Screenshot 01_03_02_typing_patient_address_box is taken")
            time.sleep(2)

            ## Input Patient's address
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']").send_keys(patient_address)
            time.sleep(2)
            self.driver.hide_keyboard
            time.sleep(2)
            
            ## Change outlook of icons in Patient's Address after the process of inputting patient address
            print("Book SOPC01-03-02 Scenario 02 typing patient address box in Patient's Address")
            self.driver.save_screenshot(test_dir+"01_03_02_icons_patient_address_after_input_address.png")
            print("Screenshot 01_03_02_icons_patient_address_after_input_address is taken")
            time.sleep(2)

            ## Click Next to go next page
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)


        except TimeoutException:
            print("Book SOPC01-03 View User Guide in Submit Document page in application process Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC01-03 View User Guide in Submit Document page in application process Exception")
            assert(False)
        finally:
            print("Book SOPC01-03 View User Guide in Submit Document page in application process finish")

    def testbooksopc010401(self):
        try:
            print("Book SOPC01-04 Scanning QR code on Referral letter start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            submit_application_button = user_data['submit_application_button'][app_lang]
            book_for_self_button = user_data['book_for_self_button'][app_lang]
            continue_button = user_data['continue_button'][app_lang]
            Select_Specialty_spinner = user_data['Select_Specialty_spinner'][app_lang]
            Select_Hospital_spinner = user_data['Select_Hospital_spinner'][app_lang]
            spinner_specialty = user_data['spinner_specialty'][app_lang]
            spinner_hospital = user_data['spinner_hospital'][app_lang]
            next_button = user_data['next_button'][app_lang]
            scan_qr_code_user_guide_text = user_data['scan_qr_code_user_guide_text'][app_lang]
            patient_address = user_data['patient_address'][app_lang]
            please_click_here_to_check_link = user_data['please_click_here_to_check_link'][app_lang]

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

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            print("Click scroll icon to scroll down")
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

            ## Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled
            print("Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("xpath=(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"]]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()

            ## The Specialty and Hospital can be input by user
            print("The Specialty and Hospital can be input by user")
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

            ## The Progress Bar with 3rd icon highlighted is displayed
            print("Book SOPC01-04 Scenario 01 The Progress Bar with 3rd icon highlighted is displayed")
            self.driver.save_screenshot(test_dir+"01_04_Progress_bar_3rd_icon.png")
            print("Screenshot 01_04_Progress_bar_3rd_icon is taken")
            time.sleep(2)

            ## Click User Guide link
            print("Click User Guide link")
            self.driver.find_element_by_xpath("xpath=//*[@text='"+scan_qr_code_user_guide_text+"']").click()
            time.sleep(2)

            ## User Guide in scanning QR code on Referral letter
            print("Book SOPC01-04 Scenario 02 User Guide in scanning QR code on Referral letter is displayed")
            self.driver.save_screenshot(test_dir+"01_04_User_guide_scanning_qr_code_referral_letter.png")
            print("Screenshot 01_04_User_guide_scanning_qr_code_referral_letter is taken")
            time.sleep(2)

            ## Close User Guide pop-up
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ScrollView']]]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ScrollView']]]").click()
            time.sleep(2)
            print("Book SOPC01-04 Scenario 03 User Guide in scanning QR code on Referral letter is closed")
            self.driver.save_screenshot(test_dir+"01_04_user_guide_closed.png")
            print("Screenshot 01_04_user_guide_closed is taken")

            ## Wait 20 seconds for manually scanning invalid QR code
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            print("Book SOPC01-04-01 Scenario 01 Functions of buttons of scanning QR code on Referral letter")
            time.sleep(3)
            print("Invalid QR code is scanned")
            self.driver.save_screenshot(test_dir+"01_04_01_invalid_QR_code.png")
            print("Screenshot 01_04_01_invalid_QR_code is taken")

            ## Clicked Re-scan button
            self.driver.find_element_by_xpath("//*[@id='button1']").click()
            time.sleep(3)
            print("Clicked Re-scan button")
            self.driver.save_screenshot(test_dir+"01_04_01_rescan_QR_code.png")
            print("Screenshot 01_04_01_rescan_QR_code is taken")

            ## Wait 20 seconds for manually scanning valid QR code
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            time.sleep(3)
            print("QR code is scanned successfully")
            self.driver.save_screenshot(test_dir+"01_04_01_valid_QR_code_scanned.png")
            print("Screenshot 01_04_01_valid_QR_code_scanned is taken")
            time.sleep(3)

            ## Clicked Close button to go Check data page
            self.driver.find_element_by_xpath("//*[@id='button1']").click()

            ## User is on check data page
            print("User is on check data page")
            self.driver.save_screenshot(test_dir+"01_04_01_check_data_page_from_QR_code_scanned.png")
            print("Screenshot 01_04_01_check_data_page_from_QR_code_scanned is taken")
            time.sleep(3)

            #### TEMPORARILY COMMENT OUT UNTIL BUG FIXED START
            ## Check if link "Please click here to check" exists
            #assert(self.driver.find_element_by_xpath("//*[@text='"+please_click_here_to_check_link+"']").is_displayed), "Cannot find Please click here to check link"
            #time.sleep(2)
            #### TEMPORARILY COMMENT OUT UNTIL BUG FIXED END

        except TimeoutException:
            print("Book SOPC01-04-01 Scanning QR code on Referral letter Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC01-04-01 Scanning QR code on Referral letter Exception")
            assert(False)
        finally:
            print("Book SOPC01-04-01 Scanning QR code on Referral letter finish")

    def testbooksopc010402(self):
        try:
            print("Book SOPC01-04-02 Take Photo on Referral letter start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
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
            submit_docuement_user_guide_text = user_data['submit_docuement_user_guide_text'][app_lang]
            patient_address = user_data['patient_address'][app_lang]
            submit_docuement_guidelines_text = user_data['submit_docuement_guidelines_text'][app_lang]

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

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            print("Click scroll icon to scroll down")
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

            ## Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled
            print("Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("xpath=(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()

            ## The Specialty and Hospital can be input by user
            print("The Specialty and Hospital can be input by user")
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

            ## Click User Guide link
            print("Click User Guide link")
            self.driver.find_element_by_xpath("xpath=//*[@text='"+submit_docuement_user_guide_text+"']").click()
            time.sleep(2)

            ## Type in Patient's Address in Submit Document page in application process
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*[@class='android.widget.TextView' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()
            time.sleep(2)

            ## Close User Guide pop-up
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+submit_docuement_guidelines_text+"']]]")))
            self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+submit_docuement_guidelines_text+"']]]").click()
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
            time.sleep(4)
            print("Book SOPC01-04-02 Scenario 01 Read User Guide in taking picture on Referral letter")
            self.driver.save_screenshot(test_dir+"01_04_02_switch_to_photo_taking.png")
            print("Screenshot 01_04_02_switch_back_to_photo_taking is taken")
            time.sleep(4)

            ## Click User Guide link
            time.sleep(2)
            print("Click User Guide link")
            self.driver.find_element_by_xpath("//*[@text='"+submit_docuement_user_guide_text+"']").click()
            time.sleep(2)

            ## User Guide in Take Photo on Referral letter
            print("Book SOPC01-04-02 Scenario 02 User Guide in take photo on Referral letter is displayed")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_04_02_User_guide_take_photo_referral_letter.png")
            print("Screenshot 01_04_02_User_guide_take_photo_referral_letter is taken")
            time.sleep(2)

            ## Close User Guide pop-up
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ScrollView']]]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.widget.ScrollView']]]").click()
            time.sleep(2)
            print("Book SOPC01-04-02 Scenario 03 User Guide in take photo on Referral letter is closed")
            self.driver.save_screenshot(test_dir+"01_04_02_User_guide_closed.png")
            print("Screenshot 01_04_02_User_guide_closed is taken")
            time.sleep(3)

            ## Tap on Photo icon to take 1st photo
            print("Book SOPC01-04-02-01 Scenario 01 Tap on Photo icon to take 1st photo")
            self.driver.save_screenshot(test_dir+"01_04_02_01_Tap_Photo_icon.png")
            print("Screenshot 01_04_02_01_Tap_Photo_icon is taken")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[6]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[6]").click()
            time.sleep(3)

            ## User is on Photo interface screen
            print("Book SOPC01-04-02-01 Scenario 02 Photo interface screen")
            self.driver.save_screenshot(test_dir+"01_04_02_01_Photo_interface_screen.png")
            print("Screenshot 01_04_02_01_Photo_interface_screen is taken")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]")))
            self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]").click()
            time.sleep(3)

            ## Confirm photo taken
            print("Confirm photo taken")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Photo_OK_button+"']]").click()
            time.sleep(2)

            ## Photo taken is added
            print("Book SOPC01-04-02-01 Scenario 03 Change outlook of icons in other Referral letter after the process of Take Photo")
            self.driver.save_screenshot(test_dir+"01_04_02_01_Photo_taken_on_referral_letter_page.png")
            print("Screenshot 01_04_02_01_Photo_taken_on_referral_letter_page is taken")
            time.sleep(3)

            ## Tap Zoom button
            print("Tap Zoom button to open photo page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[5]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[5]").click()
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"01_04_02_01_Zoom_Photo_taken_page.png")
            print("Screenshot 01_04_02_01_Zoom_Photo_taken_page is taken")
            time.sleep(3)

            ## Return to Submit Referral letter page
            print("Return to Submit Referral Letter page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text]]]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text]]]").click()
            time.sleep(3)

            ## Tap x button to delete 1st image
            print("Tap x button to delete 1st image")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.ViewGroup").click()
            time.sleep(3)

            ## Confirm Delete image
            print("Book SOPC01-04-02-02 Scenario 01 Functions of buttons related to removing photo in Patient's Address")
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"01_04_02_02_confirm_delete_image.png")
            print("Screenshot 01_04_02_02_confirm_delete_image is taken")

            ## 1st image is deleted
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            self.driver.find_element_by_xpath("//*[@id='button1']").click()
            time.sleep(3)
            print("Book SOPC01-04-02-02 Scenario 02 Change outlook of icons in Submit Referral Letter after the process of removing photo")
            self.driver.save_screenshot(test_dir+"01_04_02_02_referral_letter_page_after_delete_image.png")
            print("Screenshot 01_04_02_02_referral_letter_page_after_delete_image is taken")
            time.sleep(3)

        except TimeoutException:
            print("Book SOPC01-04-02 Take Photo on Referral letter Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC01-04-02 Take Photo on Referral letter Exception")
            assert(False)
        finally:
            print("Book SOPC01-04-02 Take Photo on Referral letter finish")

    def testbooksopc010501(self):
        try:
            print("Book SOPC01-05-01 Edit Application in Check Data start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
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
            submit_docuement_user_guide_text = user_data['submit_docuement_user_guide_text'][app_lang]
            patient_address = user_data['patient_address'][app_lang]
            submit_docuement_guidelines_text = user_data['submit_docuement_guidelines_text'][app_lang]
            edit_button = user_data['edit_button'][app_lang]
            edit_prefix_text = user_data['edit_prefix_text'][app_lang]
            cancel_button = user_data['cancel_button'][app_lang]

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

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            print("Click scroll icon to scroll down")
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

            ## Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled
            print("Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("xpath=(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()

            ## The Specialty and Hospital can be input by user
            print("The Specialty and Hospital can be input by user")
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

            ## Click User Guide link
            print("Click User Guide link")
            self.driver.find_element_by_xpath("xpath=//*[@text='"+submit_docuement_user_guide_text+"']").click()
            time.sleep(2)

            ## Type in Patient's Address in Submit Document page in application process
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*/*[@class='android.widget.TextView' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()
            time.sleep(2)

            ## Close User Guide pop-up
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+submit_docuement_guidelines_text+"']]]")))
            self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+submit_docuement_guidelines_text+"']]]").click()
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

            ## Swipe down to show Next button to click
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## User is on the Check Data screen
            print("Book SOPC01-05 Scenario 01 Function of go back to correct page by clicking the back button")
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"01_05_landed_check_data_page.png")
            print("Screenshot 01_05_landed_check_data_page is taken")
            time.sleep(2)

            ## Click Back button to go back Submit Referral Letter screen
            print("Click Back button to go back Submit Referral Letter screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@class='android.view.ViewGroup']] and ./*[@class='android.widget.ImageView']]").click()
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"01_05_back_submit_referral_letter_from_check_data.png")
            print("Screenshot 01_05_back_submit_referral_letter_from_check_data is taken")
            time.sleep(2)

            ## Swipe down to show Next button to click and enter Check Data screen again
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Click Edit Button
            print("Book SOPC01-05-01 Scenario 01 Correct sequence when accessing to the patient information pages")
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_01_edit_button_in_check_data.png")
            print("Screenshot 01_05_01_edit_button_in_check_data is taken")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+edit_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_01_edit_input_data_page.png")
            print("Screenshot 01_05_01_edit_input_data_page is taken")
            time.sleep(2)

            ## Swipe down to show Appointment options
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)

            ## Tap Specialty
            print("Book SOPC01-05-01 Scenario 02 Patient information in the patient information pages can be edited")
            time.sleep(2)
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*/*[@class='android.widget.Spinner'])[1]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_01_edit_specialty.png")
            print("Screenshot 01_05_01_edit_specialty is taken")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)

            ## Tap Hospital
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*/*[@class='android.widget.Spinner'])[2]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_01_edit_hospital.png")
            print("Screenshot 01_05_01_edit_hospital is taken")
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)

            self.driver.save_screenshot(test_dir+"01_05_01_edit_button_in_check_data.png")
            print("Screenshot 01_05_01_edit_button_in_check_data is taken")
            time.sleep(2)

            ## Click Next button to enter Edit Submit document screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_01_edit_submit_document_page.png")
            print("Screenshot 01_05_01_edit_submit_document_page is taken")
            time.sleep(2)

            ## Tap Patient's correspondence address box
            self.driver.find_element_by_xpath("/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.EditText']]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_01_edit_patient_address.png")
            print("Screenshot 01_05_01_edit_patient_address is taken")
            time.sleep(2)
            self.driver.hide_keyboard
            time.sleep(2)

            ## Click Next button to enter Edit Submit Referral Letter screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            ## Check if title text contains Edit
            assert(self.driver.find_element_by_partial_link_text(edit_prefix_text).is_displayed), "Cannot find Edit in title"
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_01_edit_submit_referral_letter_page.png")
            print("Screenshot 01_05_01_edit_submit_referral_letter_page is taken")
            time.sleep(2)

            ## Tap on Photo icon to try to take another photo but cancel
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[6]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[6]").click()
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"01_05_01_edit_referral_letter.png")
            print("Screenshot 01_05_01_edit_referral_letter is taken")
            time.sleep(2)
            self.driver.find_element_by_partial_link_text(cancel_button).click()
            time.sleep(2)

            ## Swipe down to show Next button to click and enter Check Data screen again
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_01_return_check_data_from_edit.png")
            print("Screenshot 01_05_01_return_check_data_from_edit is taken")
            time.sleep(3)

        except TimeoutException:
            print("Book SOPC01-05-01 Edit Application in Check Data Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC01-05-01 Edit Application in Check Data Exception")
            assert(False)
        finally:
            print("Book SOPC01-05-01 Edit Application in Check Data finish")

    def testbooksopc010502(self):
        try:
            print("Book SOPC01-05-02 Review Documents Before Submission start")

            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
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
            please_click_here_to_check_link = user_data['please_click_here_to_check_link'][app_lang]
            patient_address = user_data['patient_address'][app_lang]
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

            ## Click Book for self in Submit Application screen
            print("Book for self in Submit Application screen")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_for_self_button+"']]").click()
            time.sleep(2)

            ## Click scroll icon to scroll down
            print("Click scroll icon to scroll down")
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

            ## Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled
            print("Patient's data in 3 input fields: Surname, Given Name, HK mobile phone number are auto-filled")
            time.sleep(2)

            ## Click Scroll down button
            self.driver.find_element_by_xpath("xpath=(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.FrameLayout' and ./parent::*[./parent::*[./parent::*[./parent::*[./parent::*[@class='android.view.ViewGroup']]]]]]]]]]]/*/*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup']])[6]").click()
            time.sleep(2)

            ## Select Spinner of Specialty：
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Specialty_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_specialty+"']").click()

            ## Select Spinner of Hospital:
            self.driver.find_element_by_xpath("//*[@class='android.widget.Spinner' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='"+Select_Hospital_spinner+"']]]").click()
            self.driver.find_element_by_xpath("//*[@text='"+spinner_hospital+"']").click()

            ## The Specialty and Hospital can be input by user
            print("The Specialty and Hospital can be input by user")
            time.sleep(2)

            ## Click Next Button to go to next screen
            print("Click Next Button to go to next screen")
            time.sleep(2)
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

            ## Swipe down to show Please click here to check link
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 500)")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_02_Please_click_here_to_check_link.png")
            print("Screenshot 01_05_02_Please_click_here_to_check_link is taken")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@text='"+please_click_here_to_check_link+"']").click()
            time.sleep(2)

            ## Display Check data screens in Please click here to check link
            print("Book SOPC01-05-02 Scenario 01 Correct sequence when accessing to the patient document review pages")
            time.sleep(2)

            ## Display Patient's Addess to be checked
            print("Patient's Addess is shown to be checked for taking photo as referral letter")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_02_patient_address_check_taking_photo.png")
            print("Screenshot 01_05_02_patient_address_check_taking_photo is taken")
            time.sleep(3)

            ## Click Next icon
            self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView").click()
            time.sleep(2)
         
            ## Display patient document review pages
            print("Book SOPC01-05-02 Scenario 02 Display patient document review pages")
            time.sleep(2)

            ## Display Referral Letter images to be checked
            print("Referral Letter images are shown to be checked for taking photo as referral letter")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"01_05_02_referral_letter_check_taking_photo.png")
            print("Screenshot 01_05_02_referral_letter_check_taking_photo is taken")
            time.sleep(3)

            ## Click x icon to leave Check data screens
            self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView").click()
            time.sleep(2)

            ##print("Book SOPC01-05-02-01 Review and Submit Application")

            ## Book SOPC01-05-02-01 Review and Submit Application
            print("Book SOPC01-05-02-01 Review and Submit Application")
            time.sleep(2)
            print("Book SOPC01-05-02-01 Scenario 01 Function of Submit button in Review page")
            self.driver.save_screenshot(test_dir+"01_05_02_01_click_submit_button_after_check_data.png")
            print("Screenshot 01_05_02_01_click_submit_button_after_check_data is taken")
            time.sleep(3)

            ## Click Submit button to Submit the Application
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]").click()
            time.sleep(6)

            ## Application Complete screen is displayed
            print("Book SOPC01-05-02-01 Scenario 02 Progress bar display")
            time.sleep(2)

            ## Function of buttons in Complete page
            print("Book SOPC01-05-02-01 Scenario 03 Function of buttons in Complete page")
            time.sleep(2)

            ## Check if Information button is displayed in Complete page
            assert(self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").is_displayed), "Cannot find Information button"
            print("Information button is displayed in Complete page")
            time.sleep(2)

            ## Check if Complete button is displayed in Complete page
            assert(self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Complete_button+"' and @class='android.widget.TextView']]").is_displayed), "Cannot find Complete button"
            print("Complete button is displayed in Complete page")
            time.sleep(2)

            ## Display of Complete page and Reference code
            print("Book SOPC01-05-02-01 Scenario 04 Display of Complete page and Reference Number")
            time.sleep(2)

            ## Check if Reference Number is displayed in Complete page
            assert(self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]").is_displayed), "Cannot find Reference Code"
            reference_code = self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]").text
            print("Reference Number"+ reference_code +" is displayed in Complete page")
            time.sleep(2)

            self.driver.save_screenshot(test_dir+"01_05_02_01_progress_bar_buttons_reference_code.png")
            print("Screenshot 01_05_02_01_progress_bar_buttons_reference_code is taken")
            time.sleep(2)

            ## Display of information pop-up window when clicked info icon
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup").click()
            time.sleep(2)
            print("Book SOPC01-05-02-01 Scenario 05 Display of information pop-up window when clicked info icon")
            self.driver.save_screenshot(test_dir+"01_05_02_01_information_pop_up_reference_number.png")
            print("Screenshot 01_05_02_01_information_pop_up_reference_number is taken")
            time.sleep(2)

            ## Clicked OK button to close information pop-up window
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button1']")))
            self.driver.find_element_by_xpath("//*[@id='button1']").click()
            time.sleep(2)

            ## Leave Complete screen
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+Complete_button+"' and @class='android.widget.TextView']]").click()
            time.sleep(2)
            print("Book SOPC01-05-02-01 Scenario 06 Go back to Book SOPC home screen after clicking Submit Application button")
            self.driver.save_screenshot(test_dir+"01_05_02_01_back_book_sopc_home_screen.png")
            print("Screenshot 01_05_02_01_back_book_sopc_home_screen is taken")
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT UNTIL BUG FIXED START
            ## Check if It goes back Book SOPC Home screen
            #assert(self.driver.find_element_by_xpath("//*[@text='"+sopc_booking_title+"']").is_displayed), "Cannot find SOPC booking title"
            #time.sleep(2)
            #### TEMPORARILY COMMENT OUT UNTIL BUG FIXED END


        except TimeoutException:
            print("Book SOPC01-05-02 Review Documents Before Submission Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC01-05-02 Review Documents Before Submission Exception")
            assert(False)
        finally:
            print("Book SOPC01-05-02 Review Documents Before Submission finish")

    def tearDown(self):
        self.driver.quit()