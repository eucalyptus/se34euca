from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Image(EucaUITestLib_Base):

    def test_ui_gotopage_images(self):
	print "Started Test: GotoPage Images"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Images"
            raise
	    return 1
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Images"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Images"
            raise
	    return 1
        driver.find_element_by_link_text("Images").click()
	print "Test: Clicked the GotoPage Images"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "More actions"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Images"
            raise
	    return 1
	try:
	    driver.find_element_by_link_text("More actions").click()
	except:
	    print "Failed Test: GotoPage Images"
	    return 1
	print "Finished Test: GotoPage Images"
	print 
	return 0

if __name__ == "__main__":
    unittest.main()



