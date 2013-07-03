from se34euca.lib.EucaUITestLib_Base import *

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
        self.click_element_by_id("instances-check-all")
        self.click_element_by_id("more-actions-instances")
        self.click_element_by_link_text("Terminate")
        self.click_element_by_id("btn-instances-terminate-terminate")
        print
        print "Finished Test: Terminate Instance All"
        print
        return 0


if __name__ == "__main__":
    unittest.main()



