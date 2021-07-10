from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_feishu_appium.page.base_page import BasePage


class GroupPage(BasePage):
    load_complete_flag = (MobileBy.XPATH, "//*[@text='我管理的群组']")

    def create(self):
        WebDriverWait(self.driver, 30, 0.5).until(
            expected_conditions.visibility_of_element_located(self.load_complete_flag))
        self.find_and_click(MobileBy.XPATH, '//*[@text="创建"]')
        self.find(MobileBy.XPATH, '//*[contains(@text,"成员")]')
        return self

    def rename(self, name):
        # 点击右上角三点
        self.find_and_click(MobileBy.ID,
                            "com.ss.android.lark:id/iv_icon")
        # 点击群进入设置界面
        self.find_and_click(MobileBy.ID,
                            "com.ss.android.lark:id/group_name_desc_layout")
        # 判断已经创建了包含默认名称的群组
        self.find(MobileBy.XPATH, '//*[contains(@text,"HS")]')
        # 点击群名称进入修改界面
        self.find_and_click(MobileBy.XPATH, '//*[contains(@text,"群名称")]')
        # 重命名群名称
        self.find(MobileBy.ID,
                  "com.ss.android.lark:id/info_edit_text").send_keys(name)

        self.find(MobileBy.XPATH, f'//*[contains(@text,"{name}")]')  # 验证已经输入成功
        # 点击保存
        self.find_and_click(MobileBy.XPATH, '//*[contains(@text,"保存")]')
        return self

    def back_to_main(self):
        self.finds(MobileBy.XPATH, '//*[@class="android.widget.TextView"]')[0].click()
        sleep(3)    # 等待3秒，避免因为延迟而查找到了上一个页面的元素
        tmpele = self.finds(MobileBy.XPATH, '//*[@class="android.widget.TextView"]')[0]
        tmpele.click()
        self.find_and_click(MobileBy.ID,
                            "com.ss.android.lark:id/back")
