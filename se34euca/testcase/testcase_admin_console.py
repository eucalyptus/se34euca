from se34euca.testcase.testcase_base import *

class testcase_admin_console(testcase_base):

    def create_accounts_and_users_via_admin_console(self):
        print "=== runTest: Launch Instance Basic ==="
        self.eucaUITester.base.test_ui_admin_console_login()
        self.eucaUITester.admin_console.test_ui_create_accounts_and_users_via_admin_console()
        self.eucaUITester.base.test_ui_admin_console_logout()