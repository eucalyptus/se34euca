from se34euca.lib.EucaUITestLib_Base import *

class EucaUITestLib_Volume(EucaUITestLib_Base):

    def test_ui_gotopage_volumes(self):
	print "Started Test: GotoPage Volumes"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "euca-logo"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Volumes"
            raise
	    return 1
        driver.find_element_by_id("euca-logo").click()
	print "Test: Received the Page Title -> " + driver.title
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Volumes"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "dashboard-storage-volume"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("dashboard-storage-volume").click()
	print "Test: Clicked the GoToPage Button"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: GotoPage Volumes"
            raise
	    return 1
        try: self.assertTrue(self.is_element_present(By.ID, "table-volumes-new"))
        except AssertionError as e: self.verificationErrors.append(str(e))
	print "Finished Test: GotoPage Volumes"
	print 
	return 0

    def test_ui_create_volume(self):
	print "Started Test: Create Volume"
        driver = self.driver
	print "Test: Go to the Page Volume"
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Volume"
            raise
            return 1
        driver.find_element_by_id("dashboard-storage-volume").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Volume"
            raise
            return 1
	print "Test: Create New Volume"
        driver.find_element_by_id("table-volumes-new").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "volume-size"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create New Volume"
            raise
            return 1
	try:
            driver.find_element_by_id("volume-size").clear()
            driver.find_element_by_id("volume-size").send_keys("2")
            ##driver.find_element_by_id("volumes-add-btn").click()
            driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Create New Volume"
            raise
            return 1
	print "Finished: Create New Volume"
	print
	return 0

    def test_ui_delete_volume(self):
	print "Started Test: Delete Volume"
	driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	print "Test: Go to the Page Volume"
	driver.find_element_by_id("dashboard-storage-volume").click()
	driver.find_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.ID, "more-actions-volumes"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	print "Test: Delete Volume"
	driver.find_element_by_id("more-actions-volumes").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.LINK_TEXT, "Delete"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	driver.find_element_by_link_text("Delete").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.ID, "btn-volumes-delete-delete"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	try:
	    driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Delete Volume"
            raise
            return 1
	print "Finished: Delete Volume"
	print
	return 0

    def test_ui_delete_volume_all(self):
	print "Started Test: Delete Volume All"
	driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "dashboard-storage-volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	print "Test: Go to the Page Volume"
	driver.find_element_by_id("dashboard-storage-volume").click()
	for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "volumes-check-all"): break
            except: pass
            time.sleep(1)
        else:
            print "Failed Test: Delete Volume All"
            raise
            return 1
	driver.find_element_by_id("volumes-check-all").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.ID, "more-actions-volumes"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	print "Test: Delete Volume"
	driver.find_element_by_id("more-actions-volumes").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.LINK_TEXT, "Delete"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	driver.find_element_by_link_text("Delete").click()
	for i in range(self.retry):
	    try:
		if self.is_element_present(By.ID, "btn-volumes-delete-delete"): break
	    except: pass
	    time.sleep(1)
	else:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	try:
	    driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Delete Volume All"
            raise
            return 1
	print "Finished: Delete Volume All"
	print
	return 0

    def test_ui_create_snapshot_from_volume(self):
	print "Started Test: Create Snapshot From Volume"
        driver = self.driver
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Launch new instance"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
	print "Test: Go to the Page Volume"
        driver.find_element_by_css_selector("#dashboard-storage-volume > span").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "table-volumes-new"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
        driver.find_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.ID, "more-actions-volumes"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
	print "Test: Create Snapshot From Volume"
        driver.find_element_by_id("more-actions-volumes").click()
        for i in range(self.retry):
            try:
                if self.is_element_present(By.LINK_TEXT, "Create snapshot from volume"): break
            except: pass
            time.sleep(1)
        else:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
        driver.find_element_by_link_text("Create snapshot from volume").click()
	try:
            driver.find_element_by_id("snapshot-create-description").clear()
            driver.find_element_by_id("snapshot-create-description").send_keys("snapshot by selenium script")
            driver.find_element_by_id("btn-volumes-delete-delete").click()
	except:
	    print "Failed Test: Create Snapshot From Volume"
            raise
            return 1
	print "Finished: Create Snapshot From Volume"   
	print
	return 0


if __name__ == "__main__":
    unittest.main()



