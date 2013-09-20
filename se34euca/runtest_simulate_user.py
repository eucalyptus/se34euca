#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_simulate_user import testcase_simulate_user


class SimulateUser(se34euca.TestRunner):
    testcase = "simulate_user_case_00"
    testclass = testcase_simulate_user


if __name__ == "__main__":
    SimulateUser().start_test()
    
