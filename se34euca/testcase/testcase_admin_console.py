from se34euca.testcase.testcase_base import *

class testcase_admin_console(testcase_base):

    def create_accounts_and_users_via_admin_console(self):
        print "=== runTest: Create Accounts via Admin Console ==="
        self.eucaUITester.base.test_ui_admin_console_login()
        self.eucaUITester.admin_console.test_ui_create_accounts_and_users_via_admin_console()
        self.eucaUITester.base.test_ui_admin_console_logout()

    def create_then_delete_accounts_via_admin_console(self):
        print "=== runTest: Create then Delete Accounts via Admin Console ==="
        self.eucaUITester.base.test_ui_admin_console_login()
        self.eucaUITester.admin_console.test_ui_create_then_delete_accounts_via_admin_console(10)
        self.eucaUITester.base.test_ui_admin_console_logout()