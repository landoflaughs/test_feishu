from selenium import webdriver
from selenium.webdriver.common.by import By

from test_feishu_selinum.page.create_group_page import CreateGroupPage


class MainPage:
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        self.driver.get("https://test-cck6ervfruif.feishu.cn/messenger")


    def goto_create_group(self):
        self.driver.find_element(By.XPATH,
                                 "//*[@class = 'lark-drag-disable quick-jump-enter__icon']").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@class = 'quick-jump-menu__item']").click()
        return CreateGroupPage(self.driver)