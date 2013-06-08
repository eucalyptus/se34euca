from se34euca.testcase.testcase_base import *

class testcase_keypair(testcase_base):

    def generate_keypair(self):
	print "=== runTest: Generate Keypair ==="
	self.eucaUITester.test_ui_login()
	self.eucaUITester.test_ui_generate_keypair()
	self.eucaUITester.test_ui_logout()

    def delete_keypair(self):
	print "=== runTest: Delete Keypair ==="
	self.eucaUITester.test_ui_login()
	self.eucaUITester.test_ui_delete_keypair()
	self.eucaUITester.test_ui_logout()


if __name__ == "__main__":
    unittest.main()



