from se34euca.testcase.testcase_base import *

class testcase_security_group(testcase_base):

    def create_security_group(self):
        print "=== runTest: Create Security Group ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_create_security_group()
        self.eucaUITester.base.test_ui_logout()

    def create_empty_security_group(self):
        print "=== runTest: Create Empty Security Group ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_create_empty_security_group()
        self.eucaUITester.base.test_ui_logout()

    def add_rules_to_security_group(self):
        print "=== runTest: Add Rules to Security Group ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_add_rules_to_security_group()
        self.eucaUITester.base.test_ui_logout()

    def delete_security_group(self):
        print "=== runTest: Delete Security Group ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_delete_security_group()
        self.eucaUITester.base.test_ui_logout()

    def delete_security_group_all(self):
        print "=== runTest: Delete Security Group All ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_delete_security_group_all()
        self.eucaUITester.base.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



