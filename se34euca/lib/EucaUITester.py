from se34euca.lib.EucaUITestLib_Admin_Console import *
from se34euca.lib.EucaUITestLib_Image import *
from se34euca.lib.EucaUITestLib_Instance import *
from se34euca.lib.EucaUITestLib_IP_Address import *
from se34euca.lib.EucaUITestLib_Keypair import *
from se34euca.lib.EucaUITestLib_Security_Group import *
from se34euca.lib.EucaUITestLib_Snapshot import *
from se34euca.lib.EucaUITestLib_Volume import *
from se34euca.lib.EucaUITestLib_Utility import *
#from se34euca.lib.UI_Eutester import *


class EucaUITester():
    selenium_server_ip = "localhost"
    selenium_server_port = "4444"
    protocol = "https"
    ui_ip = "localhost"
    port = "8888"
    accountname = "eucalyptus"
    username = "admin"
    password = "password"
    sauce_account = "eucaqa"
    sauce_access_key = ""
    sauce_address = "@ondemand.saucelabs.com:80"
    retry = 120
    config_file = '/Users/alicehubenko/2b_tested.lst'

    def setSeleniumServerInfo(self, ip, port, sauce_account, sauce_address, sauce_access_key):
        self.selenium_server_ip = ip
        self.selenium_server_port = port
        self.sauce_account = sauce_account
        self.sauce_address = sauce_address
        self.sauce_access_key = sauce_access_key
        print "SELENIUM SERVER IP: " + ip
        print "SELENIUM SERVER PORT: " + port
        print

    def setUIInfo(self, ip, port, protocol):
        self.ui_ip = ip
        self.port = port
        self.protocol = protocol
        print "UI IP: " + ip
        print "PORT: " + port
        print "PROTOCOL: " + protocol
        print

    #def setUIprotocol(self, protocol):
    #    self.protocol = protocol
    #    print "EUCALYPTUS CONSOLE PROXY PROTOCOL: " + protocol
    #    print
    #    return 0

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
        self.base.setSeleniumServerInfo(self.selenium_server_ip, self.selenium_server_port, self.sauce_account, self.sauce_access_key, self.sauce_address)
        self.base.setUIInfo(self.ui_ip, self.port, self.protocol)
        self.base.setUserInfo(self.accountname, self.username, self.password)
        self.base.setUp()
        self.image = EucaUITestLib_Image("NoOp")
        self.image.setSeleniumWebDriver(self.base.driver)
        self.admin_console = EucaUITestLib_Admin_Console("NoOp")
        self.admin_console.setSeleniumWebDriver(self.base.driver)
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
        self.utility = EucaUITestLib_Utility("NoOp")
        self.utility.setSeleniumWebDriver(self.base.driver)
        self.utility.setUserInfo(self.accountname, self.username, self.password)
        self.admin_console = EucaUITestLib_Admin_Console("NoOp")
        print

    def tearDown(self):
        print
        print "========== Terminating EucaUITester =========="
        print
        self.base.tearDown()
        print



