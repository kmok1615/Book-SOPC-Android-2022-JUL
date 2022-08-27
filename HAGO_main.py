# coding=UTF-8
'''
Created on 2022.4.19
Author: Ken Mok
'''
#coding:utf-8

import unittest
import os
import yaml

## Single test case
# Book SOPC
from hago_testcase.book_sopc01 import TestBookSOPC01
from hago_testcase.book_sopc02 import TestBookSOPC02
from hago_testcase.book_sopc03 import TestBookSOPC03
from hago_testcase.book_sopc04 import TestBookSOPC04
from hago_testcase.book_sopc05 import TestBookSOPC05
from hago_testcase.book_sopc06 import TestBookSOPC06
from hago_testcase.book_sopc07 import TestBookSOPC07
#from hago_testcase.book_sopc08 import TestBookSOPC08
# Book AH


from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner

test_dir = './Automation Test/hago_testcase'
report_name = './Automation Test/report/test_html_report.html'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='book_sopc0*.py') #Single File running

CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\Automation Test\\hago_testcase\\"

 # Perform test
if __name__=="__main__":
    ##fb = open(report_name,'wb')

    ### Load Test Data
    conf = yaml.load(open(CONF_PATH + 'config.yml'), Loader=yaml.FullLoader)
    userdata = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.SafeLoader)
    testreport_switch = userdata['testreport_switch']

    ### Test case
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(TestEmptyState))
    #suite.addTest(TestBookSOPC01('testbooksopc0101'))
    #suite.addTest(TestBookSOPC01('testbooksopc010402'))
    #suite.addTest(TestBookSOPC02('testbooksopc0201'))
    #suite.addTest(TestBookSOPC02('testbooksopc0204'))
    #suite.addTest(TestBookSOPC03('testbooksopc0304'))
    #suite.addTest(TestBookSOPC04('testbooksopc0404'))
    #suite.addTest(TestBookSOPC05('testbooksopc0504'))
    #suite.addTest(TestBookSOPC06('testbooksopc0602'))
    #suite.addTest(TestBookSOPC06('testbooksopc0604'))
    suite.addTest(TestBookSOPC07('testbooksopc0700'))

    ### Decide if test report is required
    if testreport_switch == 'Yes':
        ##### Running Single test case with HTML Test Report
        runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                                open_in_browser=True, description="HTMLTestReport")
    elif testreport_switch == 'No':
        ##### Running Single test case without HTML Test Report
        runner = unittest.TextTestRunner()
    else:
        print("INVALID SETTING OF TESTREPORT SWITCH IN test_data.yml")
        runner = ""

    ##### Running Multiple test cases in files
    #runner.run(discover)

    ##### Run Test
    runner.run(suite)


