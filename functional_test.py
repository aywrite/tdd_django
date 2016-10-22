from selenium import webdriver
from  selenium.webdriver.firefox.firefox_binary import FirefoxBinary

firefox_path='/home/andrew/Downloads/firefox/firefox'
chrome_driver_path='/home/andrew/Downloads/chromedriver'

browser = webdriver.Chrome(chrome_driver_path)

#browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
#    firefox_path=firefox_path
#))
browser.get('http://localhost:8000')

assert 'Django' in browser.title
