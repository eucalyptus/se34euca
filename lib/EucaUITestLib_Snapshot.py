from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Snapshot(EucaUITestLib_Base):

    def test_ui_delete_snapshot(self):
	print "Started Test: Delete Snapshot"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
	print "Test: Go to the Page Snapshot"
        driver.find_element_by_css_selector("#dashboard-storage-snapshot > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-snapshots-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
        driver.find_element_by_css_selector("td.checkbox-cell.sorting_1 > input[type=\"checkbox\"]").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "more-actions-snapshots"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
        driver.find_element_by_id("more-actions-snapshots").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
	print "Test: Delete Snapshot"
        driver.find_element_by_link_text("Delete").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "btn-volumes-delete-delete"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
	try:
            driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Delete Snapshot"
            raise
            return 1
	print "Finished: Delete Snapshot" 
	print
	return 0

    def test_ui_create_volume_from_snapshot(self):
	print
	print "Started Test: Create Volume From Snapshot"
        driver = self.driver
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



