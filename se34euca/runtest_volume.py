#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_volume import testcase_volume


class Volume(se34euca.TestRunner):
    testcase = "create_volume_name_v"
    testclass = testcase_volume


if __name__ == "__main__":
    Volume().start_test()
