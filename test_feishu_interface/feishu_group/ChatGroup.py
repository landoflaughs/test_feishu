from test_feishu_interface.feishu_group.base import Base


class ChatGroup(Base):
    def create_group(self):
        url = "https://open.feishu.cn/open-apis/im/v1/chats"
