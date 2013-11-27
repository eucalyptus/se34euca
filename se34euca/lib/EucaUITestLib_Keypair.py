from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_Keypair(EucaUITestLib_Base):
    def test_ui_gotopage_keypairs(self):
        print
        print "Started Test: GotoPage Keypairs"
        print
        self.click_element_by_id("euca-logo")
        print
        print "Test: Received the Page Title -> " + self.driver.title
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.verify_element_by_id("table-keys-new")
        print
        print "Finished Test: GotoPage Keypairs"
        print
        return 0


    def test_ui_generate_keypair(self):
        print
        print "Started Test: Generate Keypair"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id("table-keys-new")
        print
        print "Test: Generate New Keypair"
        self.set_keys_by_id("key-add-name", "my-sel-gen-key-00")
        self.click_element_by_id("keys-add-btn")
        print
        print "Finished Test: Generate Keypair"
        print
        return 0

    def test_ui_generate_keypair_given_name(self, keypair_name):
        print
        print "Started Test: Generate Keypair Given Name"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id("table-keys-new")
        print
        print "Test: Generate New Keypair"
        self.set_keys_by_id("key-add-name", keypair_name)
        self.click_element_by_id("keys-add-btn")
        print
        print "Finished Test: Generate Keypair Given Name"
        print
        return 0

    def test_ui_import_keypair(self):
        print
        print "Started Test: Import Keypair"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id("table-keys-extra")
        print
        print "Test: Import Keypair"
        self.set_keys_by_id(this_id="key-import-contents",
                            keys="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDI1x6tEjkBQCCP0ssF69vAgP2xg+N9ScoTrqRqyl5w4qEgsV/AppfHHYRKYr0N/tTyG4/z1XGNrB2SaslnRpgEOsvMZldlOnqsUujL2fgoEg+/gB92+1JhZgTjU8nL5j5BFkVTh93nSHtXHdzYl7SjlXrv26ZbyuDwJmI+s6bJQk5noJ4Q4g7N/0y9pHRvezyhgxkyX7PQoA9WJm8SqlakyhMYa0j/baMhb/ehSI0VvwNodmcaWaS6Z2F4rZS4C2DmCUDXYy/1+0tiRTjHjlPbqRKCVKam8ImWytlZD0zbdV/tpADxDpnhW2cPVpXcjy4sRzUCc8AZW+OE3LQxXild alicehubenko@Alices-MacBook-Pro.local")
        self.set_keys_by_id('key-import-name', "import-key")
        self.click_element_by_id("keys-add-btn")
        print
        print "Finished Test: Import Keypair"
        print
        return 0

    def test_ui_import_keypair_given_name(self, keypair_name):
        print
        print "Started Test: Import Keypair Given Name"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id("table-keys-extra")
        print
        print "Test: Import Keypair " + keypair_name
        self.set_keys_by_id(this_id="key-import-contents",
                            keys="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDI1x6tEjkBQCCP0ssF69vAgP2xg+N9ScoTrqRqyl5w4qEgsV/AppfHHYRKYr0N/tTyG4/z1XGNrB2SaslnRpgEOsvMZldlOnqsUujL2fgoEg+/gB92+1JhZgTjU8nL5j5BFkVTh93nSHtXHdzYl7SjlXrv26ZbyuDwJmI+s6bJQk5noJ4Q4g7N/0y9pHRvezyhgxkyX7PQoA9WJm8SqlakyhMYa0j/baMhb/ehSI0VvwNodmcaWaS6Z2F4rZS4C2DmCUDXYy/1+0tiRTjHjlPbqRKCVKam8ImWytlZD0zbdV/tpADxDpnhW2cPVpXcjy4sRzUCc8AZW+OE3LQxXild alicehubenko@Alices-MacBook-Pro.local")
        self.set_keys_by_id('key-import-name', keypair_name)
        self.click_element_by_id("keys-add-btn")
        print
        print "Finished Test: Import Keypair Given Name"
        print
        return 0

    #Verifying on Key Pairs landing page by key pair name that key pair is present
    def test_ui_verify_keypair_given_name(self, keypair_name):
        print
        print "Started Test: Verify Keypair Given Name"
        print 
        self.click_element_by_link_text(link_text="Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print "Verifying that the Keypair " + keypair_name + " exists"
        self.verify_element_by_id(keypair_name)
        print
        print "Finished Test: Verify Keypair Given Name"
        print
        return 0

    def test_ui_verify_delete_keypair_given_name(self, keypair_name):
        print
        print "Started Test: Verify Delete Keypair Given Name"
        print 
        self.click_element_by_link_text(link_text="Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print "Verifying that the Keypair " + keypair_name + " is deleted"
        self.verify_element_not_present("ID", keypair_name)
        print
        print "Finished Test: Verify Delete Keypair Given Name"
        print
        return 0

    def test_ui_check_keypair_count(self, keys_count):
        print
        print "Started Test: Check Keypair Count"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Verifying that Keypair Count on Dashboard is " + keys_count
        self.verify_text_displayed_by_css("#dashboard-netsec-keypair > span", keys_count)
        print
        print "Finished Test: Check Keypair Count"
        print
        return 0


    def test_ui_delete_keypair(self):
        '''
        Goes to Key Pairs LP and deletes the first key pair from top.
        '''
        print
        print "Started Test: Delete Keypair"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_xpath("//table[@id='keys']/tbody/tr/td[2]")
        self.click_element_by_id("more-actions-keys")
        print
        print "Test: Delete Keypair"
        self.click_element_by_link_text("Delete")
        self.click_element_by_id("btn-keys-delete-delete")
        print
        print "Finished Test: Delete Keypair"
        print
        return 0

    def test_ui_delete_keypair_given_name(self, keypair_name):
        print
        print "Started Test: Delete Keypair Given Name"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id(keypair_name)
        self.click_element_by_id("more-actions-keys")
        print
        print "Test: Delete Keypair"
        self.click_element_by_link_text("Delete")
        self.click_element_by_id("btn-keys-delete-delete")
        print
        print "Finished Test: Delete Keypair"
        print
        return 0

    def test_ui_delete_keypair_all(self):
        print
        print "Started Test: Delete Keypair All"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id("keys-check-all")
        self.click_element_by_id("more-actions-keys")
        print
        print "Test: Delete Keypair All"
        self.click_element_by_link_text("Delete")
        self.click_element_by_id("btn-keys-delete-delete")
        print
        print
        print "Finished Test: Delete Keypair All"
        print
        return 0


if __name__ == "__main__":
    unittest.main()



