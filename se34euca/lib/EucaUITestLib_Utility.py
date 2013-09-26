from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_Utility(EucaUITestLib_Base):

    retry = 10
    sleep_time = 20

    def test_ui_change_password(self, new_password):
        '''
        old password is saved as password_old

        '''

        self.password_old = self.password
        print self.username
        print self.accountname
        print self.password
        self.click_element_by_link_text(self.username + "@" + self.accountname)
        self.click_element_by_link_text("Change password")
        self.set_keys_by_xpath("(//input[@id='current'])[2]", self.password)
        self.set_keys_by_xpath("(//input[@id='newpwd'])[2]", new_password)
        self.set_keys_by_xpath("(//input[@id='confirmpwd'])[2]", new_password)
        time.sleep(1)
        self.click_element_by_id("change-pwd")
        try_again = 0
        while (self.is_element_present(By.LINK_TEXT, "There was a problem with your request")) and try_again < 3:
            print "Try " + `try_again` + " to change password"
            try_again += 1
            self.click_element_by_link_text("Close")
            self.password_old = self.password
            self.click_element_by_link_text(self.username + "@" + self.accountname)
            self.click_element_by_link_text("Change password")
            self.set_keys_by_xpath("(//input[@id='current'])[2]", self.password)
            self.set_keys_by_xpath("(//input[@id='newpwd'])[2]", new_password)
            self.set_keys_by_xpath("(//input[@id='confirmpwd'])[2]", new_password)
            time.sleep(1)
            self.click_element_by_id("change-pwd")

        self.password = new_password
        time.sleep(1)
        print "Test: old pwd: " + self.password_old
        print "Test: new pwd: " + self.password

    def test_ui_clean_up(self):

        print "Started Test: Clean Up"
        print
        print "Check number of Running Instances on Dashboard, terminate if not zero"
        print
        for i in range(self.retry):
            print "Trial: " + str(i)
            self.click_element_by_id("resource-menu-dashboard")
            time.sleep(self.sleep_time)
            if self.driver.find_element_by_css_selector("div.status-readout > span").text != str(0):
                num_running_instances = self.get_text_by_css_selector("div.status-readout > span")
                print "Test: Verified number of Running Instances on dashboard is non-zero: " + num_running_instances
                print
                print "Test: Go to Running Instances Page"
                self.click_element_by_css_selector("div.status-readout > span")
                self.verify_element_by_id("table-instances-new")
                self.click_element_by_id("instances-check-all")
                self.click_element_by_id("more-actions-instances")
                print
                print "Test: Delete All Instances"
                self.click_element_by_link_text("Terminate")
                self.click_element_by_id("btn-instances-terminate-terminate")
                time.sleep(self.sleep_time)
            else:
                print "Test: Instance count on Dashboard is zero"
                break
        print
        print "Check number of Snapshots on Dashboard, terminate if not zero"
        print
        for i in range(self.retry):
            print "Trial: " + str(i)
            self.click_element_by_id("resource-menu-dashboard")
            time.sleep(self.sleep_time)
            if self.driver.find_element_by_css_selector("#dashboard-storage-snapshot > span").text != str(0):
                num_snapshots = self.get_text_by_css_selector("#dashboard-storage-snapshot > span")
                print "Test: Verified number of Snapshots on dashboard is non-zero: " + num_snapshots
                print
                print "Test: Go to Snapshots Landing Page"
                self.click_element_by_css_selector("#dashboard-storage-snapshot > span")
                self.verify_element_by_id("table-snapshots-new")
                self.click_element_by_id("snapshots-check-all")
                self.click_element_by_id("more-actions-snapshots")
                print
                print "Test: Delete All Snapshots"
                self.click_element_by_link_text("Delete")
                self.click_element_by_id("button-dialog-deletesnapshot-delete")
                time.sleep(self.sleep_time)
            else:
                print
                print "Test: Snapshot count on Dashboard is zero"
                break
        print
        print "Check number of Key Pairs on Dashboard, delete if not zero"
        print
        for i in range(self.retry):
            print "Trial: " + str(i)
            self.click_element_by_id("resource-menu-dashboard")
            time.sleep(self.sleep_time)
            if self.driver.find_element_by_css_selector("#dashboard-netsec-keypair > span").text != str(0):
                num_key_pairs = self.get_text_by_css_selector("#dashboard-netsec-keypair > span")
                print "Test: Verified number of Key Pairs on dashboard is non-zero: " + num_key_pairs
                print
                print "Test: Go to Key Pairs Landing Page"
                self.click_element_by_css_selector("#dashboard-netsec-keypair > span")

                self.verify_element_by_id("table-keys-new")
                self.click_element_by_id("keys-check-all")
                self.click_element_by_id("more-actions-keys")
                print
                print "Test: Delete All Key Pairs"
                self.click_element_by_link_text("Delete")
                self.click_element_by_id("btn-keys-delete-delete")
                time.sleep(self.sleep_time)
            else:
                print
                print "Test: Key Pair count on Dashboard is zero"
                break
        print
        print "Check number of Volumes on Dashboard, delete if not zero"
        print
        for i in range(self.retry):
            print "Trial: " + str(i)
            self.click_element_by_id("resource-menu-dashboard")
            time.sleep(self.sleep_time)
            if self.driver.find_element_by_css_selector("#dashboard-storage-volume > span").text != str(0):
                num_volumes = self.get_text_by_css_selector("#dashboard-storage-volume > span")
                print "Test: Verified number of Volumes on dashboard is non-zero: " + num_volumes
                print
                print "Test: Go to Volumes Landing Page"
                print "Click 'Storage' button"
                self.click_element_by_id("resource-menu-storage")
                print "Click 'Volumes' from menu"
                self.click_element_by_id("resource-menuitem-volume")
                print "Filter for available volumes"
                self.click_element_by_css_selector("div.VS-search-inner")
                self.click_element_by_link_text("All Text")
                self.set_keys_by_xpath("//input[@value]","available")
                self.click_element_by_css_selector("div.VS-search-inner")
                #self.click_element_by_id("volumes-wrapper")
                if self.driver.find_element_by_css_selector("div.table-row-status.status-available"):
                    self.verify_element_by_id("table-volumes-new")
                    self.click_element_by_id("volumes-check-all")
                    self.click_element_by_id("more-actions-volumes")
                    print
                    print "Test: Delete All Volumes"
                    self.click_element_by_link_text("Delete")
                    self.click_element_by_id("button-dialog-deletevolume-delete")
                    time.sleep(self.sleep_time)
                    time.sleep(self.sleep_time)
                    time.sleep(self.sleep_time)
                else:
                    print
                    print "Could not find any available volumes"
                    print
            else:
                print
                print "Test: Volume count on Dashboard is zero"
                break
        print
        print "Check number of Security Groups on Dashboard, delete if not one"
        print
        for i in range(self.retry):
            print "Trial: " + str(i)
            self.click_element_by_id("resource-menu-dashboard")
            time.sleep(self.sleep_time)
            if self.driver.find_element_by_css_selector("#dashboard-netsec-sgroup > span").text != str(1):
                num_security_groups = self.get_text_by_css_selector("#dashboard-netsec-sgroup > span")
                print "Test: Verified number of Security Groups on dashboard is not one: " + num_security_groups
                print
                print "Test: Go to Security Groups Landing Page"
                self.click_element_by_css_selector("#dashboard-netsec-sgroup > span")
                self.verify_element_by_id("table-sgroups-new")
                self.click_element_by_id("sgroups-check-all")
                self.click_element_by_id("more-actions-sgroups")
                print
                print "Test: Delete All Security Groups"
                self.click_element_by_link_text("Delete")
                self.click_element_by_id("btn-sgroups-delete-delete")
                time.sleep(self.sleep_time)
            else:
                print
                print "Test: Security Group count on Dashboard is one"
                print
                break
        print
        print "Check number of IP Addresses on Dashboard, release to cloud if not zero"
        print
        for i in range(self.retry):
            print "Trial: " + str(i)
            self.click_element_by_id("resource-menu-dashboard")
            time.sleep(self.sleep_time)
            if self.driver.find_element_by_css_selector("#dashboard-netsec-eip > span").text != str(1):
                num_ip_addresses = self.get_text_by_css_selector("#dashboard-netsec-eip > span")
                print "Test: Verified number of IP Addresses on dashboard is non-zero: " + num_ip_addresses
                print
                print "Test: Go to IP Addresses Landing Page"
                self.click_element_by_css_selector("#dashboard-netsec-eip > span")
                self.verify_element_by_id("table-eips-new")
                self.click_element_by_id("eips-check-all")
                self.click_element_by_id("more-actions-eips")
                print
                print "Test: Delete All IP Addresses"
                self.click_element_by_link_text("Release to cloud")
                self.click_element_by_id("btn-eips-release-release")
                time.sleep(self.sleep_time)
            else:
                print
                print "Test: Security Group count on Dashboard is one"
                break
        print
        print "Finished Test: Clean Up"



if __name__ == "__main__":
    unittest.main()
