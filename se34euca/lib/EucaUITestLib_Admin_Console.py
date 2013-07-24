from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Admin_Console(EucaUITestLib_Base):

    def test_ui_create_accounts_and_users_via_admin_console(self):
        print
        print "Started Test: Create Accounts and Users via Admin Console"
        self.click_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div[2]")
        self.click_element_by_link_text("New account")
        self.set_keys_by_css_selector("input.gwt-TextBox","aaacct")
        self.set_keys_by_css_selector("input.gwt-PasswordTextBox","foobar")
        self.set_keys_by_xpath("(//input[@type='password'])[2]","foobar")
        self.verify_element_by_link_text("OK")
        self.click_element_by_css_selector("th.GCOJGB3BCH.GCOJGB3BAI")
        self.click_element_by_xpath("//div[3]/div/div/div/table/tbody/tr/td[2]")
        self.click_element_by_link_text("Delete accounts")
        self.click_element_by_link_text("OK")
        print
        print "Finished Test: Create Accounts and Users via Admin Console"
        print
        return 0