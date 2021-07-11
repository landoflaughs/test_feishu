import pytest
import allure

from test_feishu_interface.conftest import load_yaml
from test_feishu_interface.feishu_group.ChatGroup import ChatGroup


@allure.feature("test group")
class TestGroup:
    def setup_class(self):
        self.chat_ids = list()
        self.group = ChatGroup()

    def setup(self):
        print("start test")

    def teardown(self):
        print("end test")

    @pytest.mark.run(order=1)
    @allure.story("add group")
    @pytest.mark.parametrize('name', load_yaml('group.yml')['name'])
    def test_add_group(self, name):
        r = self.group.create_group(name)
        print("created", self.chat_ids)
        self.chat_ids.append(r['data']['chat_id'])
        print("created", self.chat_ids)
        assert r.get("code") == 0
        return self.chat_ids

    @pytest.mark.run(order=2)
    @allure.story("get all chat_ids")
    def test_get_data(self):
        print(self.chat_ids)

    @pytest.mark.run(order=3)
    @allure.story("get all group")
    def test_get_group(self):
        print("self.chat_ids: ", self.chat_ids)
        if self.chat_ids:
            for item in self.chat_ids:
                chat_id = item
                r = self.group.get_group(chat_id)
                print(r)
                assert r.get("code") == 0
        else:
            print("no group")
            assert False

    @pytest.mark.run(order=4)
    @allure.story("delete all  group")
    def test_delete_group(self):
        if self.chat_ids:
            for item in self.chat_ids:
                chat_id = item
                r = self.group.delete_group(chat_id)
                assert r.get("code") == 0
        else:
            print("no group")
            assert False
