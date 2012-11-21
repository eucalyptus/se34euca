from selenium import *
import unittest, time, re
from lib_euca_ui_test import *

class testcase_view_page(lib_euca_ui_test):

    def check_login_and_logout(self):
	print "=== runTest: Check Login and Logout ==="
	print
	self.test_ui_login()
	self.test_ui_logout()

    def get_dashboard_source(self):
	print "=== runTest: Get Dashboard Source ==="
	print
	self.test_ui_login()
	self.test_ui_view_page_get_dashboard_source()
	self.test_ui_logout()

    def view_keypairs_page(self):
	print "=== runTest: View Keypairs Page ==="
	print
	self.test_ui_login()
	self.test_ui_gotopage_keypairs()
	self.test_ui_logout()

    def view_running_page(self):
	print "=== runTest: View Running Page ==="
	print
	self.test_ui_login()
	self.test_ui_gotopage_running()
	self.test_ui_logout()

    def view_security_groups_page(self):
	print "=== runTest: View Security Groups Page ==="
	print
	self.test_ui_login()
	self.test_ui_gotopage_security_groups()
	self.test_ui_logout()

    def view_volumes_page(self):
	print "=== runTest: View Volumes Page ==="
	print
	self.test_ui_login()
	self.test_ui_gotopage_volumes()
	self.test_ui_logout()

    def view_images_page(self):
	print "=== runTest: View Images Page ==="
	print
	self.test_ui_login()
	self.test_ui_gotopage_images()
	self.test_ui_logout()

    def view_all_page(self):
	print "=== runTest: View All Page ==="
	print
	self.test_ui_login()
	self.test_ui_gotopage_keypairs()
	self.test_ui_gotopage_running()
	self.test_ui_gotopage_security_groups()
	self.test_ui_gotopage_volumes()
	self.test_ui_gotopage_images()
	self.test_ui_view_page_get_dashboard_source()
	self.test_ui_logout()

    def view_all_page_in_loop(self):
	print "=== runTest: View All Page In Loop ==="
        print
	self.test_ui_login()
	while True:
	    try:
		print "Test: view_all_page_in_loop - Click Through All Landing Pages"
		print
		self.test_ui_gotopage_keypairs()
		self.test_ui_gotopage_running()
		self.test_ui_gotopage_security_groups()
		self.test_ui_gotopage_volumes()
		self.test_ui_gotopage_images()
		self.test_ui_view_page_get_dashboard_source()
		print "Test: view_all_page_in_loop - Sleep 5 Sec"
		print	
		time.sleep(5)
	    except:
		print "Test: view_all_page_in_loop - Catched Exception: Try to Log Back In"
		print
		self.test_ui_login()

if __name__ == "__main__":
    unittest.main()



