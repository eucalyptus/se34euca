#!/usr/bin/python
from se34euca.lib.EucaUITestLib_Base import *
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from eucaops import Eucaops

import unittest, time, re

from eutester.sshconnection import SshConnection

ssh = SshConnection(host='10.111.5.62', password='foobar', verbose=True)
print ssh.sys('ls /etc')


#tester = Eucaops(config_file='62.conf', password='foobar')

