from se34euca.testcase.testcase_base import *


class testcase_keypair(testcase_base):
    def generate_keypair(self):
        print "=== runTest: Generate Keypair ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_generate_keypair()
        #print "EUTESTER!!!"
        #print
        #print "THis is stdin:" + str(sys.stdin) + ", stderr: " + str(sys.stderr) +", stdout:" + str(sys.stdout)
        #emi=self.eutester.get_emi()
        #print emi
        #print
        self.eucaUITester.base.test_ui_logout()

    def import_keypair(self):
        print "=== runTest: Generate Keypair ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_import_keypair()
        self.eucaUITester.base.test_ui_logout()

    def delete_keypair(self):
        print "=== runTest: Delete Keypair ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_delete_keypair()
        self.eucaUITester.base.test_ui_logout()

    def delete_keypair_all(self):
        print "=== runTest: Delete Keypair All ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_delete_keypair_all()
        self.eucaUITester.base.test_ui_logout()

    def create_keypair_given_name(self, keypair_name):
        print "=== runTest: Create Keypair Given Name ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_generate_keypair_given_name(keypair_name)
        self.eucaUITester.base.test_ui_logout()

    def create_keypair_given_name_then_delete_it(self, keypair_name='testkey-789'):
        print "=== runTest: Create Keypair Named testkey-789 then Delete It==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_generate_keypair_given_name(keypair_name)
        self.eucaUITester.keypair.test_ui_delete_keypair_given_name(keypair_name)
        self.eucaUITester.base.test_ui_logout()


if __name__ == "__main__":
    unittest.main()



