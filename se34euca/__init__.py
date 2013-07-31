
import unittest, time, re
from optparse import OptionParser
from unittest import TestResult

class TestRunner(object):
    testcase = None
    testclass = None

    def __init__(self):
        self.selenium_server_ip = "localhost"
        self.selenium_server_port = "4444"
        self.ui_ip = "localhost"
        self.port = "8888"
        self.accountname = "eucalyptus"
        self.username = "admin"
        self.password = "password"
        self.testcases = ""
        for key in self.testclass.__dict__:
            if hasattr(self.testclass.__dict__[key], "__call__"):
                self.testcases += key+' '
	
        parser = OptionParser()
        parser.add_option("-s", "--sel_server_ip", dest="selenium_server_ip", help="selenium server ip")
        parser.add_option("-r", "--sel_server_port", dest="selenium_server_port", help="selenium server port")
        parser.add_option("-i", "--ip", dest="ui_ip", help="ui ip")
        parser.add_option("-p", "--port", dest="port", help="port")
        parser.add_option("-a", "--account", dest="accountname", help="accountname")
        parser.add_option("-u", "--user", dest="username", help="username")
        parser.add_option("-w", "--password", dest="password", help="password")
        parser.add_option("-t", "--testcase", dest="testcase", help="testcase: "+self.testcases)
        (options, args) = parser.parse_args()

        if options.selenium_server_ip is not None:
            self.selenium_server_ip = options.selenium_server_ip

        if options.selenium_server_port is not None:
            self.selenium_server_port = options.selenium_server_port

        if options.ui_ip is not None:
            self.ui_ip = options.ui_ip

        if options.port is not None:
            self.port = options.port

        if options.accountname is not None:
            self.accountname = options.accountname

        if options.username is not None:
            self.username = options.username

        if options.password is not None:
            self.password = options.password

        if options.testcase is not None:
            self.testcase = options.testcase

    def start_test(self):
        print "=============================="
        print "TEST "+self.testclass.__name__
        print "=============================="

        testresult = TestResult()
        ui = self.testclass(self.testcase)

        print
        print "### SETUP"
        print "TESTCASE: " + self.testcase
        print
        ui.setSeleniumServerInfo(self.selenium_server_ip, self.selenium_server_port)
        ui.setUIInfo(self.ui_ip, self.port)
        ui.setUserInfo(self.accountname, self.username, self.password)

        print
        print "### TEST"
        ui.run(testresult)

        print
        print "### RESULT"
        print "Failures: "  + str(len(testresult.failures))
        if len(testresult.failures) > 0:
            print testresult.failures
        print "Errors: " + str(len(testresult.errors))
        if len(testresult.errors) > 0:
            print testresult.errors

        print
        print "=============================="
        print "END OF TEST : "+self.testclass.__name__
        print "=============================="
        exit(len(testresult.failures) + len(testresult.errors))

