#!/usr/bin/python

import unittest, time, re
from optparse import OptionParser
from unittest import TestResult
from se34euca.testcase.testcase_instance import *

def main():

    testcase = "launch_instance_basic"

    selenium_server_ip = "localhost"
    selenium_server_port = "4444"
    ui_ip = "localhost"
    port = "8888"
    accountname = "eucalyptus"
    username = "admin"
    password = "password"

    print "=============================="
    print "TEST INSTANCE"
    print "=============================="

    parser = OptionParser()
    parser.add_option("-s", "--sel_server_ip", dest="selenium_server_ip", help="selenium server ip")
    parser.add_option("-r", "--sel_server_port", dest="selenium_server_port", help="selenium server port")
    parser.add_option("-i", "--ip", dest="ui_ip", help="ui ip")
    parser.add_option("-p", "--port", dest="port", help="port")
    parser.add_option("-a", "--account", dest="accountname", help="accountname")
    parser.add_option("-u", "--user", dest="username", help="username")
    parser.add_option("-w", "--password", dest="password", help="password")
    parser.add_option("-t", "--testcase", dest="testcase", help="testcase: launch_instance_basic, launch_instance_name_testinstance, terminate_instance_basic, terminate_instance_all")
    (options, args) = parser.parse_args()

    if options.selenium_server_ip is not None:
        selenium_server_ip = options.selenium_server_ip

    if options.selenium_server_port is not None:
        selenium_server_port = options.selenium_server_port

    if options.ui_ip is not None:
        ui_ip = options.ui_ip

    if options.port is not None:
        port = options.port

    if options.accountname is not None:
        accountname = options.accountname

    if options.username is not None:
        username = options.username

    if options.password is not None:
        password = options.password

    if options.testcase is not None:
        testcase = options.testcase

    testresult = TestResult()
    ui = testcase_instance(testcase)

    print
    print "### SETUP"
    print "TESTCASE: " + testcase
    print
    ui.setSeleniumServerInfo(selenium_server_ip, selenium_server_port)
    ui.setUIInfo(ui_ip, port)
    ui.setUserInfo(accountname, username, password)

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
    print "END OF TEST : INSTANCE"
    print "=============================="
    exit(len(testresult.failures) + len(testresult.errors))

if __name__ == "__main__":
    main()
    exit
