#!/usr/bin/env python

import time
import sys
import os

def run_cmd(command):
	print "CMD: " + command
	print
	os.system(command)
	print	
	time.sleep(1)
	return

def main():

	print
	print "===== INSTALLER FOR SE34EUCA ======"
	print

	cmd = "sudo apt-get -y update"
	run_cmd(cmd)

	cmd = "sudo apt-get -y install default-jre"
	run_cmd(cmd)

	cmd = "sudo apt-get -y install xvfb"
	run_cmd(cmd)
	
	cmd = "sudo apt-get -y install firefox"
	run_cmd(cmd)

	cmd = "sudo apt-get -y install python-pip"
	run_cmd(cmd)
	
	cmd = "pip install selenium"
	run_cmd(cmd)

	cmd = "mkdir -p /root/selenium-server"
        run_cmd(cmd)

	wget_cmd = "wget http://selenium.googlecode.com/files/selenium-server-standalone-2.25.0.jar"
	cmd = "cd /root/selenium-server/; " + wget_cmd
	run_cmd(cmd)

	cmd = "Xvfb :0 -ac 2> /dev/null &"
	run_cmd(cmd)

	run_selenium = "nohup java -jar selenium-server-standalone-2.25.0.jar &"
	cmd = "cd /root/selenium-server/; " + run_selenium
	run_cmd(cmd)

	print
	print "===== INSTALLER FOR SE34EUCA : DONE ====="
	print

	print "TO DO:"
	print
	print "*** BE SURE TO RUN BELOW COMMAND FIRST:"
	print
	print "export DISPLAY=:0"
	print 

	print "## TEST RUN ##"
	print
	print "./runtest_ip_address.py -i 192.168.51.86 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t allocate_two_ip_addresses"
	print 
	print "./runtest_ip_address.py -i 192.168.51.86 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t release_ip_address"
	print

if __name__ == "__main__":
    main()
    exit


