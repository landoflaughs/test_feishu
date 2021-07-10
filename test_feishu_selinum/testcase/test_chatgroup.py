from test_feishu_selinum.page.main_page import MainPage

# 测试前需要先cmd打开浏览器复用
# chrome --remote-debugging-port=9222
# 然后在网页端登录一次飞书，以便跳过登录环节

class TestChatGroup:

    def test_add_group(self):
        main = MainPage()
        main.goto_create_group().create_group("group1").remove_group()

