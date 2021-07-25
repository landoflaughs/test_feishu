import pytest
import allure
from appium.webdriver.common.mobileby import MobileBy

from test_feishu_appium.page.app import App


@allure.feature("appium test")
class TestAddGroup:
    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardown(self):
        # self.app.stop()
        pass

    @allure.story("add group")
    # @pytest.mark.parametrize('name', "AB")
    def test_add_group(self, add_group):
        self.main.goto_notification_click_add().create().rename(add_group).back_to_main()
