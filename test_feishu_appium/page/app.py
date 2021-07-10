import yaml
from appium import webdriver

from test_feishu_appium.page.base_page import BasePage
from test_feishu_appium.page.main_page import MainPage

with open(r'D:\WORK\jenkins\connect\workspace\windows_appium\feishu_windows_test\test_feishu_appium\datas\feishu_caps'
          r'.yml') as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']


class App(BasePage):
    def start(self):
        if self.driver is None:
            # 启动飞书
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(10)  # 设置5秒隐式等待
        else:
            self.driver.launch_app()  # Start on the device the application specified in the desired capabilities.
        return self

    def restart(self):
        # 重启
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)
