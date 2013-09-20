import unittest
from se34euca.lib.EucaUITester import *
#from eucaops import Eucaops

class testcase_base(unittest.TestCase):
    eucaUITester = EucaUITester()

    def setSeleniumServerInfo(self, ip, port):
        self.eucaUITester.setSeleniumServerInfo(ip, port)

    def setUIInfo(self, ip, port, protocol):
        self.eucaUITester.setUIInfo(ip, port, protocol)

    def setUserInfo(self, accountname, username, password):
        self.eucaUITester.setUserInfo(accountname, username, password)

    def setUp(self):
        self.eucaUITester.setUp()
        #  self.eutester = Eucaops(config_file='/Users/alicehubenko/2b_tested.lst', password='foobar')

    def tearDown(self):
        self.eucaUITester.tearDown()


if __name__ == "__main__":
    unittest.main()



