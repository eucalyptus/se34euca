from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_IP_Address(EucaUITestLib_Base):
    def test_ui_allocate_ip_address(self, ip_count):
        print
        print "Started Test: Allocate IP Address: IP_COUNT " + str(ip_count)
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        self.verify_element_by_id("dashboard-netsec-eip")
        print
        print "Test: Go to the Page IP Address"
        self.click_element_by_id("dashboard-netsec-eip")
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
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Verifying that IP Address Count on Dashboard is " + ip_count
        self.verify_text_displayed_by_css("#dashboard-netsec-eip > span", ip_count)
        print
        print "Finished Test: IP Address Count"
        print
        return 0

    def test_ui_release_ip_address(self):
        print
        print "Started Test: Release IP Address"
        self.click_element_by_link_text("Dashboard")
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



