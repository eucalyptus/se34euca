from se34euca.testcase.testcase_base import *

class testcase_security_group(testcase_base):

    def create_security_group(self):
	print "=== runTest: Create Security Group ==="
	self.eucaUITester.test_ui_login()
	self.eucaUITester.test_ui_create_security_group()
	self.eucaUITester.test_ui_logout()

    def delete_security_group(self):
	print "=== runTest: Delete Security Group ==="
	self.eucaUITester.test_ui_login()
	self.eucaUITester.test_ui_delete_security_group()
	self.eucaUITester.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



