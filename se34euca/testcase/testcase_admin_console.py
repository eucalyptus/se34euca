from se34euca.testcase.testcase_base import *

class testcase_admin_console(testcase_base):

    def create_accounts_and_users_via_admin_console(self):
        print "=== runTest: Launch Instance Basic ==="
        self.eucaUITester.base.test_ui_admin_console_login()
        #self.eucaUITester.instance.test_ui_launch_instance_basic()
        self.eucaUITester.base.test_ui_admin_console_logout()