#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_keypair import testcase_keypair


class Keypair(se34euca.TestRunner):
    testcase = "import_keypair"
    testclass = testcase_keypair


if __name__ == "__main__":
    Keypair().start_test()
