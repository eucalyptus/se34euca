from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_instance(lib_euca_ui_test):

    def launch_instance_basic(self):
	print "=== runTest: Launch Instance Basic ==="
	self.test_ui_login()
	self.test_ui_launch_instance_basic()
	self.test_ui_logout()


    def terminate_instance_basic(self):
	print "=== runTest: Terminate Instance Basic ==="
	self.test_ui_login()
	self.test_ui_terminate_instance_basic()
	self.test_ui_logout()

    def terminate_instance_all(self):
	print "=== runTest: Terminate Instance All ==="
	self.test_ui_login()
	self.test_ui_terminate_instance_all()
	self.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



