from se34euca.testcase.testcase_base import *

class testcase_sequences(testcase_base):

    sleep_time=5

    def instance_operations(self):
        sleep_time=40
        print "=== runTest: Instance Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_basic()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_launch_more_like_this()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("2")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("0")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_launch_instance_from_instances_lp()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_launch_instance_from_images_lp()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("2")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        time.sleep(sleep_time)
        self.eucaUITester.base.test_ui_logout()

    def keypair_operations(self):
        sleep_time=60
        print "=== runTest: Keypair Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_import_keypair()
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_delete_keypair()
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_check_keypair_count("0")
        time.sleep(sleep_time)
        self.eucaUITester.base.test_ui_logout()
if __name__ == "__main__":
    unittest.main()

