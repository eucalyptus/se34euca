#!/usr/bin/python

import se34euca
from se34euca.testcase.testcase_view_page import testcase_view_page

class ViewPage(se34euca.TestRunner):
	testcase = "check_login_and_logout"
	testclass = testcase_view_page

if __name__ == "__main__":
    ViewPage().start_test()
