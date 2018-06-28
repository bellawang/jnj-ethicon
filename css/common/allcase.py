# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest
import time
import re
import csv
from configparser import ConfigParser
import toHexadecimal
from selenium.webdriver.remote.webelement import WebElement
import util


def homepage(self,args):
    driver = self.driver
    self.base_url =  args.get('url')
    driver.get(self.base_url)
    element=driver.find_element_by_xpath(args.get('element'))
    print(element.get_attribute("innerText"))
    fontSize =element.value_of_css_property('font-size')
    colorRgb=element.value_of_css_property('color')
    numInColor=re.findall(r"\d+",colorRgb)
    color=str(toHexadecimal.toHex(numInColor))
    driver.save_screenshot('../pictures/1.png')
    # print(fontSize)
    # print(color)
    self.assertEqual(fontSize, args.get(
        'fontSize'), 'font-size is ' + fontSize + ', should be ' + args.get('fontSize'))
    self.assertEqual(color, args.get(
        'color'), 'color is ' + color + ', should be ' + args.get('color'))   