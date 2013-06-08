from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Keypair(EucaUITestLib_Base):

    def test_ui_gotopage_keypairs(self):
	print "Started Test: GotoPage Keypairs"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Keypairs"
	    raise
            return 1
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-netsec-keypair"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Keypairs"
	    raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "dashboard-netsec-keypair"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("dashboard-netsec-keypair").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-keys-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Keypairs"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "table-keys-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Keypairs"
	print
	return 0


    def test_ui_generate_keypair(self):
	print "Started Test: Generate Keypair"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Generate Keypair"
            raise
            return 1
	try:
		print "Test: Go to the Page Keypair"
		driver.find_element_by_id("dashboard-netsec-keypair").click()
		print "Test: Generate New Keypair"
		driver.find_element_by_id("table-keys-new").click()
		driver.find_element_by_id("key-name").clear()
		driver.find_element_by_id("key-name").send_keys("my-sel-gen-key-00")
		# ERROR: Caught exception [ERROR: Unsupported command [typeKeys]]
		driver.find_element_by_id("keys-add-btn").click()
	except:
		print "Failed Test: Generate Keypair"
		raise
		return 1
	print "Finished Test: Generate Keypair"
	print
	return 0


    def test_ui_delete_keypair(self):
	print "Started Test: Delete Keypair"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Keypair"
            raise
            return 1
	try:
		print "Test: Go to the Page Keypair"
        	driver.find_element_by_id("dashboard-netsec-keypair").click()
		print "Test: Delete Keypair"
		driver.find_element_by_xpath("//table[@id='keys']/tbody/tr/td[2]").click()
        	driver.find_element_by_id("more-actions-keys").click()
        	driver.find_element_by_link_text("Delete").click()
        	driver.find_element_by_id("btn-keys-delete-delete").click()
	except:
		print "Failed Test: Delete Keypair"
		raise
		return 1
	print "Finished Test: Delete Keypair"
	print
	return 0

    def test_ui_delete_keypair_all(self):
	print "Started Test: Delete Keypair All"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Keypair All"
            raise
            return 1
	try:
		print "Test: Go to the Page Keypair"
        	driver.find_element_by_id("dashboard-netsec-keypair").click()
		print "Test: Delete Keypair All"
		for i in range(self.retry):
		    try:
			if self.is_element_present(By.ID, "keys-check-all"): break
		    except: pass
		    time.sleep(1)
		else:
		    print "Failed Test: Delete Keypair All"
		    raise
		    return 1
		driver.find_element_by_id("keys-check-all").click()
        	driver.find_element_by_id("more-actions-keys").click()
        	driver.find_element_by_link_text("Delete").click()
        	driver.find_element_by_id("btn-keys-delete-delete").click()
	except:
		print "Failed Test: Delete Keypair All"
		raise
		return 1
	print "Finished Test: Delete Keypair All"
	print
	return 0

if __name__ == "__main__":
    unittest.main()



