from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Volume(EucaUITestLib_Base):

    def test_ui_gotopage_volumes(self):
	print
	print "Started Test: GotoPage Volumes"
	self.click_element_by_id("euca-logo")
	print
	print "Test: Received the Page Title -> " + self.driver.title
	self.click_element_by_id("dashboard-storage-volume")
	print
	print "Test: Clicked the GoToPage Button"
	self.verify_element_by_id("table-volumes-new")
	print
	print "Finished Test: GotoPage Volumes"
	print 
	return 0

    def test_ui_create_volume(self):
	print
	print "Started Test: Create Volume"
	print
	print "Test: Go to the Page Volume"
	self.click_element_by_id("dashboard-storage-volume")
	print
	print "Test: Create New Volume"
	self.click_element_by_id("table-volumes-new")
	self.verify_element_by_id("volume-size")
	try:
            self.driver.find_element_by_id("volume-size").clear()
            self.driver.find_element_by_id("volume-size").send_keys("2")
	except:
	    print "Failed Test: Create New Volume"
            raise
            return 1
	self.click_element_by_id("btn-volumes-delete-delete")
	print
	print "Finished: Create New Volume"
	print
	return 0

    def test_ui_delete_volume(self):
	print
	print "Started Test: Delete Volume"
	print
	print "Test: Go to the Page Volume"
	self.click_element_by_id("dashboard-storage-volume")
	self.click_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]")
	print
	print "Test: Delete Volume"
	self.click_element_by_id("more-actions-volumes")
	self.click_element_by_link_text("Delete")
	self.click_element_by_id("btn-volumes-delete-delete")
	print
	print "Finished: Delete Volume"
	print
	return 0

    def test_ui_delete_volume_all(self):
	print
	print "Started Test: Delete Volume All"
        print
	print "Test: Go to the Page Volume"
	self.click_element_by_id("dashboard-storage-volume")
	self.click_element_by_id("volumes-check-all")
	print
	print "Test: Delete Volume"
	self.click_element_by_id("more-actions-volumes")
	self.click_element_by_link_text("Delete")
	self.click_element_by_id("btn-volumes-delete-delete")
	print
	print "Finished: Delete Volume All"
	print
	return 0

    def test_ui_create_snapshot_from_volume(self):
	print
	print "Started Test: Create Snapshot From Volume"
	self.verify_element_by_link_text("Launch new instance")
	print
	print "Test: Go to the Page Volume"
	self.click_element_by_css_selector("#dashboard-storage-volume > span")
	self.verify_element_by_id("table-volumes-new")
	self.click_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]")
	print
	print "Test: Create Snapshot From Volume"
        self.click_element_by_id("more-actions-volumes")
        self.click_element_by_link_text("Create snapshot from volume")
	try:
            self.driver.find_element_by_id("snapshot-create-description").clear()
            self.driver.find_element_by_id("snapshot-create-description").send_keys("snapshot by selenium script")
	except:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
	self.click_element_by_id("btn-volumes-delete-delete")
	print
	print "Finished: Create Snapshot From Volume"   
	print
	return 0


if __name__ == "__main__":
    unittest.main()



