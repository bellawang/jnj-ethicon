# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
# import requests
import unittest
import time
import re
import HTMLTestRunner
import csv
from configparser import ConfigParser
from common import toHexadecimal
from common import allcase

cf = ConfigParser()
cf.read("../config/css.conf")
# username = cf.get('baseurl', 'username')
# password = cf.get('baseurl', 'password')
homepage_Desktop=cf.get('csvFile','homepage_desktop')



class Font(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.verificationErrors = []
        self.accept_next_alert = True

# Test for font size and font color
    def font(self, args):
        driver = self.driver
        self.base_url =  args.get('url')
        driver.get(self.base_url)
        element=driver.find_element_by_xpath(args.get('element'))
        fontSize =element.value_of_css_property('font-size')
        colorRgb=element.value_of_css_property('color')
        numInColor=re.findall(r"\d+",colorRgb)
        color=str(toHexadecimal.toHex(numInColor))
        # print(fontSize)
        # print(color)
        self.assertEqual(fontSize, args.get(
            'fontSize'), 'font-size is ' + fontSize + ', should be ' + args.get('fontSize'))
        self.assertEqual(color, args.get(
            'color'), 'color is ' + color + ', should be ' + args.get('color'))        

    def fontsize_check(self, args):
        driver = self.driver
        self.base_url =  args.get('url')
        print(self.base_url)
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
    with open(homepage_Desktop) as csvfile:
        arglists = csv.DictReader(csvfile)
        for args in arglists:
            testcase.addTest(Font('test_Font_%s' %
                                      (args.get('section'))))

        return testcase


if __name__ == '__main__':
    __generateTestCases()
    # 确定生成报告的路径
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filePath = "..\\report\\" + now + "_homepage.html"
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title='Homepage Test Report', description='This is homepage Report', verbosity=2)
    runner.run(all_cases())
    fp.close()
    # unittest.main(verbosity=2)
