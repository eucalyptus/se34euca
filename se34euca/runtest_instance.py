#!/usr/bin/python

import sys
sys.path.append('..')

import se34euca
from se34euca.testcase.testcase_instance import testcase_instance


class Instance(se34euca.TestRunner):
    testcase = "launch_instance_basic"
    testclass = testcase_instance


if __name__ == "__main__":
    Instance().start_test()
