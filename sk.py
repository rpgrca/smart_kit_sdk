import requests
import json

class SmartKitConnection:
    API_TOKEN = "3939E0F2-08E5-4BB1-B3A6-DDB1183666D3"
    API_URL_BASE = "https://bgh-services.solidmation.com/1.0/"
    API_URL = API_URL_BASE + "HomeCloudServiceAdmin.svc/"

    def __init__(self, token):
        self.__session = requests.Session()
        self.__token = token

    def _get_http_headers(self):
        headers = requests.utils.default_headers()
        headers.update({
            'Content-Type': 'application/json; charset="utf-8"'
        })
        return headers

    def _post(self, command, **kwargs):
        return self.__session.post(self.API_URL + command,
                                   headers=self._get_http_headers(), **kwargs)

    def _post_at_HomeCloudService(self, command, **kwargs):
        return self.__session.post(self.API_URL_BASE + "HomeCloudService.svc/" + command,
                                   headers=self._get_http_headers(), **kwargs)

    def _get(self, command, **kwargs):
        return self.__session.get(self.API_URL_BASE + command,
                                  headers=self._get_http_headers(), **kwargs)

#    def ping(self):
#        result = self._get("HomeCloudCommandService.svc")
#        return result.status_code == 200

    def ping(self):
        result = self._post_at_HomeCloudService("Ping")
        return result.json().get("PingResult")

    def ping_with_token(self):
        data = json.dumps({ "token": { "token": self.__token } })
        result = self._post_at_HomeCloudService("PingWithToken", data=data)
        return result.json().get("PingWithTokenResult")

    def login(self, email, password):
        result = self._post("Login", data=str({ "token": { "Token": self.__token }, "eMail": email, "password": password }))
        print(result.content)
        return result

    def send_forgotten_password_email(self, email):
        result = self._post("SendForgottenPasswordEmail", data={ "token": { "token": self.__token }, "eMail": email })
        return result

    def get_account(self):
        result = self._post_at_HomeCloudService("GetAccount", data={ "token": self.__token })
        return result

token = ''
with open('account.token') as f:
    token = f.readline().rstrip()

print(token)
sk = SmartKitConnection(SmartKitConnection.API_TOKEN)
result = sk.ping()
print(result)

# vim:ts=4:nowrap
