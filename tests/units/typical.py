from tests.base.tests import UnitTest


class Movement(UnitTest):
    def test1(self):
        self.full_run('test1', (0, 5))

    def test2(self):
        self.full_run('test2',(1,1))