from se34euca.lib.EucaUITestLib_Base import *
from se34euca.lib.EucaUITestLib_Image import *
from se34euca.lib.EucaUITestLib_Instance import *
from se34euca.lib.EucaUITestLib_IP_Address import *
from se34euca.lib.EucaUITestLib_Keypair import *
from se34euca.lib.EucaUITestLib_Security_Group import *
from se34euca.lib.EucaUITestLib_Snapshot import *
from se34euca.lib.EucaUITestLib_Volume import *

class EucaUITester():

    selenium_server_ip = "localhost"
    selenium_server_port = "4444"
    ui_ip = "localhost"
    port = "8888"
    accountname = "eucalyptus"
    username = "admin"
    password = "password"
    retry = 5

    def setSeleniumServerInfo(self, ip, port):
	self.selenium_server_ip = ip
	self.selenium_server_port = port
	print "SELENIUM SERVER IP: " + ip
	print "SELENIUM SERVER PORT: " + port
	print

    def setUIInfo(self, ip, port):
	self.ui_ip = ip
	self.port = port
	print "UI IP: " + ip
	print "PORT: " + port
	print

    def setUserInfo(self, accountname, username, password):
	self.accountname = accountname
	self.username = username
	self.password = password
	print "ACCOUNTNAME: " + accountname
	print "USERNAME: " + username
	print "PASSWORD: " + password
	print

    def setUp(self):
	print "========== Initializing EucaUITester =========="
	print
	self.base = EucaUITestLib_Base("NoOp")
	self.base.setSeleniumServerInfo(self.selenium_server_ip, self.selenium_server_port)
	self.base.setUIInfo(self.ui_ip, self.port)
	self.base.setUserInfo(self.accountname, self.username, self.password)
	self.base.setUp()
	self.image = EucaUITestLib_Image("NoOp")
	self.image.setSeleniumWebDriver(self.base.driver)
	self.instance = EucaUITestLib_Instance("NoOp")
	self.instance.setSeleniumWebDriver(self.base.driver)
	self.ip_address = EucaUITestLib_IP_Address("NoOp")
	self.ip_address.setSeleniumWebDriver(self.base.driver)
	self.keypair = EucaUITestLib_Keypair("NoOp")
	self.keypair.setSeleniumWebDriver(self.base.driver)
	self.security_group = EucaUITestLib_Security_Group("NoOp")
	self.security_group.setSeleniumWebDriver(self.base.driver)
	self.snapshot = EucaUITestLib_Snapshot("NoOp")
	self.snapshot.setSeleniumWebDriver(self.base.driver)
	self.volume = EucaUITestLib_Volume("NoOp")
	self.volume.setSeleniumWebDriver(self.base.driver)
	print

    def tearDown(self):
	print
	print "========== Terminating EucaUITester =========="
	print
	self.base.tearDown()
	print    



