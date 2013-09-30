from se34euca.testcase.testcase_base import *


class testcase_utility(testcase_base):
    def change_password(self):
        print "=== runTest: Change Password ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.utility.test_ui_change_password("testpass1")
        self.eucaUITester.utility.test_ui_change_password("mypassword1")
        self.eucaUITester.base.test_ui_logout()

    def clean_up(self):
        print "=== runTest: Clean Up ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.utility.test_ui_clean_up()
        self.eucaUITester.base.test_ui_logout()


if __name__ == "__main__":
    unittest.main()



