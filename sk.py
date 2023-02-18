import requests
import json

try:
    from secrets.secrets import *
except ImportError:
    from secrets.empty_secrets import *

class SmartKitConnection:
    APPLICATION_TOKEN = "3939E0F2-08E5-4BB1-B3A6-DDB1183666D3"
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

    def _post_at_HomeCloudServiceAdmin(self, command, **kwargs):
        return self.__session.post(self.API_URL_BASE + "HomeCloudServiceAdmin.svc/" + command,
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
        data = json.dumps({ "token": { "Token": self.__token } })
        result = self._post_at_HomeCloudService("PingWithToken", data=data)
        return result.json().get("PingWithTokenResult")

    def get_account(self):
        data = json.dumps({ "token": { "Token": self.__token } })
        result = self._post_at_HomeCloudService("GetAccount", data=data)
        return result.json().get("GetAccountResult")
    
    def check_for_new_firmware_available(self, home_id):
        data = json.dumps({ "token": { "Token": self.__token }, "homeid": home_id })
        result = self._post_at_HomeCloudService("CheckForNewFirmwareAvailable", data=data)
        return result.json().get("CheckForNewFirmwareAvailableResult")

    def login(self, email, password):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "email": email, "password": password })
        result = self._post_at_HomeCloudServiceAdmin("Login", data=data)
        return result.json().get("LoginResult")
 
    def login_with_expiration(self, email, password, expiration):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "email": email, "password": password, "expiration": expiration })
        result = self._post_at_HomeCloudServiceAdmin("LoginWithExpiration", data=data)
        return result.json().get("LoginWithExpirationResult")
    
    def send_forgotten_password_email(self, email):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "email": email })
        result = self._post_at_HomeCloudServiceAdmin("SendForgottenPasswordEmail", data=data)
        print(result)
        return result.json()

if __name__ == "__main__":
    sk = SmartKitConnection(ACCESS_KEY)
    result = sk.login(EMAIL, PASSWORD)
    print(result)

# vim:ts=4:nowrap
