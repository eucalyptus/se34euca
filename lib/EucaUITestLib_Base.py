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


    def check_if_element_present_by_type(self, element_type, element):

	this_element_type = ""
	if( element_type is "LINK_TEXT" ):
	    this_element_type = By.LINK_TEXT
	elif( element_type is "ID" ):
	    this_element_type = By.ID
	elif( element_type is "CSS_SELECTOR" ):
	    this_element_type = By.CSS_SELECTOR
	elif( element_type is "XPATH" ):
	    this_element_type = By.XPATH

	for i in range(self.retry):
            print "Wait On:: Trial: " + str(i)  + " Element Type: " + element_type + ", Element: " + element
            try:
                if self.is_element_present(this_element_type, element):
		    break
            except:
		pass
            time.sleep(1)

        try:
            self.assertTrue(self.is_element_present(this_element_type, element))
        except AssertionError as e:
	    self.verificationErrors.append(str(e))
	    print "TEST FAILED::: Wait On:: Element Type: " + element_type + ", Element: " + element
	    raise
	    return 1

	print "Found:: Element type: " + element_type + ", Element: " + element
	return 0


    def verify_element_by_link_text(self, element):
	return self.check_if_element_present_by_type("LINK_TEXT", element)

    def verify_element_by_id(self, element):
	return self.check_if_element_present_by_type("ID", element)

    def verify_element_by_css_selector(self, element):
	return self.check_if_element_present_by_type("CSS_SELECTOR", element)

    def verify_element_by_xpath(self, element):
	return self.check_if_element_present_by_type("XPATH", element)


    def click_element_by_link_text(self, link_text):
	if( self.check_if_element_present_by_type("LINK_TEXT", link_text) is not 0 ):
	    return 1
        print "Click: Element Type: LINK_TEXT, Element: "+ link_text
        self.driver.find_element_by_link_text(link_text).click()
	return 0

    def click_element_by_id(self, this_id):
	if( self.check_if_element_present_by_type("ID", this_id) is not 0 ):
	    return 1
        print "Click: Element Type: ID, Element: "+ this_id
        self.driver.find_element_by_id(this_id).click()
	return 0

    def click_element_by_css_selector(self, css_selector):
	if( self.check_if_element_present_by_type("CSS_SELECTOR", css_selector) is not 0 ):
	    return 1
        print "Click: Element Type: CSS_SELECTOR, Element: "+ css_selector
        self.driver.find_element_by_css_selector(css_selector).click()
	return 0

    def click_element_by_xpath(self, xpath):
	if( self.check_if_element_present_by_type("XPATH", xpath) is not 0 ):
	    return 1
        print "Click: Element Type: XPATH, Element: "+ xpath
        self.driver.find_element_by_xpath(xpath).click()
	return 0


    def set_keys_by_element_id(self,element_id, type_keys):

        driver = self.driver
        wait_in_secs=self.wait_in_secs
        print "==============find_el_by_id " +element_id + " and_send_keys " + type_keys + " START================="

        for i in range(wait_in_secs):
            try:
                print "Test: Verifying element present by id: " + element_id
                if self.is_element_present(By.ID, element_id): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id(element_id).clear()
        print "Test: Trying to click element by id: " + element_id + " and send keys " +type_keys
        driver.find_element_by_id(element_id).send_keys(type_keys)
        print "Test: Sent keys " + type_keys
        print "==============find_el_by_id " +element_id + " and_send_keys " + type_keys + " DONE=================="

    def set_keys_by_css(self, element_css, text):

        driver = self.driver
        wait_in_secs=self.wait_in_secs
        print "==============find_el_by_css " +element_css+ " and_send_text " + text + " START================="

        for i in range(wait_in_secs):
            try:
                print "Test: Verifying element present by css: " + element_css
                if self.is_element_present(By.CSS_SELECTOR, element_css): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector (element_css).clear()
        print "Test: Trying to click element by css: " + element_css + " and send keys " +text
        driver.find_element_by_css_selector(element_css).send_keys(text)
        print "Test: Sent keys " + text
        print "==============find_el_by_id " +element_css + " and_send_keys " + text + " DONE=================="


    def set_keys_by_xpath(self, element_xpath, text):
        driver = self.driver
        wait_in_secs=self.wait_in_secs

        for i in range(wait_in_secs):
            try:
                print "Test: Verifying element present by xpath: " + element_xpath
                if self.is_element_present(By.XPATH, element_xpath): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        try: self.assertTrue(self.is_element_present(By.XPATH, element_xpath))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath(element_xpath).clear()
        driver.find_element_by_xpath(element_xpath).send_keys(text)
        print "Test: Typed: "+text+ " in the xpath location " + element_xpath


    def get_value_by_css(self, element_css, what_is_it):
        '''
        element_css is the css path to the element the value of which we are interested in
        what_is_it is a short description of the element for the log; i.e. number of running instances
        saves the value of the desired element into self.save_value

        '''
        driver = self.driver
        wait_in_secs=self.wait_in_secs

        print "==============copy_value_into_var "+ what_is_it+ " by_css " + element_css + " START================="

        for i in range(wait_in_secs):
            try:
                print "Test: Verifying element present by css: " + element_css
                if self.is_element_present(By.CSS_SELECTOR, element_css): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        print "Test: Assert element present by css: " + element_css
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, element_css))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.save_value = driver.find_element_by_css_selector(element_css).text
        while self.save_value == "":
            self.save_value = driver.find_element_by_css_selector(element_css).text
        print "Test: saved value for " + what_is_it + " " + self.save_value

        print "==============copy_value_into_var "+ what_is_it + " by_css " + element_css + " DONE================="


if __name__ == "__main__":
    unittest.main()



