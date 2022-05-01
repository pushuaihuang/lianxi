# author:黄浦帅
# time:2022/4/28 12:25 下午
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#元素操作
def test_element():
    """
    元素的定位，点击，输入，qingkong操作
    :return:
    """
    driver = webdriver.Chrome()
    driver.get("https://www.sogou.com/")
    driver.find_element(By.ID,"query").send_keys("苏醒")
    time.sleep(2)
    driver.find_element(By.ID,"stb").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#upquery").clear()
    time.sleep(3)
    driver.find_element(By.ID,"upquery").send_keys("pushuai")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="searchBtn"]').click()
    driver.quit()
#元素属性
def test_attribute():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    time.sleep(2)
    web_element = driver.find_element(By.ID,"locate_id")
    #获取元素的文本信息
    print(web_element.text)
    print(web_element.get_attribute("id"))
    time.sleep(2)
    driver.quit()



