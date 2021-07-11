import yaml


def load_yaml(url):
    with open(url, encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    return all_datas
