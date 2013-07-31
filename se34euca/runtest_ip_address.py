#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_ip_address import testcase_ip_address

class IpAddress(se34euca.TestRunner):
    # default test case, if no provided
    testcase = "allocate_ip_address"

    # class to use for running tests
    testclass = testcase_ip_address

if __name__ == "__main__":
    IpAddress().start_test()
