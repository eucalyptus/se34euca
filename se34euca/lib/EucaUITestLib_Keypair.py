from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Keypair(EucaUITestLib_Base):

    def test_ui_gotopage_keypairs(self):
        print
        print "Started Test: GotoPage Keypairs"
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
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id("table-keys-new")
        print
        print "Test: Generate New Keypair"
        self.set_keys_by_id("key-name", "my-sel-gen-key-00")
        self.click_element_by_id("keys-add-btn")
        print"Test: Verification"
        #Verifying on Key Pairs landing page by key pair name that key pair is present
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        self.verify_element_by_css_selector('span[title="my-sel-gen-key-00"]')
        print
        print
        print "Finished Test: Generate Keypair"
        print
        return 0

    def test_ui_generate_keypair_name_demokey(self):
        print
        print "Started Test: Generate Keypair"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id("table-keys-new")
        print
        print "Test: Generate New Keypair"
        self.set_keys_by_id("key-name", "demokey")
        self.click_element_by_id("keys-add-btn")
        print"Test: Verification"
        #Verifying on Key Pairs landing page by key pair name that key pair is present
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("Key Pairs")
        self.verify_element_by_css_selector('span[title="demokey"]')
        print
        print
        print "Finished Test: Generate Keypair"
        print
        return 0

    def test_ui_import_keypair(self):
        print
        print "Started Test: Import Keypair"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
        self.click_element_by_id("table-keys-extra")
        print
        print "Test: Import Keypair"
        self.set_keys_by_id(this_id="key-import-contents",keys="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDI1x6tEjkBQCCP0ssF69vAgP2xg+N9ScoTrqRqyl5w4qEgsV/AppfHHYRKYr0N/tTyG4/z1XGNrB2SaslnRpgEOsvMZldlOnqsUujL2fgoEg+/gB92+1JhZgTjU8nL5j5BFkVTh93nSHtXHdzYl7SjlXrv26ZbyuDwJmI+s6bJQk5noJ4Q4g7N/0y9pHRvezyhgxkyX7PQoA9WJm8SqlakyhMYa0j/baMhb/ehSI0VvwNodmcaWaS6Z2F4rZS4C2DmCUDXYy/1+0tiRTjHjlPbqRKCVKam8ImWytlZD0zbdV/tpADxDpnhW2cPVpXcjy4sRzUCc8AZW+OE3LQxXild alicehubenko@Alices-MacBook-Pro.local")
        self.set_keys_by_xpath(xpath="(//input[@id='key-name'])[2]",keys="import-key")
        self.click_element_by_id("keys-add-btn")
        print
        print"Test: Verification"
        #Verifying on Key Pairs landing page by key pair name that key pair is present
        self.click_element_by_link_text(link_text="Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.click_element_by_id("dashboard-netsec-keypair")
        self.verify_element_by_css_selector('span[title="import-key"]')
        print
        print "Finished Test: Import Keypair"
        print
        return 0

    def test_ui_check_keypair_count(self, keys_count):
        print
        print "Started Test: Check Keypair Count"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Verifying that Keypair Count on Dashboard is "+keys_count
        self.verify_text_displayed_by_css("#dashboard-netsec-keypair > span",keys_count)
        print
        print "Finished Test: Check Keypair Count"
        print
        return 0



    def test_ui_delete_keypair(self):
        print
        print "Started Test: Delete Keypair"
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

    def test_ui_delete_keypair_all(self):
        print
        print "Started Test: Delete Keypair All"
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



