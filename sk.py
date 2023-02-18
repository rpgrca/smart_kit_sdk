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
        data = json.dumps({ "token": { "Token": self.__token }, "homeID": home_id })
        result = self._post_at_HomeCloudService("CheckForNewFirmwareAvailable", data=data)
        return result.json().get("CheckForNewFirmwareAvailableResult")

    def login(self, email, password):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "eMail": email, "password": password })
        result = self._post_at_HomeCloudServiceAdmin("Login", data=data)
        return result.json().get("LoginResult")
 
    def login_with_expiration(self, email, password, expiration):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "eMail": email, "password": password, "expiration": expiration })
        result = self._post_at_HomeCloudServiceAdmin("LoginWithExpiration", data=data)
        return result.json().get("LoginWithExpirationResult")
    
    def send_forgotten_password_email(self, email):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "eMail": email })
        result = self._post_at_HomeCloudServiceAdmin("SendForgottenPasswordEmail", data=data)
        return result.json().get("SendForgottenPasswordEmailResult")

    def get_login_details(self):
        data = json.dumps({ "token": { "Token": self.__token } })
        result = self._post_at_HomeCloudService("GetLoginDetails", data=data)
        return result.json().get("GetLoginDetailsResult")

    def get_firmware_information(self, device):
        data = json.dumps({ "token": { "Token": self.__token }, "deviceModelDescription": device })
        result = self._post_at_HomeCloudService("GetFirmwareInformation", data=data)
        return result.json().get("GetFirmwareInformationResult")

    def get_firmware_information_for_all_models(self):
        data = json.dumps({ "token": { "Token": self.__token } })
        result = self._post_at_HomeCloudService("GetFirmwareInformationForAllModels", data=data)
        return result.json().get("GetFirmwareInformationForAllModelsResult")

    def get_group(self, group_id):
        data = json.dumps({ "token": { "Token": self.__token }, "groupID": group_id })
        result = self._post_at_HomeCloudService("GetGroup", data=data)
        return result.json().get("GetGroupResult")

    def get_home(self, home_id):
        data = json.dumps({ "token": { "Token": self.__token }, "homeID": home_id })
        result = self._post_at_HomeCloudService("GetHome", data=data)
        return result.json().get("GetHomeResult")

    def get_endpoint_usage_records(self, home_id, endpoint_id, date_from, date_to, time_to, language = "ES", width = 640, height = 480, color = 0xff0000, query_type = 0, email = None):
        usage = {
            "HomeID": home_id,
            "EndpointID": endpoint_id,
            "DateFrom": date_from,
            "DateTo": date_to,
            "TimeTo": time_to,
            "LanguageCode": language,
            "ScreenWidth": width,
            "ScreenHeight": height,
            "MeteringQueryType": query_type,
            "EndpointIDsForDoorlockEvents": None,
            "CustomerColorAsHex": color,
            "EmailAddressForDownload": email
        }
        data = json.dumps({ "token": { "Token": self.__token }, "parameters": usage })
        result = self._post_at_HomeCloudService("GetEndpointUsageRecords", data=data)
        return result.json().get("GetEndpointUsageRecordsResult")


if __name__ == "__main__":
    sk = SmartKitConnection(ACCESS_KEY)
#    result = sk.get_endpoint_usage_records(HOME_ID, ENDPOINT_ID, { "Day": 17, "Month": 2, "Year": 2023 }, { "Day": 18, "Month": 2, "Year": 2023 }, { "Hour": 23, "Minute": 59, "Second": 59, "Millisecond": 0 }, query_type = 1)

    result = sk.get_firmware_information("HPA-4911")
    print(result)

# vim:ts=4:nowrap
