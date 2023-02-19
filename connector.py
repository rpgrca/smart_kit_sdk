import requests


class Connector:
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

    def post_at_HomeCloudService(self, command, **kwargs):
        result = self.__session.post(self.API_URL_BASE + "HomeCloudService.svc/" + command,
                                     headers=self._get_http_headers(), **kwargs)
        if result.status_code == 200:
            return result.json()

        return None

    def post_at_HomeCloudServiceAdmin(self, command, **kwargs):
        result = self.__session.post(self.API_URL_BASE + "HomeCloudServiceAdmin.svc/" + command,
                                     headers=self._get_http_headers(), **kwargs)
        if result.status_code == 200:
            return result.json()

        return None

    def get(self, command, **kwargs):
        result = self.__session.get(self.API_URL_BASE + command,
                                    headers=self._get_http_headers(), **kwargs)
        if result.status_code == 200:
            return result.json()

        return None
