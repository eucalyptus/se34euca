from se34euca.lib.EucaUITestLib_Base import *
import time

class EucaUITestLib_Instance(EucaUITestLib_Base):

    def test_ui_gotopage_running(self):
        print
        print "Started Test: GotoPage Running"
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
        print "Finished Test: Launch Instance Basic"
        print
        return 0



    def test_ui_launch_instance_given_instance_name(self, instance_name):

        print
        print "Started Test: Launch Instance Given Instance Name: " + str(instance_name)
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
        self.set_keys_by_id("launch-instance-names", str(instance_name))
        print "Click: ID -> nextButton"
        self.click_element_by_id("nextButton")
        print "Select: ID -> launch-wizard-security-keypair-selector, TEXT -> None (advanced option)"
        self.select_text_by_id("launch-wizard-security-keypair-selector", "None (advanced option)")
        print "Click: ID -> finishButton"
        self.click_element_by_id("finishButton")
        print
        print "Finished Test: Launch Instance Basic"
        print
        return 0

    def test_ui_launch_instance_from_images_lp(self):
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
        print "Select: ID -> launch-wizard-security-keypair-selector, TEXT -> my-sel-gen-key-00"
        self.select_text_by_id("launch-wizard-security-keypair-selector", "my-sel-gen-key-00")
        print "Click: ID -> nextButton"
        self.click_element_by_id("finishButton")

    def test_ui_launch_instance_from_instances_lp(self):
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
        print "Select: ID -> launch-wizard-security-keypair-selector, TEXT -> my-sel-gen-key-00"
        self.select_text_by_id("launch-wizard-security-keypair-selector", "my-sel-gen-key-00")
        print "Click: ID -> nextButton"
        self.click_element_by_id("finishButton")

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

    def test_ui_terminate_instance_basic(self):
        print
        print "Started Test: Terminate Instance Basic"
        print
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Running Instances"
        self.click_element_by_css_selector("div.status-readout")
        print "Test: Terminate an Instance"
        self.click_element_by_xpath("//table[@id='instances']/tbody/tr/td[5]")
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
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Running Instances"
        self.click_element_by_css_selector("div.status-readout")
        print "Test: Terminate an Instance All"
        time.sleep(5)
        self.click_element_by_id("instances-check-all")
        time.sleep(5)
        self.click_element_by_id("more-actions-instances")
        self.click_element_by_link_text("Terminate")
        self.click_element_by_id("btn-instances-terminate-terminate")
        print
        print "Finished Test: Terminate Instance All"
        print
        return 0

    def test_ui_associate_ip_from_inst_lp(self):
        '''
        Requires a running instance and an available ip.

        Picks a running instance from Instances Landing Page
        and using dialog from Instance Landing Page associates to it the first unassigned IP from the list on IP address Landing Page.
        '''
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("IP Addresses")
        self.click_element_by_css_selector("div.VS-search-inner")
        self.click_element_by_link_text("Assignment")
        self.click_element_by_link_text("Unassigned")
        available_ip=self.get_text_by_xpath("//table[@id='eips']/tbody/tr/td[2]")
        self.click_element_by_link_text("Instances")
        self.click_element_by_css_selector("li.toggle-on > ul > li > a")
        self.click_element_by_css_selector("div.table-row-status.status-running")
        self.click_element_by_id("more-actions-instances")
        self.click_element_by_link_text("Associate IP address")
        self.set_keys_by_xpath("(//input[@id='associate-selected-value'])[2]",available_ip)
        self.click_element_by_link_text(available_ip)
        self.click_element_by_id("eip-associate-btn")
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("IP Addresses")
        print "Test: Verifying " + str(available_ip) + " is in assigned state."
        self.click_element_by_css_selector("div.VS-search-inner")
        self.click_element_by_link_text("Assignment")
        self.click_element_by_link_text("Assigned")
        self.verify_element_by_link_text(available_ip)



    def test_ui_check_running_instances_count(self, running_instances_count):
        print
        print "Started Test: Check Running Instances Count"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Verifying that Running Instances Count on Dashboard is "+running_instances_count
        self.verify_text_displayed_by_css("div.status-readout > span",running_instances_count)
        print
        print "Finished Test: Check Running Instances Count"
        print
        return 0

if __name__ == "__main__":
    unittest.main()



