# author:黄浦帅
# time:2022/4/27 9:11 下午
#浏览器控制操作
import time
from selenium import webdriver
def test_browser():
    driver = webdriver.Chrome()
    #通过url打开浏览器
    driver.get("https://www.baidu.com")
    time.sleep(5)
    #最大化浏览器
    driver.maximize_window()
    driver.get("https://ceshiren.com")
    time.sleep(2)
    #退回上一步
    driver.back()
    # 刷新浏览器
    driver.refresh()
    #退出浏览器
    time.sleep(2)
    driver.quit()



