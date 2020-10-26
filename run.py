'''
Author:田菲
Date:2020/10/26
Model:柠檬班ERP

'''
from NM_ERP import erp_search
from testData import testData
import selenium
from selenium import webdriver
driver=webdriver.Chrome()
url=testData.url["url"]
username=testData.login_data["username"]
password=testData.login_data["password"]
search_key=testData.search_key["search_key"]
erp_search.all_search(driver=driver,url=url,username=username,password=password,search_key=search_key)