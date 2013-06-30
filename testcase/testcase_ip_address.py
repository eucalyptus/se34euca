from se34euca.testcase.testcase_base import *

class testcase_ip_address(testcase_base):

    def allocate_two_ip_addresses(self):
        print "=== runTest: Allocate Two IP Addresses ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.ip_address.test_ui_allocate_two_ip_addresses()
        self.eucaUITester.base.test_ui_logout()

    def release_ip_address(self):
        print "=== runTest: Release IP Address ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.ip_address.test_ui_release_ip_address()
        self.eucaUITester.base.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



