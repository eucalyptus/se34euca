from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Utility(EucaUITestLib_Base):

    def test_ui_change_password(self, new_password):
        '''
        old password is saved as password_old

        '''

        self.password_old=self.password
        print self.username
        print self.accountname
        print self.password
        self.click_element_by_link_text(self.username+"@"+self.accountname)
        self.click_element_by_link_text("Change password")
        self.set_keys_by_xpath("(//input[@id='current'])[2]",self.password)
        self.set_keys_by_xpath("(//input[@id='newpwd'])[2]", new_password)
        self.set_keys_by_xpath("(//input[@id='confirmpwd'])[2]",new_password)
        time.sleep(1)
        self.click_element_by_id("change-pwd")
        try_again = 0
        while (self.is_element_present(By.LINK_TEXT, "There was a problem with your request")) and try_again < 3:
            print "Try " + `try_again` + " to change password"
            try_again +=1
            self.click_element_by_link_text("Close")
            self.password_old=self.password
            self.click_element_by_link_text(self.username+"@"+self.accountname)
            self.click_element_by_link_text("Change password")
            self.set_keys_by_xpath("(//input[@id='current'])[2]",self.password)
            self.set_keys_by_xpath("(//input[@id='newpwd'])[2]",new_password)
            self.set_keys_by_xpath("(//input[@id='confirmpwd'])[2]",new_password)
            time.sleep(1)
            self.click_element_by_id("change-pwd")

        self.password = new_password
        time.sleep(1)
        print "Test: old pwd: " + self.password_old
        print "Test: new pwd: " + self.password




if __name__ == "__main__":
     unittest.main()
