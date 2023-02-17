import requests

class SmartKitConnection:
    API_TOKEN = "3939E0F2-08E5-4BB1-B3A6-DDB1183666D3"
    API_URL_BASE = "https://bgh-services.solidmation.com/1.0/"
    API_URL = API_URL_BASE + "HomeCloudServiceAdmin.svc/"

    def __init__(self):
        self.__session = requests.Session()

    def _get_http_headers(self):
        headers = requests.utils.default_headers()
        headers.update({
            'Content-Type': 'application/json; charset="utf-8"'
        })
        return headers

    def _post(self, command, **kwargs):
        return self.__session.post(self.API_URL + command,
                                   headers=self._get_http_headers(), **kwargs)

    def _get(self, command, **kwargs):
        return self.__session.get(self.API_URL_BASE + command,
                                  headers=self._get_http_headers(), **kwargs)

    def ping(self):
        result = self._get("HomeCloudCommandService.svc")
        return result.status_code == 200

    def ping2(self):
        result = self._post("Ping", data=f"token={self.API_TOKEN}")
        return result

    def login(self, email, password):
        result = self._post("Login", data=f"token={self.API_TOKEN}&eMail={email}&password={password}")
        print(result.content)
        return result

sk = SmartKitConnection()
result = sk.ping2()
print(result.content)
