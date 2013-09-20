from se34euca.testcase.testcase_base import *


class testcase_view_page(testcase_base):
    def check_login_and_logout(self):
        print "=== runTest: Check Login and Logout ==="
        print
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.base.test_ui_logout()

    def get_dashboard_source(self):
        print "=== runTest: Get Dashboard Source ==="
        print
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.base.test_ui_view_page_get_dashboard_source()
        self.eucaUITester.base.test_ui_logout()

    def view_keypairs_page(self):
        print "=== runTest: View Keypairs Page ==="
        print
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_gotopage_keypairs()
        self.eucaUITester.base.test_ui_logout()

    def view_running_page(self):
        print "=== runTest: View Running Page ==="
        print
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_gotopage_running()
        self.eucaUITester.base.test_ui_logout()

    def view_security_groups_page(self):
        print "=== runTest: View Security Groups Page ==="
        print
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_gotopage_security_groups()
        self.eucaUITester.base.test_ui_logout()

    def view_volumes_page(self):
        print "=== runTest: View Volumes Page ==="
        print
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.volume.test_ui_gotopage_volumes()
        self.eucaUITester.base.test_ui_logout()

    def view_images_page(self):
        print "=== runTest: View Images Page ==="
        print
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.image.test_ui_gotopage_images()
        self.eucaUITester.base.test_ui_logout()

    def view_all_page(self):
        print "=== runTest: View All Page ==="
        print
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_gotopage_keypairs()
        self.eucaUITester.instance.test_ui_gotopage_running()
        self.eucaUITester.security_group.test_ui_gotopage_security_groups()
        self.eucaUITester.volume.test_ui_gotopage_volumes()
        self.eucaUITester.image.test_ui_gotopage_images()
        self.eucaUITester.base.test_ui_view_page_get_dashboard_source()
        self.eucaUITester.base.test_ui_logout()

    def view_all_page_in_loop(self):
        print "=== runTest: View All Page In Loop ==="
        print
        self.eucaUITester.base.test_ui_login()
        while True:
            try:
                print "Test: view_all_page_in_loop - Click Through All Landing Pages"
                print
                self.eucaUITester.keypair.test_ui_gotopage_keypairs()
                self.eucaUITester.instance.test_ui_gotopage_running()
                self.eucaUITester.security_group.test_ui_gotopage_security_groups()
                self.eucaUITester.volume.test_ui_gotopage_volumes()
                self.eucaUITester.image.test_ui_gotopage_images()
                self.eucaUITester.base.test_ui_view_page_get_dashboard_source()
                print "Test: view_all_page_in_loop - Sleep 5 Sec"
                print
                time.sleep(5)
            except:
                print "Test: view_all_page_in_loop - Catched Exception: Try to Log Back In"
                print
                self.eucaUITester.base.test_ui_login()


if __name__ == "__main__":
    unittest.main()



