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
from common import allcase,toHexadecimal

cf = ConfigParser()
cf.read("../config/css.conf")

homepage_Tab=cf.get('csvFile','homepage_tab')


class Font(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(800,1024)
        self.driver.implicitly_wait(3)
        self.verificationErrors = []
        self.accept_next_alert = True

# Test for font size and font color
    def font(self, args):   
        allcase.homepage(self, args)


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
    with open(homepage_Tab) as csvfile:
        arglists = csv.DictReader(csvfile)
        for args in arglists:
            setattr(Font, 'test_Font_%s' %
                    (args.get('section')), Font.getTestFunc_fontSize(args))

def all_cases():
    testcase = unittest.TestSuite()
    with open(homepage_Tab) as csvfile:
        arglists = csv.DictReader(csvfile)
        for args in arglists:
            testcase.addTest(Font('test_Font_%s' %
                                      (args.get('section'))))

        return testcase


if __name__ == '__main__':
    __generateTestCases()
    # 确定生成报告的路径
    # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # filePath = "..\\report\\" + now + "_homepageMob.html"
    # fp = open(filePath, 'wb')
    # # 生成报告的Title,描述
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp, title='Homepage Test Report', description='This is homepage Report', verbosity=2)
    # runner.run(all_cases())
    # fp.close()
    unittest.main(verbosity=2)
