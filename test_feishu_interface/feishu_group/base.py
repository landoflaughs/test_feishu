import requests


# "Verification Token" = d8hxdFbZiTM7YhPregZkdhVCC1IvDZZI

class Base:
    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        params = {
            "app_id": "cli_a06bdefe0eb8500e",
            "app_secret": "gHS6GMdHfnONwr6HXdpRidEFKHodXGSH"
        }
        r = self.s.post(url, params=params)
        return r.json()['tenant_access_token']

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)




# if __name__ == '__main__':
#     b = Base()
#     b.get_token()
