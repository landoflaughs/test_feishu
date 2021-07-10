import pytest
from appium.webdriver.common.mobileby import MobileBy

from test_feishu_appium.page.app import App


class TestAddGroup:
    def setup(self):
        self.app = App().start()
        self.main = self.app.goto_main()

    def teardown(self):
        # self.app.stop()
        pass

    # @pytest.mark.parametrize('name', '[group5]')
    def test_add_group(self,name):
        self.main.goto_notification_click_add().create().rename("group5").back_to_main()
