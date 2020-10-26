'''
Author:田菲
Date:2020/10/26
Model:柠檬班ERP

'''
# 导入selenium库，初始化driver
import selenium
import time
from selenium import webdriver
# driver = webdriver.Chrome()

# 1.打开一个网址
def open_url(driver,url):
    driver.get(url)
# driver.get("http://erp.lemfix.com")
# 2.输入用户名和密码进行登录
def login_data(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
    driver.maximize_window()
    time.sleep(1)
# 4.serch_all
def all_search(driver,url,username,password,search_key):
    open_url(driver,url)
    login_data(driver,username,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(1)
    outBaseId = driver.find_element_by_xpath("//span[text()='零售出库']/..").get_attribute("data-tab-id")
    time.sleep(1)
    billNum = outBaseId + '-frame'
    driver.switch_to.frame(billNum)
    driver.find_element_by_id("searchNumber").send_keys(search_key)
    time.sleep(1)
    driver.find_element_by_id("searchBtn").click()
