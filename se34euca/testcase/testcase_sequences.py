from se34euca.testcase.testcase_base import *

class testcase_sequences(testcase_base):

    def instance_operations(self):
        print "=== runTest: Instance Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_basic()
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        self.eucaUITester.instance.test_ui_launch_more_like_this()
        self.eucaUITester.instance.test_ui_check_running_instances_count("2")
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        self.eucaUITester.instance.test_ui_check_running_instances_count("0")
        self.eucaUITester.instance.test_ui_launch_instance_from_instances_lp()
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        self.eucaUITester.instance.test_ui_launch_instance_from_images_lp()
        self.eucaUITester.instance.test_ui_check_running_instances_count("2")
        self.eucaUITester.base.test_ui_logout()



if __name__ == "__main__":
    unittest.main()

