#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_security_group import testcase_security_group


class SecurityGroup(se34euca.TestRunner):
    testcase = "create_empty_security_group"
    testclass = testcase_security_group


if __name__ == "__main__":
    SecurityGroup().start_test()
