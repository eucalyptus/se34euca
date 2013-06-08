from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EucaUITestLib_Base(unittest.TestCase):

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

    def setSeleniumWebDriver(self, driver):
	self.driver = driver

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



