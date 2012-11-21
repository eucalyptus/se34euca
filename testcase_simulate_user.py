from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_simulate_user(lib_euca_ui_test):

    def simulate_user_case_00(self):
	sleep_time = 2
	wait_time = 120
	print "=== runTest: Simulate User Case 00 ==="
	self.test_ui_login()
	self.test_ui_gotopage_dashboard()
	self.test_ui_gotopage_images()
	self.test_ui_gotopage_dashboard()
	self.test_ui_generate_keypair()
	self.test_ui_gotopage_dashboard()
	self.test_ui_create_security_group()
	self.test_ui_gotopage_dashboard()
	self.test_ui_create_volume()
	time.sleep(sleep_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_launch_instance_basic()
        time.sleep(wait_time)
	self.test_ui_view_page_get_dashboard_source()
	self.test_ui_gotopage_dashboard()
	self.test_ui_terminate_instance_all()
	self.test_ui_gotopage_dashboard()
	self.test_ui_delete_volume_all()
	time.sleep(sleep_time)
	self.test_ui_gotopage_dashboard()
	self.test_ui_delete_security_group_all()
	self.test_ui_gotopage_dashboard()
	self.test_ui_delete_keypair_all()
	self.test_ui_view_page_get_dashboard_source()

if __name__ == "__main__":
    unittest.main()



