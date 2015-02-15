import unittest
from pydtl.rdbms import *
from pydtl.regression import *


class TestRegression(unittest.TestCase):
    def setUp(self):
        self.db = SQLiteDB('sandbox.sqlite')
        self.table = self.db.dump_table('events')
    
    def test_local(self):
        tree = RegressionTree(self.table, 'activity')
        samples = self.table.sample_rows(10)
        predictions = [tree.predict(inst) for inst in samples]


if __name__ == '__main__':
    unittest.main()
