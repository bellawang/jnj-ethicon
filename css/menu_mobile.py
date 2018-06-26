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
menuPath = cf.get('menuIcon', 'path')


class Font(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.DictReaderdriver.implicitly_wait(3)
        self.verificationErrors = []
        self.accept_next_alert = True

# Test for font size and font color
    def menu(self, args):
        driver = self.driver
        self.base_url = 'http://' + username + ':' + password + '@' + args.get('url')
        driver.get(self.base_url)
        driver.set_window_position(0, 0)
        driver.set_window_size(414, 900)
        menuIcon = driver.find_element_by_xpath(args.get('element'))
        menuIcon.click()
        element = driver.find_element_by_xpath(menuPath)

        fontSize = element.value_of_css_property('font-size')
        color = element.value_of_css_property('color')
        # print(fontSize)
        # print(color)
        self.assertEqual(fontSize, args.get(
            'fontSize'), 'font-size is ' + fontSize + ',not ' + args.get('fontSize'))
        self.assertEqual(color, args.get(
            'color'), 'color is ' + color + ',not ' + args.get('color'))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def check_font(self,args):
        driver = self.driver
        self.base_url = 'http://' + username + ':' + password + '@' + args.get('url')
        driver.get(self.base_url)
        self.menu(args)
    
    @staticmethod
    def get_func(arg):
        def func(self):
            print("2")
            self.check_font(arg)
        return func


if __name__ == '__main__':
    with open("../data/menu_mobile.csv") as csvfile:
        argslist = csv.DictReader(csvfile)
        for args in argslist:
            setattr(Font, 'test_Font_%s' %(args.get('section')), Font.get_func(args))

#     # 确定生成报告的路径
#     # now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
#     # filePath = "D:\\ONE\\API AUTO TEST\\report\\" + now + "_CSSresult.html"
#     # fp = open(filePath, 'wb')
#     # # 生成报告的Title,描述
#     # runner = HTMLTestRunner.HTMLTestRunner(
#     #     stream=fp, title='alloffice Test Report', description='This is alloffice Report', verbosity=2)
#     # runner.run(all_cases())
#     # fp.close()
    unittest.main(verbosity=2)
#         # driver.execute_script('arguments[0].scrollIntoView();',element)
