from se34euca.testcase.testcase_base import *

class testcase_instance(testcase_base):

    def launch_instance_basic(self):
        print "=== runTest: Launch Instance Basic ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_basic()
        self.eucaUITester.base.test_ui_logout()

    def terminate_instance_basic(self):
        print "=== runTest: Terminate Instance Basic ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_terminate_instance_basic()
        self.eucaUITester.base.test_ui_logout()

    def terminate_instance_all(self):
        print "=== runTest: Terminate Instance All ==="
        self.eucaUITester.base.test_ui_login()

        self.eucaUITester.instance.test_ui_terminate_instance_all()
        self.eucaUITester.instance.test_ui_check_running_instances_count(0)
        self.eucaUITester.base.test_ui_logout()

    def launch_instance_from_images_lp(self):
        print "=== runTest: Launch Instance from Images Landing Page ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_from_images_lp()
        self.eucaUITester.base.test_ui_logout()

    def launch_instance_from_instances_lp(self):
        print "=== runTest: Launch Instance from Instances Landing Page ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_from_instances_lp()
        self.eucaUITester.base.test_ui_logout()

    def launch_more_like_this(self):
        print "=== runTest: Launch More Instances Like This ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_more_like_this()
        self.eucaUITester.base.test_ui_logout()


    def launch_instance_given_name_security_group_keypair(self):
        print "=== runTest: Launch Instance Named testinstance security group 'mywebservice' keypair my-sel-gen-key-00 ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_given_name_security_group_keypair("testinstance","mywebservice","my-sel-gen-key-00")
        self.eucaUITester.base.test_ui_logout()

    def launch_and_terminate_instance(self):
        print "=== runTest: Launch and Terminate Instance ==="
        pause=5 #length of pause in seconds
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_basic()
        time.sleep(pause)
        self.eucaUITester.instance.test_ui_terminate_instance_basic()
        self.eucaUITester.base.test_ui_logout()
        time.sleep(pause)

    def associate_ip_from_inst_lp(self):
        print "=== runTest: Associate IP from Instances Landing Page ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_associate_ip_from_inst_lp()
        self.eucaUITester.base.test_ui_logout()

    def disassociate_ip_from_inst_lp(self):
        print "=== runTest: Disassociate IP from Instances Landing Page ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_disassociate_ip_from_inst_lp()
        self.eucaUITester.base.test_ui_logout()


    def associate_ip_from_ip_lp(self):
        print "=== runTest: Associate IP from IP Landing Page ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_associate_ip_from_ip_lp()
        self.eucaUITester.base.test_ui_logout()


    def disassociate_ip_from_ip_lp(self):
        print "=== runTest: Associate IP from IP Landing Page ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_disassociate_ip_from_ip_lp()
        self.eucaUITester.base.test_ui_logout()


if __name__ == "__main__":
    unittest.main()



