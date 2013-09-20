from eucaops import Eucaops


class UI_Eutester():
    def setUpEutesterInfo(self, config_file, password):
        self.config_file = '/Users/alicehubenko/2b_tested.lst'
        self.password = 'foobar'

    def setUp(self):
        self.tester = Eucaops(config_file='/Users/alicehubenko/2b_tested.lst', password='foobar')
