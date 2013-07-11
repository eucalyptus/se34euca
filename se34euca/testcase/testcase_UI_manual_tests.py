from se34euca.testcase.testcase_base import *

class testcase_UI_manual_tests(testcase_base):


#// name the classs to commit_tests

#// give it a more meaningful testcase name

#// def create_and_delete_keypair testcase()
#// def import_and_delete_keypair testcase()
#// def complete_keypair_testcases()
#// def create_and_delete_volume_testcase()
#// def create_and_delete_secutiry_group_testcase()
#// def complete_commit_testcases()

    def UI_manual_tests_01(self):
        sleep_time = 5
        wait_time = 120

        print "=== runTest: UI Manual Tests ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_generate_keypair()
        time.sleep(5)
        self.eucaUITester.keypair.test_ui_check_keypair_count('1')
        time.sleep(5)
        self.eucaUITester.keypair.test_ui_delete_keypair()
        time.sleep(5)
        self.eucaUITester.keypair.test_ui_check_keypair_count('0')
        time.sleep(5)
        self.eucaUITester.keypair.test_ui_import_keypair()
        time.sleep(5)
        self.eucaUITester.keypair.test_ui_check_keypair_count('1')
        time.sleep(5)
        self.eucaUITester.ip_address.test_ui_allocate_two_ip_addresses()
        time.sleep(5)
        self.eucaUITester.base.test_ui_logout()
