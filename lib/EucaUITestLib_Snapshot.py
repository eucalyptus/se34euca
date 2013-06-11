from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Snapshot(EucaUITestLib_Base):

    def test_ui_delete_snapshot(self):
	print
	print "Started Test: Delete Snapshot"
	self.verify_element_by_link_text("Launch new instance")
	print
	print "Test: Go to the Page Snapshot"
	self.click_element_by_css_selector("#dashboard-storage-snapshot > span")
	self.verify_element_by_id("table-snapshots-new")
	self.click_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]")
	self.click_element_by_id("more-actions-snapshots")
	print
	print "Test: Delete Snapshot"
	self.click_element_by_link_text("Delete")
        self.click_element_by_id("btn-volumes-delete-delete")
	print
	print "Finished: Delete Snapshot" 
	print
	return 0

    def test_ui_create_volume_from_snapshot(self):
	print
	print "Started Test: Create Volume From Snapshot"
	self.verify_element_by_link_text("Launch new instance")
	print
	print "Test: Go to the Page Snapshot"
	self.click_element_by_css_selector("#dashboard-storage-snapshot > span")
	self.verify_element_by_id("table-snapshots-new")
	self.click_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]")
	print
	print "Test: Create Volume From Snapshot"
	self.click_element_by_id("more-actions-snapshots")
	self.click_element_by_link_text("Create volume from snapshot")
	self.click_element_by_id("btn-volumes-delete-delete")
	print
	print "Finished: Create Volume From Snapshot"
	print
	return 0

if __name__ == "__main__":
    unittest.main()



