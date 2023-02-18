import unittest
from sk import SmartKitConnection


class SmartKitConnectionPingWithToken(unittest.TestCase):
    # b'{"PingWithTokenResult":{"Messages":[{"Code":8001,"Description":"The Access Token is invalid or it doesn\'t have the Privileges for executing the requested method."}],"Status":2}}'
    def test_with_invalid_token_should_return_status_2(self):
        sut = SmartKitConnection(SmartKitConnection.API_TOKEN)
        response = sut.ping_with_token()
        self.assertEqual(2, response["Status"])
        self.assertEqual(8001, response["Messages"][0]["Code"])
        self.assertIn("The Access Token is invalid", response["Messages"][0]["Description"])


if __name__ == "__main__":
    unittest.main()
