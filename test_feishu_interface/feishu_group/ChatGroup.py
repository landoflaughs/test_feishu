from test_feishu_interface.feishu_group.base import Base


class ChatGroup(Base):
    # def __init__(self):
    #     super().__init__()
    #     self.chat_id = ""
    #     # self.chat_id = self.create_group()['data']['chat_id']

    def create_group(self, name):
        url = "https://open.feishu.cn/open-apis/im/v1/chats"
        data = {
            "name": name}
        r = self.send("POST", url, json=data)
        return r.json()

    def get_group(self, chat_id):
        url = f"https://open.feishu.cn/open-apis/im/v1/chats/{chat_id}"
        r = self.send("get", url)
        print("get")
        return r.json()

    def delete_group(self, chat_id):
        url = f"https://open.feishu.cn/open-apis/im/v1/chats/{chat_id}"
        r = self.send("DELETE", url)
        print("del: ", r.json())
        return r.json()



# if __name__ == '__main__':
#     chat = ChatGroup()
#     chat.create_group()
#     chat.get_group()
#     chat.delete_group()