from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Image(EucaUITestLib_Base):

    def test_ui_gotopage_images(self):
        print
        print "Started Test: GotoPage Images"
        self.click_element_by_id("euca-logo")
        print "Test: Received the Page Title -> " + self.driver.title
        self.click_element_by_link_text("Images")
        print
        print "Test: Clicked the GotoPage Images"
        self.verify_element_by_link_text("More actions")
        print
        print "Finished Test: GotoPage Images"
        print
        return 0

if __name__ == "__main__":
    unittest.main()



