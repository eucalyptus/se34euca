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
	return 0

    def setSeleniumServerInfo(self, ip, port):
	self.selenium_server_ip = ip
	self.selenium_server_port = port
	print "SELENIUM SERVER IP: " + ip
	print "SELENIUM SERVER PORT: " + port
	print
	return 0

    def setUIInfo(self, ip, port):
	self.ui_ip = ip
	self.port = port
	print "EUCALYPTUS CONSOLE PROXY IP: " + ip
	print "EUCALYPTUS CONSOLE PROXY PORT: " + port
	print
	return 0

    def setUserInfo(self, accountname, username, password):
	self.accountname = accountname
	self.username = username
	self.password = password
	print "ACCOUNTNAME: " + accountname
	print "USERNAME: " + username
	print "PASSWORD: " + password
	print
	return 0

    def setUp(self):
	print
	print "=== setUp ==="
	this_ui = "https://" + self.ui_ip + ":" + self.port
	this_selenium_server_url = "http://" + self.selenium_server_ip + ":" + self.selenium_server_port + "/wd/hub"
	print "SELENIUM SERVER URL: " + this_selenium_server_url
	print "EUCALYPTUS UI PROXY URL: " + this_ui
	if self.selenium_server_ip is not "localhost":
		self.driver = webdriver.Remote(this_selenium_server_url, webdriver.DesiredCapabilities.FIREFOX)
        else:
		self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = this_ui
        self.verificationErrors = []
	print
	print "Started Selenium Test Targeted at : " + self.base_url
	print
	return 0

    def tearDown(self):
	print
	print "=== tearDown ==="
	self.driver.quit()
        self.assertEqual([], self.verificationErrors)
	print
	print "Finished Selenium Test Targeted at : " + self.base_url
	print
	return 0 

    def is_element_present(self, how, what):
        try:
	    self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
	    return False
        return True


    def test_ui_login(self):
	print
	print "Started Test: Login"	
        self.driver.get(self.base_url + "/")
	print
	print "Test: Received the Page Title -> " + self.driver.title
	self.verify_element_by_id("login")
	print
	print "Test: Received the Login Page"
        self.driver.find_element_by_id("account").clear()
        self.driver.find_element_by_id("account").send_keys(self.accountname)
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.username)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(self.password)
	print
	print "Test: Typed the User Info and Clicked the Login Button"
	self.click_element_by_name("login")
	self.verify_element_by_link_text("Launch new instance")
	print
	print "Finished Test: Login"
	print
	return 0

    def test_ui_logout(self):
	print
	print "Started Test: Logout"
	self.click_element_by_id("euca-logo")
	print
	print "Test: Received the Page Title -> " + self.driver.title
	self.verify_element_by_link_text("Launch new instance")
	this_link = self.username + "@" + self.accountname
	print "Test: Clicked User Account Menu " + this_link
	self.click_element_by_link_text(this_link)
	print "Test: Clicked the Logout Button"
	self.click_element_by_link_text("Log out")
        self.verify_element_by_id("login")
	print
	print "Finished Test: Logout"
	print
	return 0


    def test_ui_gotopage_dashboard(self):
	print
	print "Started Test: GotoPage Dashboard"
	self.click_element_by_link_text("Dashboard")
	print
	print "Test: Received the Page Title -> " + self.driver.title
	self.verify_element_by_link_text("Launch new instance")
	print
	print "Finished Test: GotoPage Dashboard"
	print
	return 0


    def test_ui_view_page_get_dashboard_source(self):
	print
	print "Started Test: View Page Get Dashboard Source"
	print
	self.click_element_by_id("euca-logo")
        print
	print "Test: Received the Page Title -> " + self.driver.title
	self.verify_element_by_link_text("Launch new instance")
	time.sleep(3)
	try:
	    running_instances = self.driver.find_element_by_css_selector("div.status-readout")
	    print "[DASHBOARD] Running Instances: " + running_instances.text
	    stopped_instances = self.driver.find_element_by_id("dashboard-instance-stopped")
	    print "[DASHBOARD] Stopped Instances: " + stopped_instances.text
	    volumes = self.driver.find_element_by_id("dashboard-storage-volume")
	    print "[DASHBOARD] Volumes: " + volumes.text
	    snapshots = self.driver.find_element_by_id("dashboard-storage-snapshot")
	    print "[DASHBOARD] Snapshots: " + snapshots.text
	    sgroup = self.driver.find_element_by_id("dashboard-netsec-sgroup")
	    print "[DASHBOARD] Security Groups: " + sgroup.text
	    keypairs = self.driver.find_element_by_id("dashboard-netsec-keypair")
	    print "[DASHBOARD] Keypairs: " + keypairs.text
	    eip = self.driver.find_element_by_id("dashboard-netsec-eip")
	    print "[DASHBOARD] IP Addresses: " + eip.text
	    print
	except:
	    print "Failed Test: GotoPage Dashboard Source"
            raise
            return 1
	print
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
	elif( element_type is "NAME" ):
	    this_element_type = By.NAME

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

    # VERIFY CALLS
    def verify_element_by_link_text(self, element):
	return self.check_if_element_present_by_type("LINK_TEXT", element)

    def verify_element_by_id(self, element):
	return self.check_if_element_present_by_type("ID", element)

    def verify_element_by_css_selector(self, element):
	return self.check_if_element_present_by_type("CSS_SELECTOR", element)

    def verify_element_by_xpath(self, element):
	return self.check_if_element_present_by_type("XPATH", element)
    
    def verify_element_by_name(self, element):
	return self.check_if_element_present_by_type("NAME", element)

    # CLICK CALLS
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
    
    def click_element_by_name(self, name):
	if( self.check_if_element_present_by_type("NAME", name) is not 0 ):
	    return 1
        print "Click: Element Type: NAME, Element: "+ name
        self.driver.find_element_by_name(name).click()
	return 0

    # SET KEYS CALLS
    def set_keys_by_link_text(self, link_text, keys):
	if( self.check_if_element_present_by_type("LINK_TEXT", link_text) is not 0 ):
            return 1
        print "Set: Element Type: LINK_TEXT, Element: "+ link_text + ", Keys: " + keys
	self.driver.find_element_by_link_text(link_text).clear()
	self.driver.find_element_by_link_text(link_text).send_keys(keys)
	return 0

    def set_keys_by_id(self, this_id, keys):
	if( self.check_if_element_present_by_type("ID", this_id) is not 0 ):
            return 1
        print "Set: Element Type: ID, Element: "+ this_id + ", Keys: " + keys
	self.driver.find_element_by_id(this_id).clear()
	self.driver.find_element_by_id(this_id).send_keys(keys)
	return 0

    def set_keys_by_css_selector(self, css_selector, keys):
	if( self.check_if_element_present_by_type("CSS_SELECTOR", css_selector) is not 0 ):
            return 1
        print "Set: Element Type: CSS_SELECTOR, Element: "+ css_selector + ", Keys: " + keys
	self.driver.find_element_by_css_selector(this_id).clear()
	self.driver.find_element_by_css_selector(this_id).send_keys(keys)
	return 0

    def set_keys_by_xpath(self, xpath, keys):
	if( self.check_if_element_present_by_type("XPATH", xpath) is not 0 ):
            return 1
        print "Set: Element Type: XPATH, Element: "+ xpath + ", Keys: " + keys
	self.driver.find_element_by_xpath(xpath).clear()
	self.driver.find_element_by_xpath(xpath).send_keys(keys)
	return 0

    def set_keys_by_name(self, name, keys):
	if( self.check_if_element_present_by_type("NAME", name) is not 0 ):
            return 1
        print "Set: Element Type: NAME, Element: "+ name + ", Keys: " + keys
	self.driver.find_element_by_name(name).clear()
	self.driver.find_element_by_name(name).send_keys(keys)
	return 0


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



