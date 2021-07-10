from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_feishu_appium.page.base_page import BasePage
from test_feishu_appium.page.group_page import GroupPage


class MainPage(BasePage):
    load_complete = (MobileBy.XPATH, "//*[contains(@text,'已完成')]")

    notification_ele = (MobileBy.ID,
                        "com.ss.android.lark:id/navigation_tab_left_title")
    add_group_ele = (MobileBy.ID,
                     "com.ss.android.lark:id/btn_create_group")

    def goto_notification_click_add(self):
        # 显示等待消息页面加载出来
        WebDriverWait(self.driver, 50, 0.5).until(
            expected_conditions.visibility_of_element_located(self.load_complete))
        # 找到消息页面，点击
        Element = WebDriverWait(self.driver, 30, 0.5).until(
            expected_conditions.visibility_of_element_located(self.notification_ele))
        Element.click()
        # 点击右上角加号
        add_btn = self.driver.find_element(MobileBy.ID, "com.ss.android.lark:id/function_btn_2")
        add_btn.click()
        # 点击添加群组
        self.find(*self.add_group_ele).click()
        return GroupPage(self.driver)
