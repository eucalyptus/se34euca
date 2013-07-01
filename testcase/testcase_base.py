import unittest, time, re
from se34euca.lib.EucaUITester import *

class testcase_base(unittest.TestCase):

    eucaUITester = EucaUITester()

    def setKeys_count(self, keys_count):
        self.keys_count=keys_count

    def setIP_address_count(self, ip_count):
        self.ip_count=ip_count

    def setSeleniumServerInfo(self, ip, port):
        self.eucaUITester.setSeleniumServerInfo(ip, port)

    def setUIInfo(self, ip, port):
        self.eucaUITester.setUIInfo(ip, port)

    def setUserInfo(self, accountname, username, password):
        self.eucaUITester.setUserInfo(accountname, username, password)

    def setUp(self):
        self.eucaUITester.setUp()

    def tearDown(self):
        self.eucaUITester.tearDown()

if __name__ == "__main__":
    unittest.main()



