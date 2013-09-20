#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_admin_console import testcase_admin_console


class AdminConsole(se34euca.TestRunner):
    testcase = "create_accounts_and_users_via_admin_console"
    testclass = testcase_admin_console


if __name__ == "__main__":
    AdminConsole().start_test()
