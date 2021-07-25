import yaml
import pytest
from typing import List


def get_datas(name):
    with open(r'D:\PyCharmWork\feishu\test_feishu_selinum\datas\test_datas.yml', encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name]
    return (datas)


@pytest.fixture(params=get_datas('name'))
def add_group(request):
    print(request.param)
    return request.param



# if __name__ == '__main__':
#     add_group