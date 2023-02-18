import unittest
from sk import SmartKitConnection


class HomeCloudServiceTests(unittest.TestCase):
    # b'{"PingWithTokenResult":{"Messages":[{"Code":8001,"Description":"The Access Token is invalid or it doesn\'t have the Privileges for executing the requested method."}],"Status":2}}'
    def test_ping_with_token_should_return_status_2(self):
        sut = SmartKitConnection(SmartKitConnection.API_TOKEN)
        response = sut.ping_with_token()
        self.assertEqual(2, response.get("Status"))
        self.assertEqual(8001, response.get("Messages")[0].get("Code"))
        self.assertIn("The Access Token is invalid", response.get("Messages")[0].get("Description"))

    # {'PingResult': {'Messages': [], 'Status': 0}}
    def test_ping_should_return_0(self):
        sut = SmartKitConnection(SmartKitConnection.API_TOKEN)
        response = sut.ping()
        self.assertEqual(0, response.get("Status"))
        self.assertFalse(response.get("Messages"))


if __name__ == "__main__":
    unittest.main()
