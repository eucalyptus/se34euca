from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_ip_address(lib_euca_ui_test):

    def allocate_two_ip_addresses(self):
	print "=== runTest: Allocate Two IP Addresses ==="
	self.test_ui_login()
	self.test_ui_allocate_two_ip_addresses()
	self.test_ui_logout()

    def release_ip_address(self):
	print "=== runTest: Release IP Address ==="
	self.test_ui_login()
	self.test_ui_release_ip_address()
	self.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



