import yaml
import pytest
from typing import List


def get_datas(name):
    with open(r'D:\WORK\jenkins\connect\workspace\windows_appium\feishu_windows_test\test_feishu_appium\datas'
              r'\test_datas.yml', encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name]
    return (datas)


@pytest.fixture(params=get_datas('name'))
def add_group(request):
    print(request.param)
    return request.param



# if __name__ == '__main__':
#     add_group
