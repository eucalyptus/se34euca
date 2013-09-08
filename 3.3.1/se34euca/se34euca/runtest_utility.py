#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_utility import testcase_utility

class Utility(se34euca.TestRunner):
    testcase = "change_password"
    testclass = testcase_utility

if __name__ == "__main__":
    Utility().start_test()

