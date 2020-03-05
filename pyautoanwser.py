import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#先安装pywin32，才能导入下面两个包
import win32api
import win32con
#导入处理alert所需要的包
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import traceback
import random
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application"
os.environ["webdriver.ie.driver"] = chromedriver

driver = webdriver.Chrome()
driver.get('http://passport2.chaoxing.com/login?fid=30528&refer=http://cmc.fanya.chaoxing.com')  # 打开网站
driver.maximize_window()
username = '19983434671'
password ='lk94dbfenshou'
numcode = input('input:')
driver.find_element_by_id('unameId').click()  # 点击用户名输入框
driver.find_element_by_id('unameId').clear()  # 清空输入框
driver.find_element_by_id('unameId').send_keys(username)  # 自动敲入用户名

driver.find_element_by_id('passwordId').click()  # 点击密码输入框
driver.find_element_by_id('passwordId').clear()  # 清空输入框
driver.find_element_by_id('passwordId').send_keys(password)  # 自动敲入密码
driver.find_element_by_id('numcode').click()  # 点击密码输入框
driver.find_element_by_id('numcode').clear()  # 清空输入框
driver.find_element_by_id('numcode').send_keys(numcode)
driver.find_element_by_class_name('zl_btn_right').click()
driver.get('https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=248013906&courseId=208423087&clazzid=16928600&enc=6e5bfd9627ca7d78ed9b85f3f430a533')
time.sleep(2)

driver.find_element_by_id('dct2').click()

time.sleep(2)

driver.switch_to.frame('iframe')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
driver.switch_to.frame('frame_content')

uls  =  driver.find_elements_by_tag_name('ul')

for i in range(len(uls)):
    li_s = uls[i].find_elements_by_tag_name('li')
    _rand= random.random()*len(li_s)
    li_s[int(_rand)].find_element_by_tag_name('input').click()
    time.sleep(1)

driver.find_element_by_class_name('Btn_blue_1').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="confirmSubWin"]/div/div/a[1]').click()
