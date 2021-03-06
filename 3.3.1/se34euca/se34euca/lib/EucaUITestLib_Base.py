from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


import unittest, time, re



class UICheckException(Exception):
    def __init__(self, message):
        raise Exception(message)

class EucaUITestLib_Base(unittest.TestCase):



    selenium_server_ip = "localhost"
    selenium_server_port = "4444"
    ui_ip = "localhost"
    port = "8888"
    accountname = "eucalyptus"
    username = "admin"
    password = "password"
    retry = 400 #waiting time in seconds for element to be present on page


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
        print
        if self.selenium_server_ip is not "localhost":
            print "SET REMOTE WEBDRIVER AT: " + this_selenium_server_url
            self.driver = webdriver.Remote(this_selenium_server_url, webdriver.DesiredCapabilities.FIREFOX)
        else:
            print "SET LOCAL WEBDRIVER"
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
        self.base_url = this_ui
        self.verificationErrors = []
        print
        print "STARTED SELENIUM TEST ON EUCALYPTUS AT: " + self.base_url
        print
        return 0

    def tearDown(self):
        print
        print "=== tearDown ==="
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print
        print "FINISHED SELENIUM TEST ON EUCALYPTUS AT: " + self.base_url
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
        self.set_keys_by_id("account", self.accountname)
        self.set_keys_by_id("username", self.username)
        self.set_keys_by_id("password", self.password)
        print
        print "Test: Typed the User Info and Clicked the Login Button"
        self.click_element_by_name("login")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Finished Test: Login"
        print
        return 0


    def test_ui_admin_console_login(self):
        print
        print "Started Test: Admin Console Login"
        self.driver.get(self.base_url + "/")
        print
        print "Test: Received the Page Title -> " + self.driver.title
        self.verify_element_by_id("loginForm")
        print
        print "Test: Received the Login Page"
        self.set_keys_by_id("accountName", self.accountname)
        self.set_keys_by_id("userName", self.username)
        self.set_keys_by_id("password", self.password)
        print
        print "Test: Typed the User Info and Clicked the Login Button"
        self.click_element_by_css_selector('input[type="submit"]')
        self.verify_element_by_link_text(str(self.username)+"@"+str(self.accountname))
        print
        print "Finished Test: Admin Console Login"
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

    def test_ui_admin_console_logout(self):
        print
        print "Started Test: Admin Console Logout"
        print "Test: Received the Page Title -> " + self.driver.title
        self.verify_element_by_link_text(str(self.username)+"@"+str(self.accountname))
        this_link = self.username + "@" + self.accountname
        print "Test: Clicked User Account Menu " + this_link
        self.click_element_by_link_text(this_link)
        print "Test: Clicked the Logout Button"
        self.click_element_by_link_text("Sign out")
        self.verify_element_by_id("logoImage")
        print
        print "Finished Test: Admin Console Logout"
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
        running_instance_count = self.get_text_by_css_selector("div.status-readout").split("\n")[0]
        stopped_instance_count = self.get_text_by_id("dashboard-instance-stopped").split("\n")[0]
        volume_count = self.get_text_by_id("dashboard-storage-volume").split("\n")[0]
        snapshot_count = self.get_text_by_id("dashboard-storage-snapshot").split("\n")[0]
        sgroup_count = self.get_text_by_id("dashboard-netsec-sgroup").split("\n")[0]
        keypair_count = self.get_text_by_id("dashboard-netsec-keypair").split("\n")[0]
        eip_count = self.get_text_by_id("dashboard-netsec-eip").split("\n")[0]
        print
        print "[DASHBOARD] Running Instances: " + running_instance_count
        print "[DASHBOARD] Stopped Instances: " + stopped_instance_count
        print "[DASHBOARD] Volumes: " + volume_count
        print "[DASHBOARD] Snapshots: " + snapshot_count
        print "[DASHBOARD] Security Groups: " + sgroup_count
        print "[DASHBOARD] Keypairs: " + keypair_count
        print "[DASHBOARD] IP Addresses: " + eip_count
        print
        print "Finished Test: View Page Get Dashboard Source"
        print
        return 0


    # VERIFY ELEMENT BY TYPE
    def check_if_element_present_by_type(self, element_type, element):

        """

        :param element_type:
        :param element:
        :return: :raise:
        """
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
            except: pass
            #raise UICheckException("Time out")
            time.sleep(1)
       # else:
       #     self.fail("timed out after "+`self.retry`+" seconds")

        try:
            self.assertTrue(self.is_element_present(this_element_type, element))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
            print "TEST FAILED::: Wait On:: Element Type: " + element_type + ", Element: " + element
            raise UICheckException("Failed to find element of type " + element_type + element +" present" )


        print "Found:: Element type: " + element_type + ", Element: " + element
        return 0


    # VERIFY ELEMENT NOT PRESENT

    def verify_element_not_present_by_type(self, element_type, element):

        print "Test: Verifying element not present by type."

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
            print "Test:: Verify not present. Trial: " + str(i) + " Element Type: " + element_type + ", Element: " + element
            if self.is_element_present(this_element_type, element) == True:
                print "Test:: Verified not present.  Element Type: " + element_type + ", Element: " + element
                break
            else:
                print "Test:: FAILED Verify not present. Element Type: " + element_type + ", Element: " + element



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


    #VERIFY TEXT DISPLAYED

    def verify_text_displayed_by_id(self, element_id, element_text):
        #print("Verifying text " +element_text+" displayed at ID "+element_id)
        for i in range(self.retry):
            print "Wait On:: Trial: " + str(i)  +("Verifying text " +element_text+" displayed at ID "+element_id)
            try:
                if element_text == self.driver.find_element_by_id(element_id).text:
                    print"Found text"
                    break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(element_text, self.driver.find_element_by_id(element_id).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        displayed_text = self.driver.find_element_by_id(element_id).text
        print("Text displayed at ID "+element_id +" is " +displayed_text)


    def verify_text_displayed_by_css(self,element_css,element_text):
        #print("Verifying text " +element_text+" displayed at ID "+element_css)
        for i in range(self.retry):
            print "Wait On:: Trial: " + str(i)  +("Verifying text " +element_text+" displayed at ID "+element_css)
            try:
                if element_text == self.driver.find_element_by_css_selector(element_css).text:
                    print"Found text"
                    break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(element_text, self.driver.find_element_by_css_selector(element_css).text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        displayed_text = self.driver.find_element_by_css_selector(element_css).text
        print("Text displayed at ID "+element_css +" is " +displayed_text)




    # CLICK CALLS
    def click_element_by_link_text(self, link_text):
        if( self.check_if_element_present_by_type("LINK_TEXT", link_text) is not 0 ):
            raise UICheckException("Element by link text not present: " + link_text)
        print "Click: Element Type: LINK_TEXT, Element: "+ link_text
        self.driver.find_element_by_link_text(link_text).click()
        return 0

    def click_element_by_id(self, this_id):
        if( self.check_if_element_present_by_type("ID", this_id) is not 0 ):
            raise UICheckException("Element by id not present: " + this_id )
        print "Click: Element Type: ID, Element: "+ this_id
        self.driver.find_element_by_id(this_id).click()
        return 0

    def click_element_by_css_selector(self, css_selector):
        if( self.check_if_element_present_by_type("CSS_SELECTOR", css_selector) is not 0 ):
            raise UICheckException("Element by css selector not present: " + css_selector)
        print "Click: Element Type: CSS_SELECTOR, Element: "+ css_selector
        self.driver.find_element_by_css_selector(css_selector).click()
        return 0

    def click_element_by_xpath(self, xpath):
        if( self.check_if_element_present_by_type("XPATH", xpath) is not 0 ):
            raise UICheckException("Element by xpath not present: " +xpath)
        print "Click: Element Type: XPATH, Element: "+ xpath
        self.driver.find_element_by_xpath(xpath).click()
        return 0
    
    def click_element_by_name(self, name):
        if( self.check_if_element_present_by_type("NAME", name) is not 0 ):
            raise UICheckException("Element by name not present: " +name)
        print "Click: Element Type: NAME, Element: "+ name
        self.driver.find_element_by_name(name).click()
        return 0


    # SET KEYS CALLS
    def set_keys_by_link_text(self, link_text, keys):
        if( self.check_if_element_present_by_type("LINK_TEXT", link_text) is not 0 ):
            raise UICheckException("Element by link text not present:" + link_text)
        print "Set: Element Type: LINK_TEXT, Element: "+ link_text + ", Keys: " + keys
        self.driver.find_element_by_link_text(link_text).clear()
        self.driver.find_element_by_link_text(link_text).send_keys(keys)
        return 0

    def set_keys_by_id(self, this_id, keys):
        if( self.check_if_element_present_by_type("ID", this_id) is not 0 ):
            raise UICheckException("Element by id not present:" + this_id)
        print "Set: Element Type: ID, Element: "+ this_id + ", Keys: " + keys
        self.driver.find_element_by_id(this_id).clear()
        self.driver.find_element_by_id(this_id).send_keys(keys)
        return 0

    def set_keys_by_css_selector(self, css_selector, keys):
        if( self.check_if_element_present_by_type("CSS_SELECTOR", css_selector) is not 0 ):
            raise UICheckException("Element by css selector not present:" + css_selector)
        print "Set: Element Type: CSS_SELECTOR, Element: "+ css_selector + ", Keys: " + keys
        self.driver.find_element_by_css_selector(css_selector).clear()
        self.driver.find_element_by_css_selector(css_selector).send_keys(keys)
        return 0

    def set_keys_by_xpath(self, xpath, keys):
        if( self.check_if_element_present_by_type("XPATH", xpath) is not 0 ):
            raise UICheckException("Element by xpath not found :" + xpath)
        print "Set: Element Type: XPATH, Element: "+ xpath + ", Keys: " + keys
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(keys)
        return 0

    def set_keys_by_name(self, name, keys):
        if( self.check_if_element_present_by_type("NAME", name) is not 0 ):
            raise UICheckException("Element by name not found:" +name)
        print "Set: Element Type: NAME, Element: "+ name + ", Keys: " + keys
        self.driver.find_element_by_name(name).clear()
        self.driver.find_element_by_name(name).send_keys(keys)
        return 0


    # GET TEXT CALLS
    def get_text_by_link_text(self, link_text):
        if( self.check_if_element_present_by_type("LINK_TEXT", link_text) is not 0 ):
            raise UICheckException("Element by link text not present:" +link_text)
        print "Get Text: Element Type: LINK_TEXT, Element: "+ link_text
        return self.driver.find_element_by_link_text(link_text).text

    def get_text_by_id(self, this_id):
        if( self.check_if_element_present_by_type("ID", this_id) is not 0 ):
            raise UICheckException("Element by id not present:" + this_id)
        print "Get Text: Element Type: ID, Element: "+ this_id
        return self.driver.find_element_by_id(this_id).text


    def get_text_by_css_selector(self, css_selector):
        if( self.check_if_element_present_by_type("CSS_SELECTOR", css_selector) is not 0 ):
            raise UICheckException("Element by css selector not present:" + css_selector)
        print "Get Text: Element Type: CSS_SELECTOR, Element: "+ css_selector
        return self.driver.find_element_by_css_selector(css_selector).text

    def get_text_by_xpath(self, xpath):
        if( self.check_if_element_present_by_type("XPATH", xpath) is not 0 ):
            raise UICheckException("Element by xpath not present: " +xpath)
        print "Get Text: Element Type: XPATH, Element: "+ xpath
        return self.driver.find_element_by_xpath(xpath).text
    
    def get_text_by_name(self, name):
        if( self.check_if_element_present_by_type("NAME", name) is not 0 ):
            raise UICheckException("Element by name not present: " + name)
        print "Click: Element Type: NAME, Element: "+ name
        return self.driver.find_element_by_name(name).text


    # SELECT TEXT CALLS
    def select_text_by_link_text(self, link_text, visible_text):
        if( self.check_if_element_present_by_type("LINK_TEXT", link_text) is not 0 ):
            raise UICheckException("Element by link text not present: " + link_text)
        print "Select: Element Type: LINK_TEXT, Element: "+ link_text + ", Text: " + visible_text
        Select(self.driver.find_element_by_link_text(link_text)).select_by_visible_text(visible_text)
        return 0

    def select_text_by_id(self, this_id, visible_text):
        if( self.check_if_element_present_by_type("ID", this_id) is not 0 ):
            raise UICheckException("Element by id not present: " + this_id)
        print "Select: Element Type: ID, Element: "+ this_id + ", Text: " + visible_text
        Select(self.driver.find_element_by_id(this_id)).select_by_visible_text(visible_text)
        return 0

    def select_text_by_css_selector(self, css_selector, visible_text):
        if( self.check_if_element_present_by_type("CSS_SELECTOR", css_selector) is not 0 ):
            raise UICheckException("Element by css selector not present: " + css_selector)
        print "Select: Element Type: CSS_SELECTOR, Element: "+ css_selector + ", Text: " + visible_text
        Select(self.driver.find_element_by_css_selector(css_selector)).select_by_visible_text(visible_text)
        return 0

    def select_text_by_xpath(self, xpath, visible_text):
        if(self.check_if_element_present_by_type("XPATH", xpath) is not 0 ):
            raise UICheckException("Element by xpath not present: " + xpath)
        print "Select: Element Type: XPATH, Element: "+ xpath + ", Text: " + visible_text
        Select(self.driver.find_element_by_xpath(xpath)).select_by_visible_text(visible_text)
        return 0
    
    def select_text_by_name(self, name, visible_text):
        if(self.check_if_element_present_by_type("NAME", name) is not 0 ):
            raise UICheckException("Element by name not present: " + name)
        print "Select: Element Type: NAME, Element: "+ name + ", Text: " + visible_text
        Select(self.driver.find_element_by_name(name)).select_by_visible_text(visible_text)
        return 0




if __name__ == "__main__":
    unittest.main()



