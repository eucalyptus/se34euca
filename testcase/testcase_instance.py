from se34euca.testcase.testcase_base import *

class testcase_instance(testcase_base):

    def launch_instance_basic(self):
	print "=== runTest: Launch Instance Basic ==="
	self.eucaUITester.test_ui_login()
	self.eucaUITester.test_ui_launch_instance_basic()
	self.eucaUITester.test_ui_logout()

    def terminate_instance_basic(self):
	print "=== runTest: Terminate Instance Basic ==="
	self.eucaUITester.test_ui_login()
	self.eucaUITester.test_ui_terminate_instance_basic()
	self.eucaUITester.test_ui_logout()

    def terminate_instance_all(self):
	print "=== runTest: Terminate Instance All ==="
	self.eucaUITester.test_ui_login()
	self.eucaUITester.test_ui_terminate_instance_all()
	self.eucaUITester.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



