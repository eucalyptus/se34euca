import time

from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_Instance(EucaUITestLib_Base):
    def test_ui_gotopage_running(self):
        print
        print "Started Test: GotoPage Running"
        print
        self.click_element_by_id("euca-logo")
        print
        print "Test: Received the Page Title -> " + self.driver.title
        self.click_element_by_css_selector("div.status-readout")
        print
        print "Test: Clicked the GoToPage Button"
        self.verify_element_by_id("table-instances-new")
        print
        print "Finished Test: GotoPage Running"
        print
        return 0

    def test_ui_launch_instance_basic(self):
        print
        print "Started Test: Launch Instance Basic"
        print
        print "Click: LINK_TEXT -> Dashboard"
        self.click_element_by_link_text("Dashboard")
        print "Click: LINK_TEXT -> Launch new instance"
        self.click_element_by_link_text("Launch new instance")
        print "Click: CSS_SELECTOR -> div.image-name"
        self.click_element_by_css_selector("div.image-name")
        print "Click: ID -> nextButton"
        self.click_element_by_id("nextButton")
        print "Wait: ID -> launch-instance-type-num-instance"
        self.verify_element_by_id("launch-instance-type-num-instance")
        print "Click: ID -> nextButton"
        self.click_element_by_id("nextButton")
        print "Select: ID -> launch-wizard-security-keypair-selector, TEXT -> None (advanced option)"
        self.select_text_by_id("launch-wizard-security-keypair-selector", "None (advanced option)")
        print "Click: ID -> finishButton"
        self.click_element_by_id("finishButton")
        print
        print "Test: Verifying there is a Running Instance"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Verifying that Running Instances Count on Dashboard is non-zero"
        self.verify_text_not_present_by_css("div.status-readout > span", "0")
        print
        print "Finished Test: Launch Instance Basic"
        return 0


    def test_ui_launch_instance_given_name_security_group_keypair(self, instance_name, security_group, keypair):
        print
        print "Started Test: Launch Instance Given Instance Name: " + str(
            instance_name) + ", security group: " + security_group + ", keypair: " + keypair
        print
        print "Click the Dashboard link"
        self.click_element_by_link_text("Dashboard")
        # Temp. Sol - TO PREVENT EMPTY IMAGE COLLECTION WHEN TRYING TO LAUNCH INSTANCE FOR THE FIRST TIME	10/08/13
        print "Click the Image link"
        self.click_element_by_link_text("Images")
        time.sleep(5)
        print "Click the Dashboard link"
        self.click_element_by_link_text("Dashboard")
        print "Click on the 'Launch new instance' button"
        self.click_element_by_link_text("Launch new instance")
        print "Click on an Available Image"
        self.click_element_by_css_selector("div.image-name")
        print "Click the 'Next' Button"
        self.click_element_by_id("nextButton")
        print "Wait: ID -> launch-instance-type-num-instance"
        self.verify_element_by_id("launch-instance-type-num-instance")
        print "Enter instance name into Name field"
        self.set_keys_by_id("launch-instance-names", str(instance_name))
        print "Click away from input field on launch instance wizard"
        self.click_element_by_id("launch-instance-type-num-instance")
        time.sleep(5)
        print "Click the 'Next: select security' button"
        self.click_element_by_id("nextButton")
        print "Select: ID -> launch-wizard-security-keypair-selector, 'TEXT -> None (advanced option)'"
        self.select_text_by_id("launch-wizard-security-keypair-selector", str(keypair))
        self.select_text_by_id("launch-wizard-security-sg-selector", str(security_group))
        print "Click: ID -> finishButton"
        self.click_element_by_id("finishButton")
        print
        print "Verifying instance named " + instance_name + " visible on Instances Landing Page"
        self.click_element_by_link_text("Dashboard")
        print "Click: LINK_TEXT -> Instances"
        self.click_element_by_link_text("Instances")
        print "Click: CSS_SELECTOR -> li.toggle-on > ul > li > a"
        self.click_element_by_css_selector("li.toggle-on > ul > li > a")
        self.verify_element_by_link_text(instance_name)
        print
        print "Finished Test: Launch Instance Given Instance Name: " + str(
            instance_name) + ", security group: " + security_group + ", keypair: " + keypair
        print
        return 0

    def test_ui_launch_instance_from_images_lp(self, key_pair):
        print
        print "Started Test: Launch Instance from Images Landing Page"
        print
        print "Click: LINK_TEXT -> Dashboard"
        self.click_element_by_link_text("Dashboard")
        print "Click: LINK_TEXT -> Images"
        self.click_element_by_link_text("Images")
        print "Click: LINK_TEXT -> Launch instance"
        self.click_element_by_link_text("Launch instance")
        print "Click: ID -> nextButton"
        self.click_element_by_id("nextButton")
        print "Select: ID -> launch-wizard-security-keypair-selector, TEXT -> " + key_pair
        self.select_text_by_id("launch-wizard-security-keypair-selector", key_pair)
        print "Click: ID -> nextButton"
        self.click_element_by_id("finishButton")
        print
        print "Finished Test: Launch Instance from Images Landing Page"
        print

    def test_ui_launch_instance_from_instances_lp(self, key_pair):
        print
        print "Started Test: Launch Instance from Instances Landing Page"
        print
        print "Click: LINK_TEXT -> Dashboard"
        self.click_element_by_link_text("Dashboard")
        print "Click: LINK_TEXT -> Instances"
        self.click_element_by_link_text("Instances")
        print "Click: CSS_SELECTOR -> li.toggle-on > ul > li > a"
        self.click_element_by_css_selector("li.toggle-on > ul > li > a")
        print "Click: ID -> table-instances-new"
        self.click_element_by_id("table-instances-new")
        print "Click: CSS_SELECTOR -> div.image-name"
        self.click_element_by_css_selector("div.image-name")
        print "Click: ID -> nextButton"
        self.click_element_by_id("nextButton")
        print "Click: ID -> nextButton"
        self.click_element_by_id("nextButton")
        print "Select: ID -> launch-wizard-security-keypair-selector, TEXT -> "+ key_pair
        self.select_text_by_id("launch-wizard-security-keypair-selector", key_pair)
        print "Click: ID -> nextButton"
        self.click_element_by_id("finishButton")
        print
        print "Finished Test: Launch Instance from Instances Landing Page"
        print

    def test_ui_launch_more_like_this(self):
        print
        print "Started Test: Launch More Like This Instance"
        print
        print "Click: LINK_TEXT -> Dashboard"
        self.click_element_by_link_text("Dashboard")
        print "Click: LINK_TEXT -> Instances"
        self.click_element_by_link_text("Instances")
        print "Click: CSS_SELECTOR -> li.toggle-on > ul > li > a"
        self.click_element_by_css_selector("li.toggle-on > ul > li > a")
        print 'Click: CSS_SELECTOR -> td.checkbox-cell > input[type="checkbox"]'
        time.sleep(5)
        self.click_element_by_css_selector('td.checkbox-cell > input[type="checkbox"]')
        time.sleep(5)
        print"Click: ID -> more-actions-instances"
        self.click_element_by_id("more-actions-instances")
        print "Click: LINK_TEXT -> Launch more like this"
        self.click_element_by_link_text("Launch more like this")
        #print "Select: ID -> launch-more-num-instance, TEXT -> 1"
        #self.set_keys_by_id("launch-more-num-instance","1")
        print "Click: ID -> btn-launch-more"
        self.click_element_by_id("btn-launch-more")
        print
        print "Finished Test: Launch More Like This Instance"
        print

    def test_ui_terminate_instance_basic(self):
        print
        print "Started Test: Terminate Instance Basic"
        print
        print
        print "Click: LINK_TEXT -> Dashboard"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Running Instances"
        self.click_element_by_css_selector("div.status-readout")
        time.sleep(3)
        print "Test: Terminate an Instance"
        self.click_element_by_css_selector("div.table-row-status.status-running")
        #self.click_element_by_xpath("//table[@id='instances']/tbody/tr/td[5]")
        self.click_element_by_id("more-actions-instances")
        self.click_element_by_link_text("Terminate")
        self.click_element_by_id("btn-instances-terminate-terminate")
        print
        print "Finished Test: Terminate Instance Basic"
        print
        return 0

    def test_ui_terminate_instance_all(self):
        print
        print "Started Test: Terminate Instance All"
        print
        print
        print "Click: LINK_TEXT -> Dashboard"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Running Instances"
        self.click_element_by_css_selector("div.status-readout")
        print "Test: Terminate an Instance All"
        time.sleep(3)
        print "Test: checkmark the 'all' box"
        self.click_element_by_id("instances-check-all")
        print "Test: click the 'More actions' button"
        self.click_element_by_id("more-actions-instances")
        self.click_element_by_link_text("Terminate")
        print "Test: click the 'Terminate' button"
        self.click_element_by_id("btn-instances-terminate-terminate")
        print
        print "Finished Test: Terminate Instance All"
        print
        return 0

    def test_ui_associate_ip_given_instance_name_and_ip_address(self, instance_name, ip):
        '''
        Associate the IP to the Instance given input
        '''
        print
        print "Started Test: Associate IP Given Instance Name and IP Address"
        print
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_css_selector("div.status-readout")
        time.sleep(3)
        self.click_element_by_link_text(instance_name)
        time.sleep(1)
        instance_id = self.get_text_by_xpath("//div[@id='tabs-1']/ul/li[2]/div[2]")
        self.click_element_by_id(instance_id)
        self.click_element_by_id("more-actions-instances")
        self.click_element_by_link_text("Associate IP address")
        self.set_keys_by_xpath("(//input[@id='associate-selected-value'])[2]", ip)
        self.click_element_by_link_text(ip)
        self.click_element_by_id("eip-associate-btn")
        print
        print "Finished Test: Associate IP Given Instance Name and IP Address"
        print
        return 0

    def test_ui_verify_associate_ip_given_instance_name_and_ip_address(self, instance_name, ip):
        '''
        Verify That the IP is associated to the instance
        '''
        print
        print "Started Test: Verify Associate IP Given Instance Name and IP Address."
        print
        print "Instance Name: " + instance_name
        print "IP: " + ip
        print
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_css_selector("div.status-readout")
        time.sleep(3)
        self.click_element_by_link_text(instance_name)

        is_matched = False
        count = 0
        while( is_matched is False and count < 3 ):
            associated_ip = self.get_text_by_xpath("//div[@id='tabs-1']/ul/li[5]/div[2]")
            print
            print "Instance " + instance_name + " is currently associated with " + associated_ip
            if( str(ip) == str(associated_ip) ):
                is_matched = True
                break
            print "Returned IP " + associated_ip + " is not matched with the input IP " + ip
            count = count + 1
            print "Sleeping 10 sec"
            time.sleep(10)

        if( is_matched is False ):
            print
            print "FAILED TEST: Verify Associate IP Given Instance Name and IP Address"
            print
            self.fail("time out")
        else:
                print
               	print "Finished Test: Associate IP Given Instance Name and IP Address"
                print
        return 0

    def test_ui_associate_ip_from_inst_lp(self):
        '''
        Requires a running instance and an available ip.

        Picks a running instance from Instances Landing Page
        and using dialog from Instance Landing Page associates to it the first unassigned IP from the list on IP address Landing Page.
        '''
        print
        print "Started Test: Associate IP from Instances Landing Page"
        print
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("IP Addresses")
        time.sleep(3)
        self.click_element_by_css_selector("div.VS-search-inner")
        self.click_element_by_link_text("Assignment")
        self.click_element_by_link_text("Unassigned")
        time.sleep(3)
        available_ip = self.get_text_by_xpath("//table[@id='eips']/tbody/tr/td[2]")
        self.click_element_by_link_text("Instances")
        self.click_element_by_css_selector("li.toggle-on > ul > li > a")
        time.sleep(3)
        self.click_element_by_css_selector("div.table-row-status.status-running")
        self.click_element_by_id("more-actions-instances")
        self.click_element_by_link_text("Associate IP address")
        self.set_keys_by_xpath("(//input[@id='associate-selected-value'])[2]", available_ip)
        self.click_element_by_link_text(available_ip)
        self.click_element_by_id("eip-associate-btn")     
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("IP Addresses")

        print "Test: Verifying " + str(available_ip) + " is in assigned state."

        for i in range(1, self.trials, 1):
            self.click_element_by_css_selector("div.VS-search-inner")
            self.click_element_by_link_text("Assignment")
            print
            print "Test: Trial " + str(i) + " : waiting for the Assigned filter to appear on IP Addresses LP..."
            if self.is_element_present(By.LINK_TEXT, "Assigned"):
                break
        print
        print "Test: Assigned filter present"
        self.click_element_by_css_selector("div.VS-search-inner")
        self.click_element_by_link_text("Assignment")
        self.click_element_by_link_text("Assigned")
        print "Test: Verify that " + str(available_ip) + " can be seen in the 'Assigned' filter"
        self.verify_element_by_link_text(available_ip)
        print
        print "Finished Test: Associate IP from Instances Landing Page"
        print

    def test_ui_associate_ip_from_ip_lp(self, instance_name):
        #broken: EUCA-7561
        '''
        Requires a running instance named "testinstance"  and an available ip.

        Picks an available IP from IP Landing Page
        and using dialog from IP Landing Page associates an instance to the available IP.
        '''
        print
        print "Started Test: Associate IP from IP Landing Page"
        print
        self.click_element_by_link_text("Dashboard")
        print
        print "Test: Go to the Page Running Instances"
        self.click_element_by_css_selector("div.status-readout")
        time.sleep(3)
        print "Open expando of instance named " + instance_name
        self.click_element_by_link_text(str(instance_name))
        print "Get instance id from expando"
        time.sleep(1)
        instance_id = self.get_text_by_xpath("//div[@id='tabs-1']/ul/li[2]/div[2]")
        print "Go to IP Addresses Landing Page"
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("IP Addresses")
        print "On the search bar filter by 'Assignment: Unassigned'"
        self.click_element_by_css_selector("div.VS-search-inner")
        self.click_element_by_link_text("Assignment")
        self.click_element_by_link_text("Unassigned")
        print "Get the unassigned IP address"
        available_ip_address = self.get_text_by_xpath(
            "/html/body/div/div[4]/div/div/div/div/div/table/tbody/tr/td[2]/a")
        self.click_element_by_id(str(available_ip_address))
        self.click_element_by_id("more-actions-eips")
        self.click_element_by_link_text("Associate with instance")
        self.set_keys_by_id("associate-selected-value", str(instance_id))
        self.click_element_by_id("eip-associate-btn")
        print
        print "Finished Test: Associate IP from IP Landing Page"
        print

    def test_ui_disassociate_ip_from_inst_lp(self):
        '''
        Requires an only running instance with associated ip.

        Picks a running instance from Instances Landing Page
        and using dialog from Instance Landing Page disassociates assigned IP.
        '''
        # To get ID of an instance that has an IP associated to it
        #self.click_element_by_link_text("Dashboard")
        #self.click_element_by_link_text("Network & Security")
        #self.click_element_by_link_text("IP Addresses")
        #self.click_element_by_css_selector("th.wrap-content.sorting")
        #self.click_element_by_css_selector("th.wrap-content.sorting")
        #associated_instance_id=self.get_text_by_id("eips.1.2").text
        print
        print "Started Test: Disassociate IP from Instances Landing Page"
        print
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Instances")
        self.click_element_by_css_selector("li.toggle-on > ul > li > a")
        time.sleep(3)
        self.click_element_by_css_selector("div.table-row-status.status-running")
        self.click_element_by_link_text("More actions")
        self.click_element_by_link_text("Disassociate IP address")
        self.click_element_by_id("btn-eip-disassociate-disassociate")
        print
        print "Finished Test: Disassociate IP from Instances Landing Page"
        print

    def test_ui_disassociate_ip_from_ip_lp(self):
        '''
        Requires an only running instance named "testinstance" with associated ip.

        '''
        print
        print "Started Test: Disassociate IP from IP Addresses Landing Page"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        time.sleep(3)
        self.click_element_by_css_selector("div.status-readout > span")
        time.sleep(3)
        print "Test: clicked on running instances link on Dashboard"
        self.click_element_by_link_text("testinstance")
        time.sleep(1)
        associated_ip_address = self.get_text_by_xpath("//div[@id='tabs-1']/ul/li[5]/div[2]")
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("IP Addresses")
        time.sleep(3)
        self.click_element_by_id(str(associated_ip_address))
        self.click_element_by_id("more-actions-eips")
        self.click_element_by_link_text("Disassociate from instance")
        self.click_element_by_id("btn-eip-disassociate-disassociate")
        self.verify_text_not_present_by_xpath("//table[@id='eips']/tbody/tr/td[3]", "testinstance")
        print
        print "Finished Test: Disassociate IP from IP Addresses Landing Page"


    def test_ui_check_running_instances_count(self, running_instances_count):
        print
        print "Started Test: Check Running Instances Count"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        time.sleep(3)
        print "Verifying that Running Instances Count on Dashboard is " + running_instances_count
        self.verify_text_displayed_by_css("div.status-readout > span", running_instances_count)
        print
        print "Finished Test: Check Running Instances Count"


if __name__ == "__main__":
    unittest.main()



