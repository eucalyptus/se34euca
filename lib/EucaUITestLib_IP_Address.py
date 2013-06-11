from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_IP_Address(EucaUITestLib_Base):

    def test_ui_allocate_two_ip_addresses(self):
	print "Started Test: Allocate Two IP Addresses"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-netsec-eip"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Allocate Two IP Addresses"
            raise
            return 1
        print "Test: Go to the Page IP Address"
        driver.find_element_by_id("dashboard-netsec-eip").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-eips-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Allocate Two IP Addresses"
            raise
            return 1
        driver.find_element_by_id("table-eips-new").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "eip-allocate-count"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Allocate Two IP Addresses"
            raise
            return 1
	print "Test: Allocate Two IP Addresses"
        driver.find_element_by_id("eip-allocate-count").clear()
        driver.find_element_by_id("eip-allocate-count").send_keys("2")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "eip-allocate-btn"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Allocate Two IP Addresses"
            raise
            return 1
	try:
            driver.find_element_by_id("eip-allocate-btn").click()
	except:
	    print "Failed Test: Allocate Two IP Addresses"
            raise
            return 1
	print "Finished: Allocate Two IP Addresses"
	print
	return 0

    def test_ui_release_ip_address(self):
	print "Started Test: Release IP Address"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Release Two IP Addresses"
            raise
            return 1
        print "Test: Go to the Page IP Address"
        driver.find_element_by_css_selector("#dashboard-netsec-eip > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-eips-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Release Two IP Addresses"
            raise
            return 1
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "more-actions-eips"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Release Two IP Addresses"
            raise
            return 1
        driver.find_element_by_id("more-actions-eips").click()
	self.click_element_by_link_text("Release to cloud")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "btn-eips-release-release"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Release Two IP Addresses"
            raise
            return 1
	try:
            driver.find_element_by_id("btn-eips-release-release").click()
	except:
	    print "Failed Test: Release Two IP Addresses"
            raise
            return 1
	print "Finished: Release IP Address" 
	print
	return 0

if __name__ == "__main__":
    unittest.main()



