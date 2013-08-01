#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_snapshot import testcase_snapshot

class Snapshot(se34euca.TestRunner):
    testcase = "delete_snapshot"
    testclass = testcase_snapshot

if __name__ == "__main__":
    Snapshot().start_test()
