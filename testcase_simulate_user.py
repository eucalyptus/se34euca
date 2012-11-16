from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_simulate_user(lib_euca_ui_test):

    def simulate_user_case_00(self):
	sleep_time = 2
	wait_time = 120
	break_time = 5
	print "=== runTest: Simulate User Case 00 ==="
	self.test_ui_login()
	self.test_ui_gotopage_dashboard()
	self.test_ui_generate_keypair()
	time.sleep(sleep_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_create_security_group()
        time.sleep(sleep_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_create_volume()
	time.sleep(sleep_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_launch_instance_basic()
        time.sleep(wait_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_terminate_instance_basic()
	time.sleep(sleep_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_delete_volume()
	time.sleep(sleep_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_delete_security_group()
        time.sleep(sleep_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_delete_keypair()
	time.sleep(break_time)


if __name__ == "__main__":
    unittest.main()



