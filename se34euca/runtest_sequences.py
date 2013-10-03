#!/usr/bin/python

import sys
sys.path.append('..')

import se34euca
from se34euca.testcase.testcase_sequences import testcase_sequences


class Sequences(se34euca.TestRunner):
    testcase = "instance_sequences"
    testclass = testcase_sequences


if __name__ == "__main__":
    Sequences().start_test()
