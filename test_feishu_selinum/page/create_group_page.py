from selenium.webdriver.common.by import By

from test_feishu_selinum.page.remove_group_page import RemoveGroupPage


class CreateGroupPage:
    def __init__(self, driver):
        self.driver = driver

    def create_group(self,name):
        self.driver.find_element(By.XPATH, "//*[@class = 'chat-name-input']").send_keys(name)
        self.driver.find_element(By.XPATH,
                                 "//*[@class = 'larkc-btn larkc-btn-normal larkc-btn-primary larkc-btn-large']").click()
        return RemoveGroupPage(self.driver)
