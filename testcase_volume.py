from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_volume(lib_euca_ui_test):

    def create_volume(self):
	print "=== runTest: Create Volume ==="
	self.test_ui_login()
	self.test_ui_create_volume()
	self.test_ui_logout()

    def delete_volume(self):
	print "=== runTest: Delete Volume ==="
	self.test_ui_login()
	self.test_ui_delete_volume()
	self.test_ui_logout()

    def create_snapshot_from_volume(self):
	print "=== runTest: Create Snapshot From Volume ==="
        self.test_ui_login()
        self.test_ui_create_snapshot_from_volume()
        self.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



