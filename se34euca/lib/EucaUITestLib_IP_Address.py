from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_IP_Address(EucaUITestLib_Base):

    def test_ui_allocate_ip_address(self, ip_count):
        print
        print "Started Test: Allocate IP Address: IP_COUNT " + str(ip_count)
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page IP Address"
        self.click_element_by_id("dashboard-netsec-eip")
        time.sleep(3)
        self.click_element_by_id("table-eips-new")
        self.verify_element_by_id("eip-allocate-count")
        print
        print "Test: Allocate IP Address"
        self.set_keys_by_id("eip-allocate-count", str(ip_count))
        self.click_element_by_id("eip-allocate-btn")
        print
        print "Finished: Allocate IP Addresses"
        print
        return 0

    def test_ui_check_ip_address_count(self, ip_count):
        print
        print "Started Test: Check IP Address Count"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        time.sleep(3)
        print "Verifying that IP Address Count on Dashboard is " + ip_count
        self.verify_text_displayed_by_css("#dashboard-netsec-eip > span", ip_count)
        print
        print "Finished Test: IP Address Count"
        print
        return 0

    def test_ui_release_ip_address_all(self):
        print
        print "Started Test: Release IP Address"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page IP Address"
        self.click_element_by_css_selector("#dashboard-netsec-eip > span")
        time.sleep(3)
        self.click_element_by_id("eips-check-all")
        self.click_element_by_id("more-actions-eips")
        self.click_element_by_link_text("Release to cloud")
        self.click_element_by_id("btn-eips-release-release")
        print
        print "Finished: Release IP Address"
        print
        return 0

    def test_ui_get_available_ip_address(self):
        '''
        Returns an available IP address at random
        '''
        print
        print "Started Test: Get Available IP Address"
        print
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("IP Addresses")
        time.sleep(3)
        self.click_element_by_css_selector("div.VS-search-inner")
        self.click_element_by_link_text("Assignment")
        self.click_element_by_link_text("Unassigned")
        time.sleep(3)
        available_ip = self.get_text_by_xpath("//table[@id='eips']/tbody/tr/td[2]")
        print
        print "Finished Test: Get Available IP Address. Returning IP: " + available_ip
        print
        return available_ip


if __name__ == "__main__":
    unittest.main()



