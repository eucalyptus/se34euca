from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Admin_Console(EucaUITestLib_Base):

    def test_ui_create_accounts_and_users_via_admin_console(self):
        print
        print "Started Test: Create Accounts and Users via Admin Console"
        self.click_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div[2]")
        self.verify_element_by_link_text("New account")
        self.set_keys_by_css_selector("input.gwt-TextBox","aaacct")




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