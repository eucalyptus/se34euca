from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class lib_euca_ui_test(unittest.TestCase):

    ui_ip = "localhost"
    port = "8888"
    accountname = "eucalyptus"
    username = "admin"
    password = "password"

    def setUIInfo(self, ip, port):
	self.ui_ip = ip
	self.port = port
	print "UI IP: " + ip
	print "PORT: " + port

    def setUserInfo(self, accountname, username, password):
	self.accountname = accountname
	self.username = username
	self.password = password
	print "ACCOUNTNAME: " + accountname
	print "USERNAME: " + username
	print "PASSWORD: " + password


    def setUp(self):
	print "=== setUp ==="
#	this_ui = "http://" + self.ui_ip + ":" + self.port + "/"
	this_ui = "https://" + self.ui_ip + ":" + self.port
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = this_ui
        self.verificationErrors = []
	print "Started Selenium Webdriver: " + self.base_url
	print

    def tearDown(self):
	print "=== tearDown ==="
	self.driver.quit()
        self.assertEqual([], self.verificationErrors)
	print "Stopped Selenium Webdriver: " + self.base_url
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
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "login"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "login"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Test: Received the Login Page"
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys(self.accountname)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(self.password)
        driver.find_element_by_name("login").click()
	print "Test: Typed the User Info and Clicked the Login Button"
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Launch new instance"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: Login"
	print

    def test_ui_logout(self):
	print "Started Test: Logout"
        driver = self.driver
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.LINK_TEXT, "Launch new instance"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	this_link = self.username + "@" + self.accountname
	for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, this_link): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Clicking User Account Menu " + this_link
        driver.find_element_by_link_text(this_link).click()
#        driver.find_element_by_css_selector("body").click()
	print "Test: Clicked User Account Menu " + this_link
	for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Log out"): break
            except: pass
	    time.sleep(1)
        else: self.fail("time out")
	print "Test: Clicking Log out"
	driver.find_element_by_link_text("Log out").click()
#        driver.find_element_by_css_selector("body").click()
	print "Test: Clicked the Logout Button"
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "login"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "login"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: Logout"
	print

    def test_ui_gotopage_keypairs(self):
	print "Started Test: GotoPage Keypairs"
        driver = self.driver
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "dashboard-netsec-keypair"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "dashboard-netsec-keypair"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("dashboard-netsec-keypair").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-keys-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "table-keys-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Keypairs"
	print

    def test_ui_gotopage_running(self):
	print "Started Test: GotoPage Running"
        driver = self.driver
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "div.status-readout"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.status-readout"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.status-readout").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-instances-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "table-instances-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Running"
	print

    def test_ui_gotopage_security_groups(self):
	print "Started Test: GotoPage Security Groups"
        driver = self.driver
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "dashboard-netsec-sgroup"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "dashboard-netsec-sgroup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("dashboard-netsec-sgroup").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-sgroups-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "table-sgroups-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Security Groups"
	print    

    def test_ui_gotopage_volumes(self):
	print "Started Test: GotoPage Volumes"
        driver = self.driver
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "dashboard-storage-volume"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("dashboard-storage-volume").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertTrue(self.is_element_present(By.ID, "table-volumes-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Volumes"
	print 


    def test_ui_launch_instance_basic(self):
	print "Started Test: Launch Instance Baisc"
        driver = self.driver
        driver.find_element_by_link_text("Launch new instance").click()
	print "Test: Clicking Through Default Options"
        driver.find_element_by_css_selector("tr.odd.selected-row").click()
        driver.find_element_by_id("launch-wizard-buttons-image-next").click()
        driver.find_element_by_id("launch-wizard-buttons-type-next").click()
        driver.find_element_by_id("launch-wizard-buttons-security-launch").click()
	print "Test: Launched an Instance at its default setting"
	print "Finished Test: Launch Instance Basic"
	print 


    def test_ui_terminate_instance_basic(self):
	print "Started Test: Terminate Instance Basic"
        driver = self.driver
	print "Test: Go to the Page Running Instances"
	driver.find_element_by_css_selector("div.status-readout").click()
	print "Test: Terminate an Instance"
        driver.find_element_by_xpath("//table[@id='instances']/tbody/tr/td[5]").click()
        driver.find_element_by_id("more-actions-instances").click()
        driver.find_element_by_link_text("Terminate").click()
        driver.find_element_by_id("btn-instances-terminate-terminate").click()
	print "Finished Test: Terminate Instance Basic"
	print 


    def test_ui_generate_keypair(self):
	print "Started Test: Generate Keypair"
        driver = self.driver
	print "Test: Go to the Page Keypair"
        driver.find_element_by_id("dashboard-netsec-keypair").click()
	print "Test: Generate New Keypair"
        driver.find_element_by_id("table-keys-new").click()
        driver.find_element_by_id("key-name").clear()
        driver.find_element_by_id("key-name").send_keys("my-sel-gen-key-00")
        # ERROR: Caught exception [ERROR: Unsupported command [typeKeys]]
        driver.find_element_by_id("keys-add-btn").click()
	print "Finished Test: Generate Keypair"
	print


    def test_ui_delete_keypair(self):
	print "Started Test: Delete Keypair"
        driver = self.driver
	print "Test: Go to the Page Keypair"
        driver.find_element_by_id("dashboard-netsec-keypair").click()
	print "Test: Delete Keypair"
        driver.find_element_by_xpath("//table[@id='keys']/tbody/tr/td[2]").click()
        driver.find_element_by_id("more-actions-keys").click()
        driver.find_element_by_link_text("Delete").click()
        driver.find_element_by_id("btn-keys-delete-delete").click()
	print "Finished Test: Delete Keypair"
	print

    def test_ui_create_volume(self):
	print "Started Test: Create Volume"
        driver = self.driver
	print "Test: Go to the Page Volume"
        driver.find_element_by_id("dashboard-storage-volume").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Create New Volume"
        driver.find_element_by_id("table-volumes-new").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "volume-size"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("volume-size").clear()
        driver.find_element_by_id("volume-size").send_keys("2")
        # ERROR: Caught exception [ERROR: Unsupported command [typeKeys | id=volume-size | 2]]
        driver.find_element_by_id("volumes-add-btn").click()
 	print "Finished: Create New Volume"

    def test_ui_delete_volume(self):
	print "Started Test: Delete Volume"
	driver = self.driver
	print "Test: Go to the Page Volume"
	driver.find_element_by_id("dashboard-storage-volume").click()
	driver.find_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]").click()
	for i in range(60):
	    try:
		if self.is_element_present(By.ID, "more-actions-volumes"): break
	    except: pass
	    time.sleep(1)
	else: self.fail("time out")
	print "Test: Delete Volume"
	driver.find_element_by_id("more-actions-volumes").click()
#	driver.find_element_by_css_selector("body").click()
	for i in range(60):
	    try:
		if self.is_element_present(By.LINK_TEXT, "Delete"): break
	    except: pass
	    time.sleep(1)
	else: self.fail("time out")
	driver.find_element_by_link_text("Delete").click()
#	driver.find_element_by_css_selector("body").click()
	for i in range(60):
	    try:
		if self.is_element_present(By.ID, "btn-volumes-delete-delete"): break
	    except: pass
	    time.sleep(1)
	else: self.fail("time out")
	driver.find_element_by_id("btn-volumes-delete-delete").click()
    	print "Finished: Delete Volume"

    def test_ui_create_snapshot_from_volume(self):
	print "Started Test: Create Snapshot From Volume"
        driver = self.driver
	print "Test: Go to the Page Volume"
        driver.find_element_by_css_selector("#dashboard-storage-volume > span").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "more-actions-volumes"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Create Snapshot From Volume"
        driver.find_element_by_id("more-actions-volumes").click()
#        driver.find_element_by_css_selector("body").click()
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Create snapshot from volume"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text("Create snapshot from volume").click()
#        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("snapshot-create-description").clear()
        driver.find_element_by_id("snapshot-create-description").send_keys("snapshot by selenium script")
        driver.find_element_by_id("snapshot-create-btn").click()
	print "Finished: Create Snapshot From Volume"   

    def test_ui_delete_snapshot(self):
	print "Started Test: Delete Snapshot"
        driver = self.driver
	print "Test: Go to the Page Snapshot"
        driver.find_element_by_css_selector("#dashboard-storage-snapshot > span").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-snapshots-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "more-actions-snapshots"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("more-actions-snapshots").click()
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Delete"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Delete Snapshot"
        driver.find_element_by_link_text("Delete").click()
#        driver.find_element_by_css_selector("body").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "btn-snapshots-delete-delete"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("btn-snapshots-delete-delete").click()
	print "Finished: Delete Snapshot" 

    def test_ui_create_volume_from_snapshot(self):
	print "Started Test: Create Volume From Snapshot"
        driver = self.driver
	print "Test: Go to the Page Snapshot"
        driver.find_element_by_css_selector("#dashboard-storage-snapshot > span").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-snapshots-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "more-actions-snapshots"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Create Volume From Snapshot"
        driver.find_element_by_id("more-actions-snapshots").click()
        driver.find_element_by_link_text("Create volume from snapshot").click()
#        driver.find_element_by_css_selector("body").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "volumes-add-btn"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("volumes-add-btn").click()
	print "Finished: Create Volume From Snapshot"

    def test_ui_create_security_group(self):
	print "Started Test: Create Security Group"
        driver = self.driver
	print "Test: Go to the Page Security Group"
        driver.find_element_by_css_selector("#dashboard-netsec-sgroup > span").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-sgroups-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("table-sgroups-new").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-name"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Create Security Group"
        driver.find_element_by_id("sgroup-name").clear()
        driver.find_element_by_id("sgroup-name").send_keys("mywebservice")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-description"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("sgroup-description").clear()
        driver.find_element_by_id("sgroup-description").send_keys("rules for my webservice")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-template"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        Select(driver.find_element_by_id("sgroup-template")).select_by_visible_text("SSH (TCP port 22, for terminal access)")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "allow-ip"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("allow-ip").clear()
        driver.find_element_by_id("allow-ip").send_keys("0.0.0.0/0")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-add-rule"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("sgroup-add-rule").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-template"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        Select(driver.find_element_by_id("sgroup-template")).select_by_visible_text("HTTP (TCP port 80, for web servers)")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "allow-ip"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("allow-ip").clear()
        driver.find_element_by_id("allow-ip").send_keys("0.0.0.0/0")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-add-rule"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("sgroup-add-rule").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-template"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        Select(driver.find_element_by_id("sgroup-template")).select_by_visible_text("Custom ICMP")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-type"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        Select(driver.find_element_by_id("sgroup-type")).select_by_visible_text("All")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "allow-ip"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("allow-ip").clear()
        driver.find_element_by_id("allow-ip").send_keys("0.0.0.0/0")
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-add-rule"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("sgroup-add-rule").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "sgroup-add-btn"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("sgroup-add-btn").click()
    	print "Finished: Create Security Group"

    def test_ui_delete_security_group(self):
	print "Started Test: Delete Security Group"
        driver = self.driver
	print "Test: Go to the Page Security Group"
        driver.find_element_by_css_selector("#dashboard-netsec-sgroup > span").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-sgroups-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "more-actions-sgroups"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("more-actions-sgroups").click()
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Delete"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Delete Security Group"
        driver.find_element_by_link_text("Delete").click()
#        driver.find_element_by_css_selector("body").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "btn-sgroups-delete-delete"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("btn-sgroups-delete-delete").click()
 	print "Finished: Delete Security Group"

    def test_ui_allocate_two_ip_addresses(self):
	print "Started Test: Allocate Two IP Addresses"
        driver = self.driver
        print "Test: Go to the Page IP Address"
        driver.find_element_by_id("dashboard-netsec-eip").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-eips-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("table-eips-new").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "eip-allocate-count"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Allocate Two IP Addresses"
        driver.find_element_by_id("eip-allocate-count").clear()
        driver.find_element_by_id("eip-allocate-count").send_keys("2")
        # ERROR: Caught exception [ERROR: Unsupported command [typeKeys | id=eip-allocate-count | 2]]
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "eip-allocate-btn"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("eip-allocate-btn").click()
	print "Finished: Allocate Two IP Addresses"

    def test_ui_release_ip_address(self):
	print "Started Test: Release IP Address"
        driver = self.driver
        print "Test: Go to the Page IP Address"
        driver.find_element_by_css_selector("#dashboard-netsec-eip > span").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "table-eips-new"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "more-actions-eips"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("more-actions-eips").click()
#        driver.find_element_by_css_selector("body").click()
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Release to cloud"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	print "Test: Release IP Address"
        driver.find_element_by_link_text("Release to cloud").click()
#        driver.find_element_by_css_selector("body").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "btn-eips-release-release"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("btn-eips-release-release").click()
	print "Finished: Release IP Address" 

    def test_ui_view_page_get_dashboard_source(self):
	print "Started Test: View Page Get Dashboard Source"
	print
        driver = self.driver
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
	print "Finished Test: View Page Get Dashboard Source"
	print

if __name__ == "__main__":
    unittest.main()



