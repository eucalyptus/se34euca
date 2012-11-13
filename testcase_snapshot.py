from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_snapshot(lib_euca_ui_test):

    def delete_snapshot(self):
	print "=== runTest: Delete Snapshot ==="
	self.test_ui_login()
	self.test_ui_delete_snapshot()
	self.test_ui_logout()

    def create_volume_from_snapshot(self):
        print "=== runTest: Create Volume From Snapshot ==="
        self.test_ui_login()
        self.test_ui_create_volume_from_snapshot()
        self.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



