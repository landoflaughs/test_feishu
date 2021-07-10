from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTmp():
    def setup_method(self,method):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.vars = {}

    def teardown_method(self,method):
        pass
        # self.driver.quit()

    def test_tmp(self):
        self.driver.get("https://test-cck6ervfruif.feishu.cn/messenger")

        self.driver.find_element(By.XPATH, "//*[@data-feed-id='6980971371111153692']").click()

        self.driver.find_element(By.XPATH, "//*[@class='lark-editor lark-empty']").send_keys("hello")

        # self.driver.close()
