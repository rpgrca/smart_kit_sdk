from connector import Connector
import json

try:
    from secrets.secrets import *
except ImportError:
    from secrets.empty_secrets import *


class SmartKitConnection:
    APPLICATION_TOKEN = "3939E0F2-08E5-4BB1-B3A6-DDB1183666D3"

    def __init__(self, token, connector: Connector):
        self.__token = token
        self.__connector = connector

    def ping(self):
        result = self.__connector.post_at_HomeCloudService("Ping")
        if result is None:
            return None

        return result.get("PingResult")

    def _post_at_HomeCloudService(self, service: str, token: str, root: str, params: dict[str, str] = {}):
        data = json.dumps({ "token": { "Token": token }} | params)
        result = self.__connector.post_at_HomeCloudService(service, data=data)
        if result is None:
            return None

        return result.get(root)

    def ping_with_token(self):
        return self._post_at_HomeCloudService("PingWithToken", self.__token, "PingWithTokenResult")

    def get_account(self):
        return self._post_at_HomeCloudService("GetAccount", self.__token, "GetAccountResult")
    
    def check_for_new_firmware_available(self, home_id):
        data = json.dumps({ "token": { "Token": self.__token }, "homeID": home_id })
        result = self.__connector.post_at_HomeCloudService("CheckForNewFirmwareAvailable", data=data)
        if result is None:
            return None

        return result.get("CheckForNewFirmwareAvailableResult")

    def login(self, email, password):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "eMail": email, "password": password })
        result = self.__connector.post_at_HomeCloudServiceAdmin("Login", data=data)
        return result.json().get("LoginResult")
 
    def login_with_expiration(self, email, password, expiration):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "eMail": email, "password": password, "expiration": expiration })
        result = self.__connector.post_at_HomeCloudServiceAdmin("LoginWithExpiration", data=data)
        return result.json().get("LoginWithExpirationResult")
    
    def send_forgotten_password_email(self, email):
        data = json.dumps({ "token": { "Token": self.APPLICATION_TOKEN }, "eMail": email })
        result = self.__connector.post_at_HomeCloudServiceAdmin("SendForgottenPasswordEmail", data=data)
        return result.json().get("SendForgottenPasswordEmailResult")

    def get_login_details(self):
        data = json.dumps({ "token": { "Token": self.__token } })
        result = self.__connector.post_at_HomeCloudService("GetLoginDetails", data=data)
        return result.json().get("GetLoginDetailsResult")

    def get_firmware_information(self, device):
        data = json.dumps({ "token": { "Token": self.__token }, "deviceModelDescription": device })
        result = self.__connector.post_at_HomeCloudService("GetFirmwareInformation", data=data)
        return result.json().get("GetFirmwareInformationResult")

    def get_firmware_information_for_all_models(self):
        data = json.dumps({ "token": { "Token": self.__token } })
        result = self.__connector.post_at_HomeCloudService("GetFirmwareInformationForAllModels", data=data)
        return result.json().get("GetFirmwareInformationForAllModelsResult")

    def get_group(self, group_id):
        data = json.dumps({ "token": { "Token": self.__token }, "groupID": group_id })
        result = self.__connector.post_at_HomeCloudService("GetGroup", data=data)
        return result.json().get("GetGroupResult")

    def get_home(self, home_id):
        data = json.dumps({ "token": { "Token": self.__token }, "homeID": home_id })
        result = self.__connector.post_at_HomeCloudService("GetHome", data=data)
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
        result = self.__connector.post_at_HomeCloudService("GetEndpointUsageRecords", data=data)
        return result.json().get("GetEndpointUsageRecordsResult")

    def get_scene(self, scene_id):
        data = json.dumps({ "token": { "Token": self.__token }, "sceneID": scene_id })
        result = self.__connector.post_at_HomeCloudService("GetScene", data=data)
        return result.json().get("GetSceneResult")


if __name__ == "__main__":
    connector = Connector()
    sk = SmartKitConnection(ACCESS_KEY, connector)
#    result = sk.get_endpoint_usage_records(HOME_ID, ENDPOINT_ID, { "Day": 17, "Month": 2, "Year": 2023 }, { "Day": 18, "Month": 2, "Year": 2023 }, { "Hour": 23, "Minute": 59, "Second": 59, "Millisecond": 0 }, query_type = 1)

    result = sk.ping_with_token()
    print(result)

# vim:ts=4:nowrap
