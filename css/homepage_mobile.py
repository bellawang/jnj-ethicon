# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import requests
import unittest
import time
import re
import HTMLTestRunner
import csv
from configparser import ConfigParser

cf = ConfigParser()
cf.read("../config/css.conf")
username = cf.get('baseurl', 'username')
password = cf.get('baseurl', 'password')


class Font(unittest.TestCase):

    def setUp(self,args):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.base_url = 'http://' + username + ':' + password + '@' + args.get('url')
        self.verificationErrors = []
        self.accept_next_alert = True

# Test for font size and font color
    def font(self, args):
        driver = self.driver
        driver.get(self.base_url)
        driver.set_window_position(0, 0)
        driver.set_window_size(414, 900)        
        element=driver.find_element_by_xpath(args.get('element'))
        fontSize =element.value_of_css_property('font-size')
        color=element.value_of_css_property('color')
        # print(fontSize)
        # print(color)
        self.assertEqual(fontSize, args.get(
            'fontSize'), 'font-size is ' + fontSize + ',not ' + args.get('fontSize'))
        self.assertEqual(color, args.get(
            'color'), 'color is ' + color + ',not ' + args.get('color'))        

    def fontsize_check(self, args):
        driver = self.driver
        driver.get(self.base_url)
        self.font(args)

    @staticmethod
    def getTestFunc_fontSize(arg):
        def func(self):
            self.fontsize_check(arg)
        return func

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


def __generateTestCases():
    with open("../data/homepage.csv") as csvfile:
        arglists = csv.DictReader(csvfile)
        for args in arglists:
            setattr(Font, 'test_Font_%s' %
                    (args.get('section')), Font.getTestFunc_fontSize(args))

def all_cases():
    testcase = unittest.TestSuite()
    with open("../data/fontsize.csv") as csvfile:
        arglists = csv.DictReader(csvfile)
        for args in arglists:
            testcase.addTest(Font('test_Font_%s' %
                                      (args.get('section'))))

        return testcase


if __name__ == '__main__':
    __generateTestCases()
    # 确定生成报告的路径
    # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # filePath = "D:\\ONE\\API AUTO TEST\\report\\" + now + "_CSSresult.html"
    # fp = open(filePath, 'wb')
    # # 生成报告的Title,描述
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp, title='alloffice Test Report', description='This is alloffice Report', verbosity=2)
    # runner.run(all_cases())
    # fp.close()
    unittest.main(verbosity=2)
        # driver.execute_script('arguments[0].scrollIntoView();',element)
