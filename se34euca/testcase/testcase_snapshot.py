from se34euca.testcase.testcase_base import *


class testcase_snapshot(testcase_base):
    def delete_snapshot(self):
        print "=== runTest: Delete Snapshot ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.snapshot.test_ui_delete_snapshot()
        self.eucaUITester.base.test_ui_logout()

    def delete_all_snapshots(self):
        print "=== runTest: Delete Snapshot ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.snapshot.test_ui_delete_all_snapshots()
        self.eucaUITester.base.test_ui_logout()


    def create_volume_from_snapshot(self):
        print "=== runTest: Create Volume From Snapshot ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.snapshot.test_ui_create_volume_from_snapshot()
        self.eucaUITester.base.test_ui_logout()

    def register_snapshot_as_image(self):
        print "=== runTest: Register Snapshot as Image ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.snapshot.test_ui_register_snapshot_as_image("myimage")
        self.eucaUITester.base.test_ui_logout()

    def populate_registered_images(self):
        sleep_time = 10
        image_count = 70
        imagename_prefix = "zzz-pop-image"
        self.eucaUITester.base.test_ui_login()
        for x in range(0, image_count):
          index = "%03d" % (x)
          imagename = imagename_prefix + "-" + index
          self.eucaUITester.snapshot.test_ui_register_snapshot_as_image(str(imagename))
          time.sleep(sleep_time)
        self.eucaUITester.base.test_ui_logout()


if __name__ == "__main__":
    unittest.main()



