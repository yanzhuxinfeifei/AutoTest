'''
web自动化基本操作
selenium的基本使用
'''
# selenium的导入
# import selenium
# from selenium import webdriver
# import time
# # 选择浏览器chrom,初始化driver
# driver = webdriver.Chrome()
# # 1.打开一个网址
# driver.get("http://www.baidu.com")
# driver.get("http://120.78.128.25:8765")
# # 2.浏览器窗口最大化
# driver.maximize_window()
# # 3.打开一个新页面
# driver.get("http://erp.lemfix.com")
# # 4.向前 退后 刷新
# driver.back() # 回退到前程贷的网页
# time.sleep(2) # 等待时间，默认时间单位是秒
# driver.forward() #前进到下一个网页
# time.sleep(2)
# driver.refresh() # 刷新页面
# # 5.退出
# driver.quit() #关闭驱动 session也同时关闭
# driver.close() #关闭当前的窗口 不会退出会话


'''
案例
'''
# selenium的导入
import selenium
from selenium import webdriver
import time
# 选择浏览器chrom,初始化driver
driver = webdriver.Chrome()
# 1.打开一个网址
driver.get("http://erp.lemfix.com")
# 2.通过元素的id来获取元素(通过find_element_by_id("username"))填入用户名和密码，通过send_keys("账号")
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()  # 进行点击操作
# 5.退出
# driver.quit() #关闭驱动 session也同时关闭
