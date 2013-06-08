from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EucaUITester(unittest.TestCase):

    selenium_server_ip = "localhost"
    selenium_server_port = "4444"
    ui_ip = "localhost"
    port = "8888"
    accountname = "eucalyptus"
    username = "admin"
    password = "password"

    retry = 5

    def NoOp(self):
	return 0

    def setSeleniumServerInfo(self, ip, port):
	self.selenium_server_ip = ip
	self.selenium_server_port = port
	print "SELENIUM SERVER IP: " + ip
	print "SELENIUM SERVER PORT: " + port
	print

    def setUIInfo(self, ip, port):
	self.ui_ip = ip
	self.port = port
	print "UI IP: " + ip
	print "PORT: " + port
	print

    def setUserInfo(self, accountname, username, password):
	self.accountname = accountname
	self.username = username
	self.password = password
	print "ACCOUNTNAME: " + accountname
	print "USERNAME: " + username
	print "PASSWORD: " + password
	print

    def setUp(self):
	print "=== setUp ==="
	this_ui = "https://" + self.ui_ip + ":" + self.port
	this_selenium_server_url = "http://" + self.selenium_server_ip + ":" + self.selenium_server_port + "/wd/hub"
	print "Selenium Server URL: " + this_selenium_server_url
	print "Eucalyptus UI URL: " + this_ui
	if self.selenium_server_ip is not "localhost":
		self.driver = webdriver.Remote(this_selenium_server_url, webdriver.DesiredCapabilities.FIREFOX)
        else:
		self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = this_ui
        self.verificationErrors = []
	print "Started Selenium Test Targeted at : " + self.base_url
	print

    def tearDown(self):
	print "=== tearDown ==="
	self.driver.quit()
        self.assertEqual([], self.verificationErrors)
	print "Finished Selenium Test Targeted at : " + self.base_url
	print    

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True


    def test_ui_login(self):
	print "Started Test: Login"	
        driver = self.driver
        driver.get(self.base_url + "/")
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "login"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Login"
	    raise
	    return 1
	print "Test: Received the Login Page"
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys(self.accountname)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(self.password)
        driver.find_element_by_name("login").click()
	print "Test: Typed the User Info and Clicked the Login Button"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Login"
	    raise
	    return 1
	print "Finished Test: Login"
	print
	return 0

    def test_ui_logout(self):
	print "Started Test: Logout"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Logout"
	    raise
	    return 1
	driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Logout"
	    raise
	    return 1
	this_link = self.username + "@" + self.accountname
	for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, this_link): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Logout"
	    raise
	    return 1
	print "Test: Clicking User Account Menu " + this_link
        driver.find_element_by_link_text(this_link).click()
	print "Test: Clicked User Account Menu " + this_link
	for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Log out"): break
            except: pass
	    time.sleep(1)
        else:
	    print "Failed Test: Logout"
            raise
            return 1
	print "Test: Clicking Log out"
	driver.find_element_by_link_text("Log out").click()
	print "Test: Clicked the Logout Button"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "login"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Logout"
            raise
            return 1
	print "Finished Test: Logout"
	print
	return 0

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

    def test_ui_gotopage_security_groups(self):
	print "Started Test: GotoPage Security Groups"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Secutiry Groups"
            raise
	    return 1
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-netsec-sgroup"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Secutiry Groups"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "dashboard-netsec-sgroup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("dashboard-netsec-sgroup").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-sgroups-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Secutiry Groups"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "table-sgroups-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Security Groups"
	print
	return 0

    def test_ui_gotopage_volumes(self):
	print "Started Test: GotoPage Volumes"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Volumes"
            raise
	    return 1
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Volumes"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "dashboard-storage-volume"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("dashboard-storage-volume").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Volumes"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "table-volumes-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Volumes"
	print 
	return 0

    def test_ui_gotopage_images(self):
	print "Started Test: GotoPage Images"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Images"
            raise
	    return 1
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Images"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Images"
            raise
	    return 1
        driver.find_element_by_link_text("Images").click()
	print "Test: Clicked the GotoPage Images"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "More actions"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Images"
            raise
	    return 1
	try:
	    driver.find_element_by_link_text("More actions").click()
	except:
	    print "Failed Test: GotoPage Images"
	    return 1
	print "Finished Test: GotoPage Images"
	print 
	return 0

    def test_ui_gotopage_dashboard(self):
	print "Started Test: GotoPage Dashboard"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Dashboard"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Dashboard"
            raise
	    return 1
	driver.find_element_by_link_text("Dashboard").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Dashboard"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Launch new instance"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Dashboard"
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

    def test_ui_create_volume(self):
	print "Started Test: Create Volume"
        driver = self.driver
	print "Test: Go to the Page Volume"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Volume"
            raise
            return 1
        driver.find_element_by_id("dashboard-storage-volume").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Volume"
            raise
            return 1
	print "Test: Create New Volume"
        driver.find_element_by_id("table-volumes-new").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "volume-size"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create New Volume"
            raise
            return 1
	try:
            driver.find_element_by_id("volume-size").clear()
            driver.find_element_by_id("volume-size").send_keys("2")
            ##driver.find_element_by_id("volumes-add-btn").click()
            driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Create New Volume"
            raise
            return 1
	print "Finished: Create New Volume"
	print
	return 0

    def test_ui_delete_volume(self):
	print "Started Test: Delete Volume"
	driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	print "Test: Go to the Page Volume"
	driver.find_element_by_id("dashboard-storage-volume").click()
	driver.find_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.ID, "more-actions-volumes"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	print "Test: Delete Volume"
	driver.find_element_by_id("more-actions-volumes").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.LINK_TEXT, "Delete"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	driver.find_element_by_link_text("Delete").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.ID, "btn-volumes-delete-delete"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	try:
	    driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	print "Finished: Delete Volume"
	print
	return 0

    def test_ui_delete_volume_all(self):
	print "Started Test: Delete Volume All"
	driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	print "Test: Go to the Page Volume"
	driver.find_element_by_id("dashboard-storage-volume").click()
	for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "volumes-check-all"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: Delete Volume All"
            raise
            return 1
	driver.find_element_by_id("volumes-check-all").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.ID, "more-actions-volumes"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	print "Test: Delete Volume"
	driver.find_element_by_id("more-actions-volumes").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.LINK_TEXT, "Delete"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	driver.find_element_by_link_text("Delete").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.ID, "btn-volumes-delete-delete"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	try:
	    driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	print "Finished: Delete Volume All"
	print
	return 0

    def test_ui_create_snapshot_from_volume(self):
	print "Started Test: Create Snapshot From Volume"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
	print "Test: Go to the Page Volume"
        driver.find_element_by_css_selector("#dashboard-storage-volume > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
        driver.find_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "more-actions-volumes"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
	print "Test: Create Snapshot From Volume"
        driver.find_element_by_id("more-actions-volumes").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Create snapshot from volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
        driver.find_element_by_link_text("Create snapshot from volume").click()
	try:
            driver.find_element_by_id("snapshot-create-description").clear()
            driver.find_element_by_id("snapshot-create-description").send_keys("snapshot by selenium script")
            driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
	print "Finished: Create Snapshot From Volume"   
	print
	return 0

    def test_ui_delete_snapshot(self):
	print "Started Test: Delete Snapshot"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
	print "Test: Go to the Page Snapshot"
        driver.find_element_by_css_selector("#dashboard-storage-snapshot > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-snapshots-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "more-actions-snapshots"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
        driver.find_element_by_id("more-actions-snapshots").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
	print "Test: Delete Snapshot"
        driver.find_element_by_link_text("Delete").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "btn-volumes-delete-delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
	try:
            driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
	print "Finished: Delete Snapshot" 
	print
	return 0

    def test_ui_create_volume_from_snapshot(self):
	print "Started Test: Create Volume From Snapshot"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Volume From Snapshot"
            raise
            return 1
	print "Test: Go to the Page Snapshot"
        driver.find_element_by_css_selector("#dashboard-storage-snapshot > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-snapshots-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Volume From Snapshot"
            raise
            return 1
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "more-actions-snapshots"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Volume From Snapshot"
            raise
            return 1
	print "Test: Create Volume From Snapshot"
        driver.find_element_by_id("more-actions-snapshots").click()
        driver.find_element_by_link_text("Create volume from snapshot").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "btn-volumes-delete-delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Volume From Snapshot"
            raise
            return 1
	try:
            driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Create Volume From Snapshot"
            raise
            return 1
	print "Finished: Create Volume From Snapshot"
	print
	return 0

    def test_ui_create_security_group(self):
	print "Started Test: Create Security Group"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Test: Go to the Page Security Group"
        driver.find_element_by_css_selector("#dashboard-netsec-sgroup > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-sgroups-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
        driver.find_element_by_id("table-sgroups-new").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-name"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Test: Create Security Group"
        driver.find_element_by_id("sgroup-name").clear()
        driver.find_element_by_id("sgroup-name").send_keys("mywebservice")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-description"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
        driver.find_element_by_id("sgroup-description").clear()
        driver.find_element_by_id("sgroup-description").send_keys("rules for my webservice. Generated by Selenium")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-template"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Click: LINK_TEXT -> Rules"
	driver.find_element_by_link_text("Rules").click()
	for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-template"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: Create Security Group"
            raise
            return 1
	print "Select: ID -> sgroup-templete, TEXT -> SSH (TCP port 22, for terminal access)"
        Select(driver.find_element_by_id("sgroup-template")).select_by_visible_text("SSH (TCP port 22, for terminal access)")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "allow-ip"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
        driver.find_element_by_id("allow-ip").clear()
        driver.find_element_by_id("allow-ip").send_keys("0.0.0.0/0")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-add-rule"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Click: ID -> sgroup-add-rule"
        driver.find_element_by_id("sgroup-add-rule").click()
	for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-rule-number-0"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: Create Security Group"
            raise
            return 1
	print "Rule 0: " + driver.find_element_by_css_selector("ul.sg-rules-list > li").text

        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-template"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Select: ID -> sgroup-templete, TEXT -> HTTP (TCP port 80, for web servers)"
        Select(driver.find_element_by_id("sgroup-template")).select_by_visible_text("HTTP (TCP port 80, for web servers)")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "allow-ip"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
        driver.find_element_by_id("allow-ip").clear()
        driver.find_element_by_id("allow-ip").send_keys("0.0.0.0/0")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-add-rule"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Click: ID -> sgroup-add-rule"
        driver.find_element_by_id("sgroup-add-rule").click()
	for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-rule-number-1"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: Create Security Group"
            raise
            return 1
	print "Rule 1: " + driver.find_element_by_xpath("//div[@id='sgroup-rules-list']/ul/li[2]").text

        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-template"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Select: ID -> sgroup-templete, TEXT -> Custom ICMP"
        Select(driver.find_element_by_id("sgroup-template")).select_by_visible_text("Custom ICMP")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-type"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Select: ID -> sgroup-type. TEXT -> All"
        Select(driver.find_element_by_id("sgroup-type")).select_by_visible_text("All")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "allow-ip"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
        driver.find_element_by_id("allow-ip").clear()
        driver.find_element_by_id("allow-ip").send_keys("0.0.0.0/0")
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-add-rule"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Click: ID -> sgroup-add-rule"
        driver.find_element_by_id("sgroup-add-rule").click()
	for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-rule-number-2"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: Create Security Group"
            raise
            return 1
	print "Rule 2: " + driver.find_element_by_xpath("//div[@id='sgroup-rules-list']/ul/li[3]").text

        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroup-add-btn"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Click: ID -> sgroup-add-btn"
	try:
            driver.find_element_by_id("sgroup-add-btn").click()
	except:
	    print "Failed Test: Create Security Group"
            raise
            return 1
	print "Finished: Create Security Group"
	print
	return 0

    def test_ui_delete_security_group(self):
	print "Started Test: Delete Security Group"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group"
            raise
            return 1
	print "Test: Go to the Page Security Group"
        driver.find_element_by_css_selector("#dashboard-netsec-sgroup > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-sgroups-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group"
            raise
            return 1
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "more-actions-sgroups"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group"
            raise
            return 1
        driver.find_element_by_id("more-actions-sgroups").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group"
            raise
            return 1
	print "Test: Delete Security Group"
        driver.find_element_by_link_text("Delete").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "btn-sgroups-delete-delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group"
            raise
            return 1
	try:
            driver.find_element_by_id("btn-sgroups-delete-delete").click()
	except:
	    print "Failed Test: Delete Security Group"
            raise
            return 1
	print "Finished: Delete Security Group"
	print
	return 0

    def test_ui_delete_security_group_all(self):
	print "Started Test: Delete Security Group All"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group All"
            raise
            return 1
	print "Test: Go to the Page Security Group"
        driver.find_element_by_css_selector("#dashboard-netsec-sgroup > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "sgroups-check-all"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group All"
            raise
            return 1
        driver.find_element_by_id("sgroups-check-all").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "more-actions-sgroups"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group All"
            raise
            return 1
        driver.find_element_by_id("more-actions-sgroups").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group All"
            raise
            return 1
	print "Test: Delete Security Group All"
        driver.find_element_by_link_text("Delete").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "btn-sgroups-delete-delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Security Group All"
            raise
            return 1
	try:
            driver.find_element_by_id("btn-sgroups-delete-delete").click()
	except:
	    print "Failed Test: Delete Security Group All"
            raise
            return 1
	print "Finished: Delete Security Group All"
	print
	return 0

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
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Release to cloud"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Release Two IP Addresses"
            raise
            return 1
	print "Test: Release IP Address"
        driver.find_element_by_link_text("Release to cloud").click()
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

    def test_ui_view_page_get_dashboard_source(self):
	print "Started Test: View Page Get Dashboard Source"
	print
        driver = self.driver
	for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: GotoPage Dashboard Source"
	    raise
            return 1
        driver.find_element_by_id("euca-logo").click()
        print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: GotoPage Dashboard Source"
            raise
	    return 1
	time.sleep(3)
	try:
	    running_instances = driver.find_element_by_css_selector("div.status-readout")
	    running_instances_text = running_instances.text
	    print "[DASHBOARD] Running Instances: " + running_instances_text
	    stopped_instances = driver.find_element_by_id("dashboard-instance-stopped")
	    stopped_instances_text = stopped_instances.text
	    print "[DASHBOARD] Stopped Instances: " + stopped_instances_text
	    volumes = driver.find_element_by_id("dashboard-storage-volume")
	    volumes_text = volumes.text
	    print "[DASHBOARD] Volumes: " + volumes_text
	    snapshots = driver.find_element_by_id("dashboard-storage-snapshot")
	    snapshots_text = snapshots.text
	    print "[DASHBOARD] Snapshots: " + snapshots_text
	    sgroup = driver.find_element_by_id("dashboard-netsec-sgroup")
	    sgroup_text = sgroup.text
	    print "[DASHBOARD] Security Groups: " + sgroup_text
	    keypairs = driver.find_element_by_id("dashboard-netsec-keypair")
	    keypairs_text = keypairs.text
	    print "[DASHBOARD] Keypairs: " + keypairs_text
	    eip = driver.find_element_by_id("dashboard-netsec-eip")
	    eip_text = eip.text
	    print "[DASHBOARD] IP Addresses: " + eip_text
	    print
	except:
	    print "Failed Test: GotoPage Dashboard Source"
            raise
            return 1
	print "Finished Test: View Page Get Dashboard Source"
	print
	return 0

if __name__ == "__main__":
    unittest.main()



