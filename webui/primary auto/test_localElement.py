# author:黄浦帅
# time:2022/4/27 10:04 下午
#常用的元素定位
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_location():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    #通过id定位
    driver.find_element(By.ID,"locate_id")
    #通过name
    driver.find_element(By.NAME,"locate")
    #通过css
    driver.find_element(By.CSS_SELECTOR,"#locate_id > a > span")
    #通过xpath
    driver.find_element(By.XPATH,'//*[@id="locate_id"]/a/span')
    #通过连接文本方式获取（1）元素一定是标签（2），输入的元素为标签内的文本
    driver.find_element(By.LINK_TEXT,"元素定位").click()
    driver.quit()
