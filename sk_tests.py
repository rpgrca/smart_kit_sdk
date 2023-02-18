import unittest
from sk import SmartKitConnection

try:
    from secrets.secrets import *
except ImportError:
    from secrets.empty_secrets import *

class HomeCloudServiceTests(unittest.TestCase):
    # {'PingResult': {'Messages': [], 'Status': 0}}
    @unittest.skip("working")
    def test_ping_should_return_0(self):
        sut = SmartKitConnection("")
        response = sut.ping()
        self.assertEqual(0, response.get("Status"))
        self.assertFalse(response.get("Messages"))

    # b'{"PingWithTokenResult":{"Messages":[{"Code":8001,"Description":"The Access Token is invalid or it doesn\'t have the Privileges for executing the requested method."}],"Status":2}}'
    @unittest.skip("working")
    def test_ping_with_invalid_token_should_return_status_2(self):
        sut = SmartKitConnection("")
        response = sut.ping_with_token()
        self.assertEqual(2, response.get("Status"))
        self.assertEqual(8001, response.get("Messages")[0].get("Code"))
        self.assertIn("The Access Token is invalid", response.get("Messages")[0].get("Description"))

    # {'GetAccountResult': {'Account': None, 'ResponseStatus': {'Messages': [{'Code': 8001, 'Description': "The Access Token is invalid or it doesn't have the Privileges for executing the requested method."}], 'Status': 2}}}
    @unittest.skip("working")
    def test_get_account_should_return_status_2(self):
        sut = SmartKitConnection("")
        response = sut.get_account()
        self.assertIsNone(response.get("Account"))
        self.assertEqual(2, response.get("ResponseStatus").get("Status"))
        self.assertEqual(8001, response.get("ResponseStatus").get("Messages")[0].get("Code"))
        self.assertIn("The Access Token is invalid", response.get("ResponseStatus").get("Messages")[0].get("Description"))

    #@unittest.skipIf(HOME_ID is None or ACCESS_KEY is None, "secrets file not found, impossible to get responses from server")
    # b'{"CheckForNewFirmwareAvailableResult":{"NewFirmwareAvailable":false,"ResponseStatus":{"Messages":[{"Code":8001,"Description":"The Access Token is invalid or it doesn\'t have the Privileges for executing the requested method."}],"Status":2}}}'
    @unittest.skip("working")
    def test_check_for_new_firmware_available_with_invalid_access_token_and_home_id_should_return_false(self):
        sut = SmartKitConnection("")
        response = sut.check_for_new_firmware_available("")
        self.assertFalse(response.get("NewFirmwareAvailable"))
        self.assertEqual(2, response.get("ResponseStatus").get("Status"))
        self.assertEqual(8001, response.get("ResponseStatus").get("Messages")[0].get("Code"))
        self.assertIn("The Access Token is invalid", response.get("ResponseStatus").get("Messages")[0].get("Description"))

    # b'{"LoginResult":{"AccessToken":null,"LoginType":0,"ResponseStatus":{"Messages":[{"Code":1001,"Description":"The e-mail address or the Password are incorrect."}],"Status":3}}}'
    # b'{"LoginResult":{"AccessToken":null,"LoginType":0,"ResponseStatus":{"Messages":[{"Code":8000,"Description":"The Application Token is invalid or it doesn\'t have the Privileges for executing the requested method."}],"Status":2}}}'
    # b'{"SendForgottenPasswordEmailResult":{"ResponseStatus":{"Messages":[{"Code":8000,"Description":"The Application Token is invalid or it doesn\'t have the Privileges for executing the requested method."}],"Status":2}}}'
    # b'{"LoginWithExpirationResult":{"AccessToken":null,"LoginType":0,"ResponseStatus":{"Messages":[{"Code":8000,"Description":"The Application Token is invalid or it doesn\'t have the Privileges for executing the requested method."}],"Status":2}}}'

if __name__ == "__main__":
    unittest.main()
