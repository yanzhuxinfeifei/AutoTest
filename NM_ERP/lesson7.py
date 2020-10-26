# 导入selenium库，初始化driver
import selenium
import time
from selenium import webdriver
driver = webdriver.Chrome()

# 1.打开一个网址
driver.get("http://erp.lemfix.com")
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
driver.maximize_window()
time.sleep(1)
driver.find_element_by_xpath("//span[text()='零售出库']").click()
time.sleep(1)
# driver.find_element_by_id("searchNumber").send_keys("314")
outBaseId=driver.find_element_by_xpath("//span[text()='零售出库']/..").get_attribute("data-tab-id")
time.sleep(1)
billNum = outBaseId+'-frame'
print(outBaseId)
print(billNum)
# 切换iframe  driver.switch_to.frame(billNum)
driver.switch_to.frame(billNum)
driver.find_element_by_id("searchNumber").send_keys("314")
time.sleep(1)
driver.find_element_by_id("searchBtn").click()