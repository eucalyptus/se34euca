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
	self.verify_element_by_link_text("Launch new instance")
	self.click_element_by_id("dashboard-netsec-keypair")
        print
        print "Test: Clicked the GoToPage Button"
	self.click_element_by_id("table-keys-new")
	print
	print "Test: Generate New Keypair"
	self.set_keys_by_id("key-name", "my-sel-gen-key-00")
	self.click_element_by_id("keys-add-btn")
	print
	print "Finished Test: Generate Keypair"
	print
	return 0


    def test_ui_delete_keypair(self):
	print
        print "Started Test: Delete Keypair"
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



