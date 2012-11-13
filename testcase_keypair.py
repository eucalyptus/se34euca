from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_keypair(lib_euca_ui_test):

    def generate_keypair(self):
	print "=== runTest: Generate Keypair ==="
	self.test_ui_login()
	self.test_ui_generate_keypair()
	self.test_ui_logout()

    def delete_keypair(self):
	print "=== runTest: Delete Keypair ==="
	self.test_ui_login()
	self.test_ui_delete_keypair()
	self.test_ui_logout()


if __name__ == "__main__":
    unittest.main()



