#!/usr/local/bin/python3 -B
# scraper.py

from time import sleep
from selenium import webdriver


options = webdriver.FirefoxOptions()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get('')
