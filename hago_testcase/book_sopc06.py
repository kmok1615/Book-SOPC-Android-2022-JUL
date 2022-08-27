# coding=UTF-8
'''
Created on 2022.07.07
Updated on 2022.07.19
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

class TestBookSOPC06(unittest.TestCase):

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

    def testbooksopc0600(self):
        try:
            print("Book SOPC06-00 Enquiry My Application Status start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Access to Enquiry Status
            print("Book SOPC06-00 Scenario 01 Access to My Application Status page")
            self.driver.save_screenshot(test_dir+"06_00_Access_My_Application_Status.png")
            print("Screenshot 06_00_Access_My_Application_Status is taken")
            time.sleep(2)

            ## Outlook of My Application Status
            print("Book SOPC06-00 Scenario 02 Outlook of My Application Status page")
            self.driver.save_screenshot(test_dir+"06_00_My_Application_Status_screen.png")
            print("Screenshot 06_00_My_Application_Status_screen is taken")
            time.sleep(2)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC06-00 Enquiry My Application Status Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-00 Enquiry My Application Status Exception")
            assert(False)
        finally:
            print("Book SOPC06-00 Enquiry My Application Status finish")

    def testbooksopc0601(self):
        try:
            print("Book SOPC06-01 In Progress Application start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_06_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_01_invalid']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_01']
            patient_reference_number_invalid = user_data['patient_reference_number_invalid']
            patient_reference_number_valid = user_data['patient_reference_number_06_01']
            next_button = user_data['next_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            reference_number_title = user_data['reference_number_title'][app_lang]
            cancel_button = user_data['cancel_button'][app_lang]
            cancel_application_button = user_data['cancel_application_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

            ## Input incomplete Reference number
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.ImageView']]]").send_keys(patient_reference_number_invalid)
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click Next Button with incomplete reference number
            print("Click Next Button with incomplete reference number")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Pop-up to reminder user that invalid reference code is displayed
            print("Pop-up to reminder user that invalid reference code is displayed")
            self.driver.save_screenshot(test_dir+"06_01_invalid_reference_number.png")
            print("Screenshot 06_01_invalid_reference_number is taken")

            ## Click OK Button to close pop-up
            print("Click OK Button to close pop-up")
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+OK_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+OK_button+"']]").click()
            time.sleep(2)

            ## Clear Reference number field
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.ImageView']]]").clear()
            time.sleep(2)

            ## Input invalid Reference number
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.ImageView']]]").send_keys(patient_reference_number_valid)
            time.sleep(2)

            ## Click Reference Number title to remove cursor
            self.driver.find_element_by_xpath("//*[@text='"+reference_number_title+"']").click()
            time.sleep(2)

            ## Click Next Button with invalid reference number
            print("Click Next Button with valid reference number")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Pop-up to reminder user that invalid HKID/HKBC is displayed
            print("Pop-up to reminder user that invalid HKID/HKBC is displayed")
            self.driver.save_screenshot(test_dir+"06_01_invalid_HKID_HKBC.png")
            print("Screenshot 06_01_invalid_HKID_HKBC is taken")

            ## Click OK Button to close pop-up
            print("Click OK Button to close pop-up")
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+OK_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+OK_button+"']]").click()
            time.sleep(2)

            ## Clear HKID/HK Birth Certificate number
            print("Clear HKID/HK Birth Certificate number")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").clear()
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").clear()
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").clear()
            time.sleep(2)

            ## Set valid HKID/HK Birth Certificate number
            patient_HKID_Letter = user_data['HKID_Letter_06_01']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_01']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_01']

            ## Input Valid HKID/HK Birth Certificate number
            print("Input Valid HKID/HK Birth Certificate number")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click Back key to remove keyboard
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click Next Button with valid reference number and HKID/HKBC
            print("Book SOPC06-01 Scenario 04 Click Next Button with valid reference number and HKID/HKBC")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Detail of "In-Progress" application
            print("Book SOPC06-01 Scenario 05 Display screen of Detail of 'In-Progress' application")
            self.driver.save_screenshot(test_dir+"06_01_My_Application_In_Progress_screen.png")
            print("Screenshot 06_01_My_Application_In_Progress_screen is taken")
            time.sleep(2)

            ## Click Cancel Application Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+cancel_application_button+"']]")))
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+cancel_application_button+"']]").click()
            time.sleep(2)

            ## Process of button 'Cancel My Application'
            print("Book SOPC06-01 Scenario 06 Process of button 'Cancel My Application'")
            self.driver.save_screenshot(test_dir+"06_01_Confirm_to_Cancel_screen.png")
            print("Screenshot 06_01_Confirm_to_Cancel_screen is taken")
            time.sleep(2)

            ## Click Cancel Button
            self.driver.find_element_by_link_text(cancel_button).click()
            time.sleep(4)


        except TimeoutException:
            print("Book SOPC06-01 In Progress Application Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-01 In Progress Application Exception")
            assert(False)
        finally:
            print("Book SOPC06-01 In Progress Application finish")

    def testbooksopc0602(self):
        try:
            print("Book SOPC06-02 Application Requires Contact and Re-submission start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_06_02']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_02']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_02']
            patient_reference_number = user_data['patient_reference_number_06_02']
            next_button = user_data['next_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            call_later_button = user_data['call_later_button'][app_lang]
            CONFIRM_button = user_data['CONFIRM_button'][app_lang]
            patient_address = user_data['patient_address_02_01'][app_lang]
            please_click_here_to_check_link = user_data['please_click_here_to_check_link'][app_lang]
            patient_correspondence_address_text = user_data['patient_correspondence_address_text'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

            ## Display screen of Detail of Application Requires Contact and Re-submission
            print("Book SOPC06-02 Scenario 01 Patient's data in 2 input fields: Reference number, HKID/Birth Certificate Number")
            self.driver.save_screenshot(test_dir+"06_02_application_contact_resubmission_screen.png")
            print("Screenshot 06_02_application_contact_resubmission_screen is taken")
            time.sleep(2)

            ## Hospital spinner field
            print("Book SOPC06-02 Scenario 02 Hospital spinner field")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_02_My_Application_Status_hospital_spinner.png")
            print("Screenshot 06_02_My_Application_Status_hospital_spinner is taken")
            time.sleep(2)

            ## Click the 1st available item in Spinner
            print("Click the 1st available item in Spinner")
            self.driver.find_element_by_xpath("(//*[@class='android.widget.ListView']/*[@text and @id='text1'])[1]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_02_My_Application_Status_selected_1st_hospital_spinner.png")
            print("Screenshot 06_02_My_Application_Status_selected_1st_hospital_spinner is taken")
            time.sleep(2)

            ## Clear Reference number field
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").clear()
            time.sleep(2)

            ## Input Reference number of Application Requires Contact and Re-submission
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").send_keys(patient_reference_number)
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click Next Button with Reference number of Application Requires Contact and Re-submission
            print("Book SOPC06-02 Scenario 03 Click Next Button")
            time.sleep(2)
            print("Click Next Button with Reference number of Application Requires Contact and Re-submission")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Detail of Application Requires Contact and Re-submission
            print("Book SOPC06-02 Scenario 04 Display screen of Detail of Application Requires Contact and Re-submission")
            self.driver.save_screenshot(test_dir+"06_02_application_contact_resubmission_screen.png")
            print("Screenshot 06_02_application_contact_resubmission_screen is taken")
            time.sleep(2)

            ## Process of button 'Cancel My reservation' and 'Next'
            print("Book SOPC06-02 Scenario 05 Process of button 'Cancel My reservation' and 'Next'")
            time.sleep(2)

            ## Swipe down to show Next button
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 800)")
            time.sleep(2)

            ## Click Next to open Pop-up box of Call
            print("Click Next to open Pop-up box of Call")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)
            self.driver.save_screenshot(test_dir+"06_02_application_contact_pop_up_window.png")
            print("Screenshot 06_02_application_contact_pop_up_window is taken")
            time.sleep(2)

            ## Process of button "Call Later" and "Call" in Pop-up box
            print("Book SOPC06-02 Scenario 06 Process of button 'Call Later' and 'Call' in Pop-up box")
            time.sleep(2)

            ## Click Call Later to close Pop-up box of Call
            print("Click Call Later to close Pop-up box of Call")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,call_later_button)))
            self.driver.find_element_by_link_text(call_later_button).click()
            time.sleep(2)

            ## Process of button 'Cancel My reservation' and 'Next' after clicking 'Call Later'
            print("Book SOPC06-02 Scenario 07 Process of button 'Cancel My reservation' and 'Next' after clicking 'Call Later'")
            time.sleep(2)

            ## Click Next to go to Document Re-submission/
            print("Click Next to go to Document Re-submission")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Document Re-submission
            print("Book SOPC06-02 Scenario 08 Display screen of Document Re-submission")
            time.sleep(2)

            self.driver.save_screenshot(test_dir+"06_02_Document_resubmission.png")
            print("Screenshot 06_02_Document_resubmission is taken")
            time.sleep(2)

            ## Functions of buttons of taking photo and inputing address
            print("Book SOPC06-02 Scenario 09 Functions of buttons of taking photo and inputing address")
            time.sleep(2)

            ## Click Open Take Photo interface button in Submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)

            self.driver.save_screenshot(test_dir+"06_02_take_photo_interface.png")
            print("Screenshot 06_02_take_photo_interface is taken")
            time.sleep(2)

            ## Click Take Photo button to take photo of document
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Photo of document can be taken
            self.driver.save_screenshot(test_dir+"06_02_take_photo_document_done.png")
            print("Screenshot 06_02_take_photo_document_done is taken")
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+OK_button+"']").click()
            time.sleep(3)

            ## Change outlook of icons in Patient's Address after the process of Take Photo
            self.driver.save_screenshot(test_dir+"06_02_patient_address_after_taking_photo_document.png")
            print("Screenshot 06_02_Npatient_address_after_taking_photo_document is taken")
            time.sleep(2)

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
            self.driver.save_screenshot(test_dir+"06_02_typing_patient_address_box.png")
            print("Screenshot 06_02_Ntyping_patient_address_box is taken")
            time.sleep(2)

            ## Input Patient's address
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText']").send_keys(patient_address)
            time.sleep(2)
            self.driver.hide_keyboard
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_02_typing_patient_address_box.png")
            print("Screenshot 06_02_typing_patient_address_box is taken")
            
            ## Click Take Photo button to remove cursor
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()

            ## Click Next to go next page
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT SCANNING REFERRAL LETTER SCREEN NOT AVAILABLE START
            ## Screen of scan QR code on Referral letter
            #print("Book SOPC06-02 Scenario 10 Screen of scan QR code on Referral letter")
            #time.sleep(2)

            ## Functions of buttons of Other Referral letter
            #print("Book SOPC06-02 Scenario 11 Functions of buttons of Other Referral letter")
            #time.sleep(2)

            #### TEMPORARILY COMMENT OUT SCANNING REFERRAL LETTER SCREEN NOT AVAILABLE END

            ## Screen of Review Document
            print("Book SOPC06-02 Scenario 12 Screen of Review Document")
            self.driver.save_screenshot(test_dir+"06_02_check_data_screen.png")
            print("Screenshot 06_02_check_data_screen is taken")
            time.sleep(2)

            ## Functions of buttons in Review Document
            print("Book SOPC06-02 Scenario 13 Functions of buttons in Review Document")
            time.sleep(2)

            ## Click Please click here to check link
            self.driver.find_element_by_link_text(please_click_here_to_check_link).click()
            time.sleep(2)

            ## Screen of check Patient's Correspondence Address in Review Document
            self.driver.save_screenshot(test_dir+"06_02_check_patient_address_screen.png")
            print("Screenshot 06_02_check_patient_address_screen is taken")
            time.sleep(2)

            ## Click x button to exit
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text='"+patient_correspondence_address_text+"']]]").click()
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT SINCE RESUBMIT OF APPLICATION SHOULD NOT BE PERFORMED START
            #print("Book SOPC06-02 Scenario 14 Submit button")
            #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,resubmit_button)))
            #self.driver.find_element_by_link_text(resubmit_button).click()
            #time.sleep(2)
            #### TEMPORARILY COMMENT OUT SINCE RESUBMIT OF APPLICATION SHOULD NOT BE PERFORMED END

        except TimeoutException:
            print("Book SOPC06-02 Application Requires Contact and Re-submission Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-02 Application Requires Contact and Re-submission Exception")
            assert(False)
        finally:
            print("Book SOPC06-02 Application Requires Contact and Re-submission finish")

    def testbooksopc0603(self):
        try:
            print("Book SOPC06-03 Application Requires Re-submission start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_06_03']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_03']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_03']
            patient_reference_number = user_data['patient_reference_number_06_03']
            next_button = user_data['next_button'][app_lang]
            OK_button = user_data['OK_button'][app_lang]
            Low_Case_Confirm_button = user_data['Low_Case_Confirm_button'][app_lang]
            please_click_here_to_check_link = user_data['please_click_here_to_check_link'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

            ## Patient's data in 2 input fields: Reference number, HKID/Birth Certificate Number
            print("Book SOPC06-03 Scenario 01 Patient's data in 2 input fields: Reference number, HKID/Birth Certificate Number")
            self.driver.save_screenshot(test_dir+"06_03_application_resubmission_screen.png")
            print("Screenshot 06_03_application_resubmission_screen is taken")
            time.sleep(2)

            ## Hospital spinner field
            print("Book SOPC06-03 Scenario 02 Hospital spinner field")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_03_My_Application_Status_hospital_spinner.png")
            print("Screenshot 06_03_My_Application_Status_hospital_spinner is taken")
            time.sleep(2)

            ## Click the 1st available item in Spinner
            print("Click the 1st available item in Spinner")
            self.driver.find_element_by_xpath("(//*[@class='android.widget.ListView']/*[@text and @id='text1'])[1]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_03_My_Application_Status_selected_1st_hospital_spinner.png")
            print("Screenshot 06_03_My_Application_Status_selected_1st_hospital_spinner is taken")
            time.sleep(2)

            ## Clear Reference number field
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").clear()
            time.sleep(2)

            ## Input Reference number of Application Requires Re-submission
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").send_keys(patient_reference_number)
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Next Button
            print("Book SOPC06-03 Scenario 3 Next Button")
            print("Click Next Button with Reference number of Application Requires Re-submission")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Detail of application requires Re-submission Only
            print("Book SOPC06-03 Scenario 04 Display screen of Detail of application requires Re-submission Only")
            self.driver.save_screenshot(test_dir+"06_03_application_resubmission_screen.png")
            print("Screenshot 06_03_application_resubmission_screen is taken")
            time.sleep(2)

            ## Process of button 'Cancel My reservation' and 'Next'
            print("Book SOPC06-03 Scenario 05 Process of button 'Cancel My reservation' and 'Next'")
            time.sleep(2)

            ## Swipe down to show Next button
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 800)")
            time.sleep(2)

            ## Click Next to go to Document Re-submission/
            print("Click Next to go to Document Re-submission")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Patient's Information Re-submission
            print("Book SOPC06-03 Scenario 06 Display screen of Patient's Information Re-submission")
            time.sleep(2)

            self.driver.save_screenshot(test_dir+"06_03_Document_resubmission.png")
            print("Screenshot 06_03_Document_resubmission is taken")
            time.sleep(2)

            ## Functions of buttons of Patient's Information Re-submission
            print("Book SOPC06-03 Scenario 07 Functions of buttons of Patient's Information Re-submission")
            time.sleep(2)

            ## Click Open Take Photo interface button in Re-submit Document page
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_03_function_take_photo.png")
            print("Screenshot 06_03_function_take_photo is taken")
            time.sleep(2)

            # Default option is Hong Kong Identity Card and click Confirm
            print("Click Confirm with selecting Hong Kong Identity Card")
            self.driver.find_element_by_xpath("//*[@text='"+Low_Case_Confirm_button+"']").click()

            ## Functions of buttons related to taking photo of Patient's HKID after selecting HKID
            self.driver.save_screenshot(test_dir+"06_03_take_photo_interface_HKID.png")
            print("Screenshot 06_03_take_photo_interface_HKID is taken")
            time.sleep(2)

            ## Click Take Photo button to take photo of HKID/HKBC
            self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]/*[@class='android.view.ViewGroup'])[4]/*/*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']])[1]").click()
            time.sleep(2)

            ## Photo of document can be taken
            self.driver.save_screenshot(test_dir+"06_03_take_photo_document_done.png")
            print("Screenshot 06_03_take_photo_document_done is taken")
            time.sleep(2)

            ## Confirm Taken Photo of document is used
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='"+OK_button+"']")))
            self.driver.find_element_by_xpath("xpath=//*[@text='"+OK_button+"']").click()
            time.sleep(3)

            ## Change outlook of icons in Patient's HKID after the process of Take Photo
            self.driver.save_screenshot(test_dir+"06_03_patient_HKID_after_taking_photo_document.png")
            print("Screenshot 06_03_patient_HKID_after_taking_photo_document is taken")
            time.sleep(2)

            ## Tap Zoom button
            print("Tap Zoom button to open photo page")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]")))
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_03_Zoom_Photo_taken_page.png")
            print("Screenshot 06_03_Zoom_Photo_taken_page is taken")
            time.sleep(2)

            ## Return to screen of Patient's Information Re-submission
            print("Return to screen of Patient's Information Re-submission")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text]]]")))
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text]]]").click()
            time.sleep(2)

            ## Click Next to go next page
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT SCANNING REFERRAL LETTER SCREEN NOT AVAILABLE START
            #print("Book SOPC06-03 Scenario 8 Display screen of Document Re-submission")
            #print("Book SOPC06-03 Scenario 9 Screen of scan QR code on Referral letter")
            #print("Book SOPC06-03 Scenario 10 Functions of buttons of Other Referral letter")
            #### TEMPORARILY COMMENT OUT SCANNING REFERRAL LETTER SCREEN NOT AVAILABLE END

            ## Screen of Review Document
            print("Book SOPC06-03 Scenario 11 Screen of Review Document")
            self.driver.save_screenshot(test_dir+"06_03_check_data_screen.png")
            print("Screenshot 06_03_check_data_screen is taken")
            time.sleep(2)

            ## Functions of buttons in Review Document
            print("Book SOPC06-03 Scenario 12 Functions of buttons in Review Document")
            time.sleep(2)

            ## Click Please click here to check link
            self.driver.find_element_by_link_text(please_click_here_to_check_link).click()
            time.sleep(2)

            ## Screen of check Patient's HKID in Review Document
            self.driver.save_screenshot(test_dir+"06_03_check_patient_HKID_screen.png")
            print("Screenshot 06_03_check_patient_HKID_screen is taken")
            time.sleep(2)

            ## Click x button to exit
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@text]]]").click()
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT SINCE RESUBMIT OF APPLICATION SHOULD NOT BE PERFORMED START
            #print("Book SOPC06-03 Scenario 13 Screen of Finish Submission")
            #print("Book SOPC06-03 Scenario 14 Finish Button")
            #### TEMPORARILY COMMENT OUT SINCE RESUBMIT OF APPLICATION SHOULD NOT BE PERFORMED END

        except TimeoutException:
            print("Book SOPC06-03 Application Requires Re-submission Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-03 Application Requires Re-submission Exception")
            assert(False)
        finally:
            print("Book SOPC06-03 Application Requires Re-submission finish")

    def testbooksopc0604(self):
        try:
            print("Book SOPC06-04 My Application Status - Application Completed start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_06_04']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_04']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_04']
            patient_reference_number = user_data['patient_reference_number_06_04']
            next_button = user_data['next_button'][app_lang]
            cancel_appointment_button = user_data['cancel_appointment_button'][app_lang]
            CONFIRM_button = user_data['CONFIRM_button'][app_lang]
            other_remarks_link = user_data['other_remarks_link'][app_lang]
            add_to_calendar_button = user_data['add_to_calendar_button'][app_lang]
            close_button = user_data['close_button'][app_lang]
            no_button = user_data['no_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

            ## Patient's data in 2 input fields: Reference number, HKID/Birth Certificate Number
            print("Book SOPC06-04 Scenario 01 Patient's data in 2 input fields: Reference number, HKID/Birth Certificate Number")
            self.driver.save_screenshot(test_dir+"06_04_My_Application_Status_landing_page.png")
            print("Screenshot 06_04_My_Application_Status_landing_page is taken")
            time.sleep(2)

            ## Hospital spinner field
            print("Book SOPC06-04 Scenario 02 Hospital spinner field")
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_04_My_Application_Status_hospital_spinner.png")
            print("Screenshot 06_04_My_Application_Status_hospital_spinner is taken")
            time.sleep(2)

            ## Click the 1st available item in Spinner
            print("Click the 1st available item in Spinner")
            self.driver.find_element_by_xpath("(//*[@class='android.widget.ListView']/*[@text and @id='text1'])[1]").click()
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_04_My_Application_Status_selected_1st_hospital_spinner.png")
            print("Screenshot 06_04_My_Application_Status_selected_1st_hospital_spinner is taken")
            time.sleep(2)

            ## Clear Reference number field
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").clear()
            time.sleep(2)
            
            ## Input Reference number of Application Completed
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").send_keys(patient_reference_number)
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Next button
            print("Book SOPC06-03 Scenario 03 Next button")
            print("Click Next Button with Reference number of Application Completed")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Detail of 'Completed' Application
            print("Book SOPC06-03 Scenario 04 Display screen of Detail of 'Completed' Application")
            self.driver.save_screenshot(test_dir+"06_04_application_completed_screen.png")
            print("Screenshot 06_04_application_completed_screen is taken")
            time.sleep(2)

            ## Swipe down to show bottom part of screen
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 800)")
            time.sleep(4)

            ## Process of link "Other Remarks"
            print("Book SOPC06-04 Scenario 05 Process of link 'Other Remarks'")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT,other_remarks_link)))
            self.driver.find_element_by_partial_link_text(other_remarks_link).click()
            time.sleep(4)

            ## Display screen of Other Remarks
            print("Display screen of Other Remarks")
            self.driver.save_screenshot(test_dir+"06_04_other_remarks_screen.png")
            print("Screenshot 06_04_other_remarks_screen is taken")
            time.sleep(2)

            ## Click Close button
            print("Click Close button")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,close_button)))
            self.driver.find_element_by_link_text(close_button).click()
            time.sleep(2)

            ## Process of button 'Cancel My reservation' and 'Add to Calendar'
            print("Book SOPC06-04 Scenario 06 Process of button 'Cancel My reservation' and 'Add to Calendar'")
            time.sleep(2)

            ## Click Add to Calendar
            print("Click Add to Calendar")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,add_to_calendar_button)))
            self.driver.find_element_by_link_text(add_to_calendar_button).click()
            time.sleep(4)

            ## Display Pop-up box to confirm adding reservation to calender
            print("Book SOPC06-04-01 Scenario 01 Display Pop-up box to confirm adding reservation to calender")
            time.sleep(4)
            self.driver.save_screenshot(test_dir+"06_04_01_confirm_adding_reservation_to_calendar.png")
            print("Screenshot 06_04_01_confirm_adding_reservation_to_calendar is taken")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,CONFIRM_button)))
            self.driver.find_element_by_link_text(CONFIRM_button).click()

            ## Select Use Once on device
            print("Select use device calendar once")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='button_once']")))
            self.driver.find_element_by_xpath("//*[@id='button_once']").click()
            time.sleep(4)

            ## Display New Event sheet
            print("Book SOPC06-04-01 Scenario 02 Display New Event sheet")
            time.sleep(4)
            self.driver.save_screenshot(test_dir+"06_04_01_device_calendar_event_sheet.png")
            print("Screenshot 06_04_01_device_calendar_event_sheet is taken")
            time.sleep(2)

            ## Save Event in Device by clicking Done
            print("Save Event in Device by clicking Done")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='add_app_bar_menu_done']")))
            self.driver.find_element_by_xpath("//*[@id='add_app_bar_menu_done']").click()
            time.sleep(4)
            #self.driver.save_screenshot(test_dir+"06_04_01_use_device_calendar_once.png")
            #print("Screenshot 06_04_01_use_device_calendar_once is taken")
            time.sleep(2)

            ## Display Pop-up box to inform user added event  to calendar successfully
            print("Book SOPC06-04-01 Scenario 03 Display Pop-up box to inform user added event to calendar successfully")
            time.sleep(4)
            self.driver.save_screenshot(test_dir+"06_04_01_event_add_success.png")
            print("Screenshot 06_04_01_event_add_success is taken")
            time.sleep(2)

            ## Click CONFIRM button to close
            print("Click CONFIRM button to close")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,CONFIRM_button)))
            self.driver.find_element_by_link_text(CONFIRM_button).click()

            ## Display Pop-up box to confirm cancelling application
            print("Book SOPC06-04-02 Scenario 01 Display Pop-up box to confirm cancelling application")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,cancel_appointment_button)))
            self.driver.find_element_by_link_text(cancel_appointment_button).click()
            time.sleep(4)
            self.driver.save_screenshot(test_dir+"06_04_02_pop_up_confirm_cancelling_application.png")
            print("Screenshot 06_04_02_pop_up_confirm_cancelling_application is taken")
            time.sleep(2)

            ## Click No button to abort
            print("Click No button to abort")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,no_button)))
            self.driver.find_element_by_link_text(no_button).click()
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT SINCE CANCEL APPOINTMENT SHOULD NOT BE PERFORMED START
            #print("Book SOPC06-04-02 Scenario 02 Display screen of Cancel Application completed")
            #print("Book SOPC06-04-02 Scenario 03 Go back to My Application Status landing page by clicking back icon")
            #### TEMPORARILY COMMENT OUT SINCE CANCEL APPOINTMENT SHOULD NOT BE PERFORMED END

        except TimeoutException:
            print("Book SOPC06-04 My Application Status - Application Completed Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-04 My Application Status - Application Completed Exception")
            assert(False)
        finally:
            print("Book SOPC06-04 My Application Status - Application Completed finish")


    def testbooksopc0605(self):
        try:
            print("Book SOPC06-05 My Application Status - Cancel Application (Status = In Progress, not yet booked) start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_06_06']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_05']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_05']
            patient_reference_number = user_data['patient_reference_number_06_05']
            next_button = user_data['next_button'][app_lang]
            cancel_application_button = user_data['cancel_application_button'][app_lang]
            confirm_button = user_data['Low_Case_Confirm_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

            ## Input Reference number of Cancel Application in Status Confirmed
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").send_keys(patient_reference_number)
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click Next Button with reference number and HKID/HKBC of Cancel Application in Status Confirmed 
            print("Click Next Button with reference number and HKID/HKBC of Cancel Application in Status Confirmed")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)
            
            ## Display screen of Application in progress
            print("Display screen of Application in progress")
            self.driver.save_screenshot(test_dir+"06_05_Application_in_progress_screen.png")
            print("Screenshot 06_05_Application_in_progress_screen is taken")
            time.sleep(2)

            ## Click Cancel Application Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+cancel_application_button+"']]")))
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+cancel_application_button+"']]").click()
            time.sleep(2)

            ## Display Pop-up box to confirm cancelling application in progress
            print("Book SOPC06-05 Scenario 01 Display Pop-up box to confirm cancelling application'")
            self.driver.save_screenshot(test_dir+"06_05_Confirm_to_Cancel_screen.png")
            print("Screenshot 06_05_Confirm_to_Cancel_screen is taken")
            time.sleep(4)

            ## Click Cancel Application Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,confirm_button)))
            self.driver.find_element_by_link_text(confirm_button).click()
            time.sleep(2)

            ## Display screen of Cancel Application completed
            print("Book SOPC06-05 Scenario 02 Display screen of Cancel Application completed")
            self.driver.save_screenshot(test_dir+"06_05_Cancel_Application_completed_screen.png")
            print("Screenshot 06_05_Confirm_to_Cancel_screen is taken")
            time.sleep(4)
            
            ## Go back to My Application Status landing page by clicking back icon
            print("Book SOPC06-05 Scenario 03 Go back to My Application Status landing page by clicking back icon")
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]").click()
            time.sleep(4)
            self.driver.save_screenshot(test_dir+"06_05_Back_My_Application_Status_landing_page.png")
            print("Screenshot 06_05_Back_My_Application_Status_landing_page is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC06-05 My Application Status - Cancel Application (Status = In Progress, not yet booked) Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-05 My Application Status - Cancel Application (Status = In Progress, not yet booked) Exception")
            assert(False)
        finally:
            print("Book SOPC06-05 My Application Status - Cancel Application (Status = In Progress, not yet booked) finish")

    def testbooksopc0606(self):
        try:
            print("Book SOPC06-06 My Application Status - Cancel Application (Status = Confirmed) start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_06_06']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_06']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_06']
            patient_reference_number = user_data['patient_reference_number_06_06']
            next_button = user_data['next_button'][app_lang]
            cancel_application_button = user_data['cancel_application_button'][app_lang]
            cancel_button = user_data['cancel_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

            ## Input Reference number of Cancel Application in Status Confirmed
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").send_keys(patient_reference_number)
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click Next Button with reference number and HKID/HKBC of Cancel Application in Status Confirmed 
            print("Click Next Button with reference number and HKID/HKBC of Cancel Application in Status Confirmed")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Application with insufficient information
            print("Display screen of Application with insufficient information")
            self.driver.save_screenshot(test_dir+"06_06_Application_with_insufficient_information_screen.png")
            print("Screenshot 06_06_Application_with_insufficient_information_screen is taken")
            time.sleep(2)

            ## Click Cancel Application Button
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+cancel_application_button+"']]")))
            self.driver.find_element_by_xpath("xpath=//*[@class='android.view.ViewGroup' and ./*[@text='"+cancel_application_button+"']]").click()
            time.sleep(2)

            ## Process of button 'Cancel My Application'
            print("Book SOPC06-06 Scenario 01 Process of button 'Cancel My Application'")
            self.driver.save_screenshot(test_dir+"06_06_Confirm_to_Cancel_screen.png")
            print("Screenshot 06_06_Confirm_to_Cancel_screen is taken")
            time.sleep(2)

            #### TEMPORARILY COMMENT OUT SINCE CANCELLING OF APPLICATION IN STATUS CONFIRMED SHOULD NOT BE PERFORMED START
            #print("Book SOPC06-06 Scenario 2 Display screen of Cancel Application completed")
            ## Click Cancel Application Button
            #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(By.LINK_TEXT,Low_Case_Confirm_button))
            #self.driver.find_element_by_link_text(Low_Case_Confirm_button).click()
            #time.sleep(2)
            #### TEMPORARILY COMMENT OUT SINCE CANCELLING OF APPLICATION IN STATUS CONFIRMED SHOULD NOT BE PERFORMED END

            ## Click Cancel Button
            self.driver.find_element_by_link_text(cancel_button).click()
            time.sleep(4)

        except TimeoutException:
            print("Book SOPC06-06 My Application Status - Cancelled Appointment Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-06 My Application Status - Cancelled Appointment Exception")
            assert(False)
        finally:
            print("Book SOPC06-06 My Application Status - Cancelled Appointment finish")


    def testbooksopc0607(self):
        try:
            print("Book SOPC06-07 My Application Status - Cancelled Appointment start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_06_07']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_07']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_07']
            patient_reference_number_06_07 = user_data['patient_reference_number_06_07']
            next_button = user_data['next_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

            ## Input Reference number of Cancelled Application
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").send_keys(patient_reference_number_06_07)
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click Next Button with reference number and HKID/HKBC of Cancelled 
            print("Click Next Button with reference number and HKID/HKBC of Cancelled")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Cancelled Appointment
            print("Book SOPC06-07 Scenario 01 Display screen of Cancelled Appointment")
            self.driver.save_screenshot(test_dir+"06_07_Cancelled_My_Application_screen.png")
            print("Screenshot 06_07_Cancelled_My_Application_screen is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC06-07 My Application Status - Cancelled Appointment Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-07 My Application Status - Cancelled Appointment Exception")
            assert(False)
        finally:
            print("Book SOPC06-07 My Application Status - Cancelled Appointment finish")

    def testbooksopc0608(self):
        try:
            print("Book SOPC06-08 My Application Status - Closed Application start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            my_application_status_button = user_data['my_application_status_button'][app_lang]
            my_application_status_title = user_data['my_application_status_title'][app_lang]
            patient_HKID_Letter = user_data['HKID_Letter_06_08']
            patient_HKID_Body_Digits = user_data['HKID_Body_Digits_06_08']
            patient_HKID_Last_Digit = user_data['HKID_Last_Digit_06_08']
            patient_reference_number_06_08 = user_data['patient_reference_number_06_08']
            next_button = user_data['next_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+book_sopc_button+"']]").click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+enquiry_button+"']]").click()
            time.sleep(2)

            ## Click My Application Status
            print("Click My Application Status button")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+my_application_status_button+"']]").click()
            time.sleep(4)

            ## Check if title text contains My Application Status
            assert(self.driver.find_element_by_link_text(my_application_status_title).is_displayed), "Cannot find My Application Status in title"
            time.sleep(2)

            ## Input Reference number of Closed Application
            self.driver.find_element_by_xpath("//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[./*[@class='android.widget.Spinner']]]").send_keys(patient_reference_number_06_08)
            time.sleep(2)

            ## Input HKID/HK Birth Certificate number
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]").send_keys(patient_HKID_Letter)
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]").send_keys(patient_HKID_Body_Digits)
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+patient_HKID_Last_Digit+"']]").click()
            time.sleep(2)

            ## Click Next Button with reference number and HKID/HKBC of Closed Application 
            print("Click Next Button with reference number and HKID/HKBC of Closed Application")
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]")))
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='"+next_button+"']]").click()
            time.sleep(4)

            ## Display screen of Closed Application
            print("Book SOPC06-08 Scenario 01 Display screen of Closed Application")
            self.driver.save_screenshot(test_dir+"06_08_Closed_Application_screen.png")
            print("Screenshot 06_08_Closed_Application_screen is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC06-08 My Application Status - Closed Application Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-08 My Application Status - Closed Application Exception")
            assert(False)
        finally:
            print("Book SOPC06-08 My Application Status - Closed Application finish")

    def testbooksopc0609(self):
        try:
            print("Book SOPC06-09 Enquiry - Waiting Time start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            waiting_time_title = user_data['waiting_time_title'][app_lang]
            pop_up_CONFIRM_button = user_data['pop_up_CONFIRM_button'][app_lang]
            specialty_selected = user_data['specialty_06_09'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,book_sopc_button)))
            self.driver.find_element_by_link_text(book_sopc_button).click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,enquiry_button)))
            self.driver.find_element_by_link_text(enquiry_button).click()
            time.sleep(2)

            ## Click Waiting Time
            print("Book SOPC06-09 Scenario 01 Access to Waiting Time page")
            print("Click Waiting Time button")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,waiting_time_title)))
            self.driver.find_element_by_link_text(waiting_time_title).click()
            time.sleep(4)

            ## Check if title text contains Waiting Time
            assert(self.driver.find_element_by_link_text(waiting_time_title).is_displayed), "Cannot find Waiting Time in title"
            time.sleep(2)
            print("Book SOPC06-09 Scenario 02 Outlook of Waiting Time page")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_09_waiting_time_page.png")
            print("Screenshot 06_09_waiting_time_page is taken")
            time.sleep(2)

            ## Click Information Button
            print("Book SOPC06-09 Scenario 03 Display Pop-up Window of SOPC waiting time")
            print("Click Information Button")
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@class='android.widget.ImageView' and ./parent::*[@class='android.view.ViewGroup' and (./preceding-sibling::* | ./following-sibling::*)[@class='android.view.ViewGroup']]]").click()
            time.sleep(2)

            ## Pop-up Window of SOPC waiting time is displayed
            print("Pop-up Window of SOPC waiting time is displayed")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_09_SOPC_waiting_time_information_window.png")
            print("Screenshot 06_09_SOPC_waiting_time_information_window is taken")
            time.sleep(2)

            ## Click CONFIRM Button to close Pop-up Window of SOPC waiting time 
            print("Click CONFIRM Button to close Pop-up Window of SOPC waiting time")
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,pop_up_CONFIRM_button)))
            self.driver.find_element_by_link_text(pop_up_CONFIRM_button).click()
            time.sleep(4)
  
            ## Access different pages of specialities
            print("Book SOPC06-09 Scenario 04 Access different pages of specialities")
            time.sleep(2)
            print("Select Specialty "+specialty_selected+" to see its waiting time")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT,specialty_selected)))
            self.driver.find_element_by_partial_link_text(specialty_selected).click()
            
            ## Check if title text matches selected specialty
            assert(self.driver.find_element_by_partial_link_text(specialty_selected).is_displayed), "Title specialty does not match"
            time.sleep(2)

            ## Display screen of waiting time page of speciality
            print("Book SOPC06-09 Scenario 05 Display screen of waiting time page of speciality")
            time.sleep(4)
            print("Waiting time page of speciality "+specialty_selected+" is displayed")
            self.driver.save_screenshot(test_dir+"06_09_SOPC_waiting_time_specialty_screen_time.png")
            print("Screenshot 06_09_Cancelled_My_Application_screen_time is taken")
            time.sleep(2)

            ## Swipe down to show Notes
            self.driver.execute_script("seetest:client.swipe(\"Down\", 200, 800)")
            time.sleep(2)

            ## Display Notes in screen of waiting time page of speciality
            print("Notes in Waiting time page of speciality "+specialty_selected+" is displayed")
            self.driver.save_screenshot(test_dir+"06_09_SOPC_waiting_time_specialty_screen_notes.png")
            print("Screenshot 06_09_Cancelled_My_Application_screen_notes is taken")
            time.sleep(2)

        except TimeoutException:
            print("Book SOPC06-09 Enquiry - Waiting Time Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-09 Enquiry - Waiting Time Exception")
            assert(False)
        finally:
            print("Book SOPC06-09 Enquiry - Waiting Time finish")

    def testbooksopc0610(self):
        try:
            print("Book SOPC06-10 Enquiry - Information About SOPC start")
            user_data = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
            app_lang = user_data['app_lang']
            book_sopc_button = user_data['book_sopc_button'][app_lang]
            enquiry_button = user_data['enquiry_button'][app_lang]
            information_about_SOPC_title = user_data['information_about_SOPC_title'][app_lang]
            specialty_selected = user_data['specialty_06_10'][app_lang]
            tab_hk_island = user_data['tab_hk_island'][app_lang]
            tab_kowloon = user_data['tab_kowloon'][app_lang]
            tab_new_territories = user_data['tab_new_territories'][app_lang]
            specialty_hospital_selected = user_data['specialty_hospital_06_10'][app_lang]
            pop_up_CONFIRM_button = user_data['pop_up_CONFIRM_button'][app_lang]

            ## Log in
            TestBook.testbook_login(self)
            time.sleep(3)

            ## Book SOPC
            print("Book SOPC")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,book_sopc_button)))
            self.driver.find_element_by_link_text(book_sopc_button).click()
            time.sleep(2)

            ## Click Enquiry Button
            print("Click Enquiry Button")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,enquiry_button)))
            self.driver.find_element_by_link_text(enquiry_button).click()
            time.sleep(2)

            ## Click Information about SOPC
            print("Book SOPC06-10 Scenario 01 Access to Information About SOPC page")
            print("Click Information About SOPC button")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,information_about_SOPC_title)))
            self.driver.find_element_by_link_text(information_about_SOPC_title).click()
            time.sleep(4)

            ## Check if title text contains Information About SOPC
            assert(self.driver.find_element_by_link_text(information_about_SOPC_title).is_displayed), "Cannot find Waiting Time in title"
            time.sleep(2)
            print("Book SOPC06-10 Scenario 02 Outlook of Information About SOPC page")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_10_information_about_sopc_page.png")
            print("Screenshot 06_10_information_about_sopc_page is taken")
            time.sleep(2)

            ## Access different information pages of the specialities
            print("Book SOPC06-10 Scenario 03 Access different information pages of the specialities")
            time.sleep(2)
            print("Select Specialty "+specialty_selected+" to see its information")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT,specialty_selected)))
            self.driver.find_element_by_partial_link_text(specialty_selected).click()
            
            ## Check if title text matches selected specialty
            assert(self.driver.find_element_by_partial_link_text(specialty_selected).is_displayed), "Title specialty does not match"
            time.sleep(2)

            ## Outlook of Information page of the speciality
            print("Book SOPC06-10 Scenario 04 Outlook of Information page of the speciality")
            time.sleep(2)
            print("Information page of speciality "+specialty_selected+" is displayed")
            self.driver.save_screenshot(test_dir+"06_10_Information_page_specialty.png")
            print("Screenshot 06_10_Information_page_specialty is taken")
            time.sleep(2)

            ## Function of switching between Tabs of Area
            print("Book SOPC06-10 Scenario 05 Function of switching between Tabs of Area")
            time.sleep(2)
            print("Click Tab of Kowloon")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='"+tab_kowloon+"']]]").click()
            time.sleep(3)
            print("Display Hospitals with related Specialty in Kowloon")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_10_specialty_tab_kowloon.png")
            print("Screenshot 06_10_specialty_tab_kowloon is taken")
            time.sleep(2)

            print("Click Tab of New Territories")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='"+tab_new_territories+"']]]").click()
            time.sleep(3)
            print("Display Hospitals with related Specialty in New Territories")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_10_specialty_tab_new_territories.png")
            print("Screenshot 06_10_specialty_tab_new_territories is taken")
            time.sleep(2)

            print("Click Tab of Hong Kong Island")
            self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@class='android.view.ViewGroup' and ./*[@text='"+tab_hk_island+"']]]").click()
            time.sleep(3)
            print("Display Hospitals with related Specialty in Hong Kong Island")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_10_specialty_tab_hk_island.png")
            print("Screenshot 06_10_specialty_tab_hk_island is taken")
            time.sleep(2)

            ## Opening Pop-Window of any hospital
            print("Book SOPC06-10 Scenario 06 Opening Pop-Window of hospital")
            time.sleep(2)
            print("Click Hospital: "+specialty_hospital_selected)
            self.driver.find_element_by_partial_link_text(specialty_hospital_selected).click()
            time.sleep(3)

            ## Pop-up Window of selected hospital is displayed
            print("Pop-up Window of selected hospital is displayed")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_10_pop_up_window_hospital.png")
            print("Screenshot 06_10_pop_up_window_hospital is taken")
            time.sleep(2)

            ## Functions in Pop-Window of hospital
            print("Book SOPC06-10 Scenario 07 Functions in Pop-Window of hospital")
            time.sleep(2)
            print("Click Address box")

            ## Device Map application is opened and pin-pointed the location of selected hospital
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[1]").click()
            time.sleep(6)
            print("Device Map application is opened and pin-pointed the location of selected hospital "+specialty_hospital_selected)
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_10_selected_hospital_address.png")
            print("Screenshot 06_10_selected_hospital_address is taken")
            time.sleep(2)

            ## Go back to HA App
            print("Go back to HA App")
            time.sleep(2)
            self.driver.press_keycode(4) # back
            time.sleep(2)

            ## Device Dialling application is opened to make voice call
            self.driver.find_element_by_xpath("(//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup' and ./parent::*[@class='android.view.ViewGroup']]]]/*[@class='android.view.ViewGroup' and ./*[@class='android.widget.ImageView']])[2]").click()
            time.sleep(6)
            print("Device Dialling application is opened to make voice call ")
            time.sleep(2)
            self.driver.save_screenshot(test_dir+"06_10_selected_hospital_voice_call_pop_up.png")
            print("Screenshot 06_10_selected_hospital_voice_call_pop_up is taken")
            time.sleep(2)
            print("Click CONFIRM to make voice call to "+specialty_hospital_selected)
            self.driver.find_element_by_link_text(pop_up_CONFIRM_button).click()
            time.sleep(3)
            self.driver.save_screenshot(test_dir+"06_10_selected_hospital_voice_call_interface.png")
            print("Screenshot 06_10_selected_hospital_voice_call_interface is taken")
            time.sleep(2)
 
        except TimeoutException:
            print("Book SOPC06-10 Enquiry - Information About SOPC Timeout Exception")
            assert(False)
        except Exception:
            print("Book SOPC06-10 Enquiry - Information About SOPC Exception")
            assert(False)
        finally:
            print("Book SOPC06-10 Enquiry - Information About SOPC finish")


    def tearDown(self):
        self.driver.quit()