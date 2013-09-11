from se34euca.testcase.testcase_base import *

class testcase_snapshot(testcase_base):

    def delete_snapshot(self):
        print "=== runTest: Delete Snapshot ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.snapshot.test_ui_delete_snapshot()
        self.eucaUITester.base.test_ui_logout()

    def create_volume_from_snapshot(self):
        print "=== runTest: Create Volume From Snapshot ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.snapshot.test_ui_create_volume_from_snapshot()
        self.eucaUITester.base.test_ui_logout()

if __name__ == "__main__":
    unittest.main()



