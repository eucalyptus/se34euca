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
        self.set_keys_by_id("volume-size", "2")
        self.click_element_by_id("btn-volumes-delete-delete")
        print
        print "Finished: Create New Volume"
        print
        return 0

    def test_ui_create_volume_name_v(self):
        print
        print "Started Test: Create Volume Named v"
        print
        print "Test: Go to the Page Volume"
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        print
        print "Test: Create New Volume"
        self.click_element_by_id("table-volumes-new")
        self.set_keys_by_id("volume-name","v")
        self.set_keys_by_id("volume-size", "1")
        self.click_element_by_id("btn-volumes-delete-delete")
        #Verifying on Volumes Landing Page that volume Named v was created
        print
        print "Verification"
        self.click_element_by_link_text(link_text="Dashboard")
        self.click_element_by_id("dashboard-storage-volume")
        self.verify_element_by_link_text("v")
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
        self.set_keys_by_id("snapshot-create-description", "Snapshot by Selenium Script")
        self.click_element_by_id("btn-volumes-delete-delete")
        print
        print "Finished: Create Snapshot From Volume"
        print
        return 0

    def test_ui_create_snapshot_from_volume_name_testsnap(self):
        print
        print "Started Test: Create Snapshot From Volume Name testsnap"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Volume"
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        self.verify_element_by_id("table-volumes-new")
        self.click_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]")
        print
        print "Test: Create Snapshot From Volume"
        self.click_element_by_id("more-actions-volumes")
        self.click_element_by_link_text("Create snapshot from volume")
        self.set_keys_by_id("snapshot-create-name", "testsnap")
        self.set_keys_by_id("snapshot-create-description", "Snapshot by Selenium Script")
        self.click_element_by_id("btn-volumes-delete-delete")
        #Verifying on Snapshots Landing Page that snapshot Named testsnap was created
        print
        print "Verification"
        self.click_element_by_link_text(link_text="Dashboard")
        self.click_element_by_id("dashboard-storage-snapshot")
        self.verify_element_by_link_text("testsnap")
        print

        print
        print "Finished: Create Snapshot From Volume"
        print
        return 0

    def test_ui_attach_volume(self):
        '''
        Attaches a volume to a running instance from Volumes Landing Page. Prerequisite: an instance named "testinstance"
        '''
        print "Started Test: Attach Volume"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Instances"
        self.click_element_by_link_text("Instances")
        self.click_element_by_css_selector("li.toggle-on > ul > li > a")
        self.click_element_by_link_text("testinstance")
        instance_id=self.get_text_by_xpath("//div[@id='tabs-1']/ul/li[2]/div[2]")
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        self.click_element_by_css_selector("div.table-row-status.status-available")
        self.click_element_by_id("more-actions-volumes")
        self.click_element_by_link_text("Attach to instance")
        self.set_keys_by_css_selector("#volumes-attach-dialog-wrapper > #volumes-attach-dialog > div.dialog-inner-content > div.form-row > #volume-attach-instance-id",instance_id)
        self.set_keys_by_id("volume-attach-device-name", "/dev/sdf")
        self.click_element_by_id("volumes-attach-dialog")
        self.click_element_by_id("btn-volumes-delete-delete")
        print
        print "Verification"
        self.click_element_by_link_text(link_text="Dashboard")
        self.click_element_by_id("dashboard-storage-snapshot")
        self.verify_element_by_link_text("testsnap")
        print




if __name__ == "__main__":
    unittest.main()



