from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_Snapshot(EucaUITestLib_Base):
    def test_ui_delete_snapshot(self):
        print
        print "Started Test: Delete Snapshot"
        print
        print "Go to Dashboard"
        self.click_element_by_id("resource-menu-dashboard")
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
        self.click_element_by_id("button-dialog-deletesnapshot-delete")
        print
        print "Finished: Delete Snapshot"
        print
        return 0

    def test_ui_create_volume_from_snapshot(self):
        print
        print "Started Test: Create Volume From Snapshot"
        print
        print "Go to Dashboard"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Snapshot"
        self.click_element_by_css_selector("#dashboard-storage-snapshot > span")
        self.verify_element_by_id("table-snapshots-new")
        self.click_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]")
        print
        print "Test: Create Volume From Snapshot"
        self.click_element_by_id("more-actions-snapshots")
        self.click_element_by_link_text("Create volume from snapshot")
        time.sleep(1)
        self.verify_element_by_id("button-dialog-createvolume-save")
        self.click_element_by_id("button-dialog-createvolume-save")
        print
        print "Finished: Create Volume From Snapshot"
        print
        return 0

    def test_ui_delete_all_snapshots(self):
        print
        print "Started Test: Delete All Snapshots"
        print
        self.test_ui_gotopage_dashboard()
        print
        print "Test: Verify that snapshot count is not zero on Dashboard:"

        if self.verify_text_not_present_by_css("#dashboard-storage-snapshot > span", "0"):
            print "Test: Verified number of snapshots on dashboard is non-zero: "
            print
            num_snapshots = self.get_text_by_css_selector("#dashboard-storage-snapshot > span")
            print "Test: Snapshot count on Dashboard: " + num_snapshots
            print "Test: Go to the Page Snapshot"
            self.click_element_by_css_selector("#dashboard-storage-snapshot > span")
            self.verify_element_by_id("table-snapshots-new")
            self.click_element_by_id("snapshots-check-all")
            self.click_element_by_id("more-actions-snapshots")
            print
            print "Test: Delete All Snapshots"
            self.click_element_by_link_text("Delete")
            time.sleep(1)
            self.click_element_by_id("button-dialog-deletesnapshot-delete")
        else:
            print "Test: Snapshot count on Dashboard was zero"
            print
        print "Finished: Delete Snapshot"
        print
        return 0

    def test_ui_register_snapshot_as_image(self, image_name):
        print
        print "Started Test: Register Snapshot as image"
        print
        print "Go to Dashboard"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Test: Go to the Page Snapshot"
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Snapshots")
        self.verify_element_by_id("table-snapshots-new")
        print "Click the 'ready' status, to check-mark the snapshot"
        self.click_element_by_css_selector("div.table-row-status.status-completed")
        print "Click the More actions button"
        self.click_element_by_id("more-actions-snapshots")
        self.click_element_by_link_text("Register as image")
        print "Enter snapshot name"
        self.set_keys_by_id("snapshot-register-image-name", image_name)
        print "Click 'Save' button"
        self.click_element_by_id("button-dialog-registersnapshot-save")
        print
        print "Verifying image " + image_name + "is visible on the Images Landing Page"
        print
        print "Go to Images Landing Page"
        self.click_element_by_id("resource-menu-image")
        print "Wait for " + image_name + " to become visible"
        self.verify_element_by_xpath('//td[text()="' + image_name + '"]')
        print
        print "Finished Test: Register Snapshot as image"
        print


    def test_ui_check_snapshot_count(self, snapshot_count):
        print
        print "Started Test: Check Snapshot Count"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Verifying that Snapshot Count on Dashboard is " + snapshot_count
        self.verify_text_displayed_by_css("#dashboard-storage-snapshot > span", snapshot_count)
        print
        print "Finished Test: Check Snapshot Count"
        print
        return 0


if __name__ == "__main__":
    unittest.main()



