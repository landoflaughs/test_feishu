from time import sleep

from selenium.webdriver.common.by import By


class RemoveGroupPage:
    def __init__(self, driver):
        self.driver = driver

    def remove_group(self):
        self.driver.find_element(By.XPATH, "//*[@class = 'chatWindow_avatar']").click()
        self.driver.find_element(By.XPATH, "//*[@class = 'uni-btn uni-btn-default uni-btn-theme-warning uni-btn-size-large ']").click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id= "__larkc-modall-container__"]/div[2]/div/div[2]/div/div/footer/div/button[2]').click()
        try:
            self.is_text_present("group1")

        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def is_text_present(self, text):
        return str(text) in self.driver.page_source