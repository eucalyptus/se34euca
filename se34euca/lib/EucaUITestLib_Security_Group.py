import time

from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_Security_Group(EucaUITestLib_Base):
    def test_ui_gotopage_security_groups(self):
        print
        print "Started Test: GotoPage Security Groups"
        print
        self.click_element_by_id("euca-logo")
        print
        print "Test: Received the Page Title -> " + self.driver.title
        self.click_element_by_id("dashboard-netsec-sgroup")
        print
        print "Test: Clicked the GoToPage Button"
        self.verify_element_by_id("table-sgroups-new")
        print
        print "Finished Test: GotoPage Security Groups"
        print
        return 0

    def test_ui_create_security_group(self, security_group_name, security_group_description):
        print
        print "Started Test: Create Security Group"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Security Group"
        self.click_element_by_id("resource-menu-netsec")
        self.click_element_by_id("resource-menuitem-sgroup")
        print "Click 'Create new security group' button"
        self.click_element_by_id("table-sgroups-new")
        print
        print "Test: Create Security Group"
        self.set_keys_by_id("sgroup-name", security_group_name)
        self.set_keys_by_id("sgroup-description", security_group_description)
        print "Click: LINK_TEXT -> Rules"
        self.click_element_by_link_text("Rules")
        print "Select: ID -> sgroup-templete, TEXT -> SSH (TCP port 22, for terminal access)"
        self.select_text_by_id("sgroup-template", "SSH (TCP port 22, for terminal access)")
        self.set_keys_by_id("allow-ip", "0.0.0.0/0")
        print "Click: ID -> sgroup-add-rule"
        self.click_element_by_id("sgroup-add-rule")
        self.verify_element_by_id("sgroup-rule-number-0")
        print "Rule 0: " + self.get_text_by_css_selector("ul.sg-rules-list > li")
        print "Select: ID -> sgroup-templete, TEXT -> HTTP (TCP port 80, for web servers)"
        self.select_text_by_id("sgroup-template", "HTTP (TCP port 80, for web servers)")
        self.set_keys_by_id("allow-ip", "0.0.0.0/0")
        print "Click: ID -> sgroup-add-rule"
        self.click_element_by_id("sgroup-add-rule")
        self.verify_element_by_id("sgroup-rule-number-1")
        print "Rule 1: " + self.get_text_by_xpath("//div[@id='sgroup-rules-list']/ul/li[2]")
        print "Select: ID -> sgroup-templete, TEXT -> Custom ICMP"
        Select(self.driver.find_element_by_id("sgroup-template")).select_by_visible_text("Custom ICMP")
        print "Select: ID -> sgroup-type. TEXT -> All"
        self.select_text_by_id("sgroup-type", "All")
        self.set_keys_by_id("allow-ip", "0.0.0.0/0")
        print "Click: ID -> sgroup-add-rule"
        self.click_element_by_id("sgroup-add-rule")
        self.verify_element_by_id("sgroup-rule-number-2")
        print "Rule 2: " + self.get_text_by_xpath("//div[@id='sgroup-rules-list']/ul/li[3]")
        self.click_element_by_id("sgroup-add-btn")
        print
        print "Finished: Create Security Group"
        print
        return 0


    def test_ui_create_empty_security_group(self):
        print
        print "Started Test: Create Empty Security Group"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Security Group"
        self.click_element_by_css_selector("#dashboard-netsec-sgroup > span")
        self.click_element_by_id("table-sgroups-new")
        print
        print "Test: Create Security Group"
        self.set_keys_by_id("sgroup-name", "mywebservice-01")
        self.set_keys_by_id("sgroup-description", "test")
        self.click_element_by_id("sgroup-add-btn")
        print
        print "Finished: Create Empty Security Group"
        print
        return 0

    def test_ui_add_rules_to_security_group(self, group_description):
        '''
        Adds rules to empty group with prescribed description
        '''
        print
        print "Started Test: Add Rules to a Security Group"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Security Group"
        self.click_element_by_link_text("Network & Security")
        self.click_element_by_link_text("Security Groups")
        print "Test: Checkbox the security group"

        #checkbox is indexed by s.group id
        #need method to find element in table or replace with eutester call
        #present method checks first and second row

        if (self.get_text_by_xpath("//table[@id='sgroups']/tbody[2]/tr/td[3]") == group_description):
            self.click_element_by_xpath("//table[@id='sgroups']/tbody[2]/tr/td[3]")

        elif (self.get_text_by_xpath("//table[@id='sgroups']/tbody/tr/td[3]") == group_description):
            self.click_element_by_xpath("//table[@id='sgroups']/tbody/tr/td[3]")

        print "Test: Add rules"
        self.click_element_by_id("more-actions-sgroups")
        self.click_element_by_link_text("Manage rules")
        print
        print "Adding TCP rule"
        print
        self.select_text_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > div.form-row > #sgroup-template", "Custom TCP")
        self.set_keys_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.form-row > #sgroup-port-option > #sgroup-ports",
            "0")
        self.set_keys_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.form-row.sg-inline-options > #allow-ip",
            "0.0.0.0/0")
        self.click_element_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.section-button-bar > #sgroup-add-rule")
        print
        print "Adding ICMP rule"
        print
        self.select_text_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > div.form-row > #sgroup-template", "Custom ICMP")
        self.set_keys_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.form-row.sg-inline-options > #allow-ip",
            "0.0.0.0/0")
        self.click_element_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.section-button-bar > #sgroup-add-rule")
        print
        print "Adding HTTP rule"
        print
        self.select_text_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > div.form-row > #sgroup-template",
            "HTTP (TCP port 80, for web servers)")
        self.set_keys_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.form-row.sg-inline-options > #allow-ip",
            "0.0.0.0/0")
        self.click_element_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.section-button-bar > #sgroup-add-rule")
        print
        print "Adding SSH rule"
        time.sleep(10)
        print
        self.select_text_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > div.form-row > #sgroup-template",
            "SSH (TCP port 22, for terminal access)")
        time.sleep(3)
        self.set_keys_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.form-row > #sgroup-port-option > #sgroup-ports",
            "0")
        time.sleep(3)
        self.click_element_by_css_selector(
            "div.content-sections-wrapper > div.rules.content-section > #sgroup-more-rules > div.form-row.sg-inline-options > #sgroup-ip-check")
        time.sleep(3)
        self.click_element_by_id("sgroup-add-btn")
        print
        print "Finished: Add Rules to Security Group"
        print
        return 0


    def test_ui_delete_security_group(self):
        print
        print "Started Test: Delete Security Group"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Security Group"
        self.click_element_by_css_selector("#dashboard-netsec-sgroup > span")
        self.verify_element_by_id("table-sgroups-new")
        self.click_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]")
        self.click_element_by_id("more-actions-sgroups")
        print
        print "Test: Delete Security Group"
        self.click_element_by_link_text("Delete")
        self.click_element_by_id("btn-sgroups-delete-delete")
        print
        print "Finished: Delete Security Group"
        print
        return 0

    def test_ui_delete_security_group_all(self):
        print
        print "Started Test: Delete Security Group All"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Security Group"
        self.click_element_by_id("resource-menu-netsec")
        self.click_element_by_id("resource-menuitem-sgroup")
        #self.click_element_by_css_selector("#dashboard-netsec-sgroup > span")
        self.click_element_by_id("sgroups-check-all")
        self.click_element_by_id("more-actions-sgroups")
        print
        print "Test: Delete Security Group All"
        self.click_element_by_link_text("Delete")
        self.click_element_by_id("btn-sgroups-delete-delete")
        print
        print "Finished: Delete Security Group All"
        print
        return 0

    def test_ui_check_security_group_sort(self):
        print
        print "Started Test: Test Table sorting with Security Groups"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Security Group"
        self.click_element_by_css_selector("#dashboard-netsec-sgroup > span")
        print
        print "Test: verify default is first group"
        self.verify_text_displayed_by_xpath("//table[@id='sgroups']/tbody[1]/tr/td[2]/a", "default")
        self.click_element_by_id("columnheader-1")
        print
        print "Test: verify default is second group"
        self.verify_text_displayed_by_xpath("//table[@id='sgroups']/tbody[2]/tr/td[2]/a", "default")
        self.click_element_by_id("columnheader-1")
        print
        print "Test: verify default is first group"
        self.verify_text_displayed_by_xpath("//table[@id='sgroups']/tbody[1]/tr/td[2]/a", "default")
        print
        print "Finished Test: Test Table sorting with Security Groups"
        print
        return 0

    def test_ui_check_security_group_count(self, sg_count):
        print
        print "Started Test: Check Security Group Count"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Verifying that Security Group Count on Dashboard is " + sg_count
        self.verify_text_displayed_by_css("#dashboard-netsec-sgroup > span", sg_count)
        print
        print "Finished Test: Check Security Group Count"
        print
        return 0


if __name__ == "__main__":
    unittest.main()



