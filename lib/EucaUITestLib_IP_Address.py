from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_IP_Address(EucaUITestLib_Base):

    def test_ui_allocate_two_ip_addresses(self):
	print
	print "Started Test: Allocate Two IP Addresses"
	self.verify_element_by_id("dashboard-netsec-eip")
        print
	print "Test: Go to the Page IP Address"
	self.click_element_by_id("dashboard-netsec-eip")
        self.click_element_by_id("table-eips-new")
	self.verify_element_by_id("eip-allocate-count")
	print
	print "Test: Allocate Two IP Addresses"
	try:
            self.driver.find_element_by_id("eip-allocate-count").clear()
            self.driver.find_element_by_id("eip-allocate-count").send_keys("2")
	except:
            print "Failed Test: Allocate Two IP Addresses"
            raise
            return 1
	self.click_element_by_id("eip-allocate-btn")
	print
	print "Finished: Allocate Two IP Addresses"
	print
	return 0

    def test_ui_release_ip_address(self):
	print
	print "Started Test: Release IP Address"
	self.verify_element_by_link_text("Launch new instance")
        print
	print "Test: Go to the Page IP Address"
	self.click_element_by_css_selector("#dashboard-netsec-eip > span")
        self.click_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]")
        self.click_element_by_id("more-actions-eips")
	self.click_element_by_link_text("Release to cloud")
        self.click_element_by_id("btn-eips-release-release")
	print
	print "Finished: Release IP Address" 
	print
	return 0

if __name__ == "__main__":
    unittest.main()



