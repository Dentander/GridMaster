from unitTests.base.UnitTest import UnitTest


class Movement(UnitTest):
    def test1(self):
        self.full_run('block1/test1_1', (0, 5))

    def test2(self):
        self.full_run('block1/test1_2',(1,1))
    def test3(self):
        self.full_run('block1/test1_3',(0,0))
class IfBlocks(UnitTest):
    def test1(self):
        self.full_run('block2/test2_1',(5,5))
    def test2(self):
        self.full_run('block2/test2_2',(0,2))