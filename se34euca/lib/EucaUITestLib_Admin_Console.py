from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Admin_Console(EucaUITestLib_Base):

    def test_ui_create_accounts_and_users_via_admin_console(self):
        print
        print "Started Test: Create Account and Users via Admin Console"
        self.click_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div[2]")
        self.click_element_by_link_text("New account")
        self.set_keys_by_css_selector("input.gwt-TextBox","aaacct")
        self.set_keys_by_css_selector("input.gwt-PasswordTextBox","foobar")
        self.set_keys_by_xpath("(//input[@type='password'])[2]","foobar")
        self.click_element_by_link_text("OK")
        self.click_element_by_css_selector("th.GCOJGB3BCH.GCOJGB3BAI")
        self.click_element_by_xpath("//td[2]/div")
        self.click_element_by_link_text("New users")
        self.set_keys_by_xpath("(//input[@type='text'])[4]","aalice; abob; aclint")
        self.set_keys_by_xpath("(//input[@type='text'])[5]","/a")
        self.click_element_by_link_text("OK")
        self.click_element_by_xpath("//div/div[3]/div/div/div[2]")
        self.click_element_by_xpath("//tr[2]/td[2]/div")
        self.click_element_by_link_text("Add policy")
        self.set_keys_by_xpath("(//input[@type='text'])[9]","AllowAll")
        self.set_keys_by_css_selector("textarea.gwt-TextArea",'{\n "Statement": [\n  {\n  "Action": "ec2:*",\n  "Effect": "Allow",\n  "Resource": "*"\n  },\n  {\n "Action": "s3:*",\n "Effect": "Allow",\n "Resource": "*"\n }\n ]\n }')
        self.click_element_by_link_text("OK")
        self.click_element_by_xpath("(//div[@onclick=''])[5]")
        time.sleep(3)
        self.click_element_by_css_selector("th.GCOJGB3BCH.GCOJGB3BAI")
        time.sleep(3)
        self.click_element_by_xpath("//div[3]/div/div/div/table/tbody/tr/td[2]")
        time.sleep(3)
        self.click_element_by_link_text("Delete accounts")
        time.sleep(3)
        self.click_element_by_link_text("OK")
        print
        print "Finished Test: Create Accounts and Users via Admin Console"
        print
        return 0

    def test_ui_create_then_delete_accounts_via_admin_console(self,number_of_accounts):
        print
        print "Started Test: Create then Delete Account via Admin Console"
        for i in range (1, number_of_accounts):
            print
            print "Test: Creating Account No" + str(i)
            self.click_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div[2]")
            self.click_element_by_link_text("New account")
            time.sleep(3)
            self.set_keys_by_css_selector("input.gwt-TextBox","aaacct"+str(i))
            time.sleep(3)
            self.set_keys_by_css_selector("input.gwt-PasswordTextBox","foobar")
            self.set_keys_by_xpath("(//input[@type='password'])[2]","foobar")
            self.click_element_by_link_text("OK")
        time.sleep(10)
        self.click_element_by_css_selector("th.GCOJGB3BCH.GCOJGB3BAI")
        for i in range (1, number_of_accounts):
            print "Test: Deleting Account No" + str(i)
            time.sleep(3)
            time.sleep(3)
            self.click_element_by_xpath("//div[3]/div/div/div/table/tbody/tr/td[2]")
            time.sleep(3)
            self.click_element_by_link_text("Delete accounts")
            time.sleep(3)
            self.click_element_by_link_text("OK")
            print
        print "Finished Test: Create then Delete Account via Admin Console"
        print
        return 0