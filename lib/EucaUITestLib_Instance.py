from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Instance(EucaUITestLib_Base):

    def test_ui_gotopage_running(self):
	print "Started Test: GotoPage Running"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Running"
            raise
	    return 1
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "div.status-readout"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Running"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.status-readout"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.status-readout").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-instances-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Running"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "table-instances-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Running"
	print
	return 0

    def test_ui_launch_instance_basic(self):
	print "Started Test: Launch Instance Basic"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: Could Not Locate LINK_TEXT -> Launch Instance Basic"
            raise
            return 1
	print "Click: LINK_TEXT -> Launch new instance"
	driver.find_element_by_link_text("Launch new instance").click()
	print "Wait: CSS_SELECTOR -> div.image-name"
	for i in range(self.retry):
		try:
		    if self.is_element_present(By.CSS_SELECTOR, "div.image-name"): break
		except: pass
		time.sleep(1)
	else:
		print "Failed Test: Could Not Locate CSS_SELECTOR -> div.image-name"
		raise
		return 1
	print "Click: CSS_SELECTOR -> div.image-name"
	driver.find_element_by_css_selector("div.image-name").click()
	print "Wait: ID -> nextButton"
	for i in range(self.retry):
		try:
		    if self.is_element_present(By.ID, "nextButton"): break
		except: pass
		time.sleep(1)
	else:   
		print "Failed Test: Could Not Locate ID -> nextButton"
		raise
		return 1
	print "Click: ID -> nextButton" 
	driver.find_element_by_id("nextButton").click()
	print "Wait: ID -> launch-instance-type-num-instance"
	for i in range(self.retry):
		try:
		    if self.is_element_present(By.ID, "launch-instance-type-num-instance"): break
		except: pass
		time.sleep(1)
	else:   
		print "Failed Test: Could Not Locate ID -> launch-instance-type-num-instance"
		raise
		return 1
	print "Click: ID -> nextButton"
	driver.find_element_by_id("nextButton").click()
	print "Wait: ID -> launch-wizard-security-keypair-selector"
	for i in range(self.retry):
		try:
		    if self.is_element_present(By.ID, "launch-wizard-security-keypair-selector"): break
		except: pass
		time.sleep(1)
	else:   
		print "Failed Test: Could Not Located ID -> launch-wizard-security-keypair-selector"
		raise
		return 1
	print "Select: ID -> launch-wizard-security-keypair-selector, TEXT -> None (advanced option)"
	Select(driver.find_element_by_id("launch-wizard-security-keypair-selector")).select_by_visible_text("None (advanced option)")
	print "Click: ID -> finishButton"
	try:
		driver.find_element_by_id("finishButton").click()
	except:
		print "Failed Test: Could Not Locate ID -> finishButton"
		raise
		return 1
	print "Finished Test: Launch Instance Basic"
	print 
	return 0 

    def test_ui_terminate_instance_basic(self):
	print "Started Test: Terminate Instance Basic"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Terminate Instance Basic"
            raise
            return 1
	try:
		print "Test: Go to the Page Running Instances"
		driver.find_element_by_css_selector("div.status-readout").click()
		print "Test: Terminate an Instance"
        	driver.find_element_by_xpath("//table[@id='instances']/tbody/tr/td[5]").click()
        	driver.find_element_by_id("more-actions-instances").click()
        	driver.find_element_by_link_text("Terminate").click()
        	driver.find_element_by_id("btn-instances-terminate-terminate").click()
	except:
		print "Failed Test: Terminate Instance Basic"
		raise
		return 1
	print "Finished Test: Terminate Instance Basic"
	print
	return 0

    def test_ui_terminate_instance_all(self):
	print "Started Test: Terminate Instance All"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Terminate Instance All"
            raise
            return 1
	try:
		print "Test: Go to the Page Running Instances"
		driver.find_element_by_css_selector("div.status-readout").click()
		for i in range(self.retry):
		    try:
			if self.is_element_present(By.ID, "instances-check-all"): break
		    except: pass
		    time.sleep(1)
		else:
		    print "Failed Test: Terminate Instance All"
		    raise
		    return 1
		print "Test: Terminate Instance All"
        	driver.find_element_by_id("instances-check-all").click()
        	driver.find_element_by_id("more-actions-instances").click()
        	driver.find_element_by_link_text("Terminate").click()
        	driver.find_element_by_id("btn-instances-terminate-terminate").click()
	except:
		print "Failed Test: Terminate Instance All"
		raise
		return 1
	print "Finished Test: Terminate Instance All"
	print
	return 0


if __name__ == "__main__":
    unittest.main()



