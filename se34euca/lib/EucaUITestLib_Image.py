from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_Image(EucaUITestLib_Base):

    def test_ui_gotopage_images(self):
        print
        print "Started Test: GotoPage Images"
        self.click_element_by_link_text("Dashboard")
        print "Test: Received the Page Title -> " + self.driver.title
        self.click_element_by_link_text("Images")
        print
        print "Test: Clicked the GotoPage Images"
        self.verify_element_by_link_text("More actions")
        print
        print "Finished Test: GotoPage Images"
        print
        return 0

    def test_ui_check_image_count(self, image_count):
        print
        print "Started Test: Check Image Count"
        print
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Images")
        time.sleep(3)
        print "Verifying that Image Count is " + image_count
        image_count_str = str(image_count) + " images found."
        self.verify_text_displayed_by_css(".euca-table-size > span:nth-child(3)", image_count_str);
        print
        print "Finished Test: Check Image Count"
        print
        return 0

    def test_ui_click_image_given_emi_name(self, emi_name):
        print
        print "Started IMAGE LANDING PAGE OPERATION: Click Image Given EMI Name"
        print "EMI Name: " + emi_name
        print
        print "Sort the Images by ROOT DEVICE in ASCENDING ORDER"
        self.click_element_by_id("columnheader-6")
        time.sleep(1)
        self.click_element_by_id("columnheader-6")
        time.sleep(3)
        print "Check the EMI Name of the Image on the First Row"
        self.verify_text_displayed_by_css("#images  >  tbody > tr > td:nth-child(3)", emi_name);
        self.click_element_by_css_selector("#images  >  tbody > tr > td:nth-child(3)")
        print
        print "Finished IMAGE LANDING PAGE OPERATION: Click Image Given EMI Name"
        print
        return 0

    def test_ui_get_image_id_given_image_name(self, image_name):
        print
        print "Started IMAGE LANDING PAGE OPERATION: Return Image ID Given Image ID"
        print "Image Name: " + image_name
        print
        self.click_element_by_link_text(image_name)
        time.sleep(3)
        image_id = "NULL"
        image_id = self.get_text_by_css_selector("ul.image-expanded:nth-child(2) > li:nth-child(3) > div:nth-child(2)")
        print
        print "Finsihed IMAGE LANDING PAGE OPERATION: Return Image ID Given Image ID"
        print "Returning Image ID: " + image_id
        print
        return image_id

    def test_ui_tag_image_given_emi_name(self, emi_name, key, value):
        print
        print "Started Test: Tag Image Given EMI Name"
        print
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Images")
        time.sleep(3)
        self.test_ui_click_image_given_emi_name(emi_name)
        self.click_element_by_link_text("More actions")
        self.click_element_by_link_text("Manage tags")
        time.sleep(3)
        self.set_keys_by_id("inputbox_newtag_name", key)
        self.set_keys_by_id("inputbox_newtag_value", value)
        time.sleep(1)
        self.click_element_by_id("button-dialog-edittags-save")
        print
        print "Finished Test: Tag Image Given EMI Name"
        print
        return 0


    def test_ui_verify_emi_name_tag_given_image_name(self, emi_name, image_name):
        print
        print "Started Test: Verify EMI Name Given Image Name"
        print
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Images")
        time.sleep(3)
        self.click_element_by_link_text(image_name)
        time.sleep(3)
        self.verify_text_displayed_by_css("ul.image-expanded:nth-child(2) > li:nth-child(2) > div:nth-child(2)", emi_name)
        print
        print "Finished Test: Verify EMI Name Given Image Name"
        print


if __name__ == "__main__":
    unittest.main()



