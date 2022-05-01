# author:黄浦帅
# time:2022/4/30 1:19 下午
from selenium import webdriver
from selenium.webdriver.common.by import By
class  TestCeshiren():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_search(self):
        self.driver.get("https://ceshiren.com/")
        #窗口最大化
        self.driver.maximize_window()
        #寻找并点击搜索按钮
        self.driver.find_element(By.CSS_SELECTOR,"#search-button").click()
        #输入要搜索的内容
        self.driver.find_element(By.ID,"search-term").send_keys("appium")
        #点击搜索
        self.driver.find_element(By.CSS_SELECTOR,".widget-link.show-advanced-search").click()
        #点击确定
        self.driver.find_element(By.CSS_SELECTOR,".fa.d-icon.d-icon-search.svg-icon.svg-string").click()
        #获取搜索结果
        web_element = self.driver.find_element(By.CSS_SELECTOR,".topic-title")
        assert "appium" in web_element.text.lower()