
import unittest
from pydtl.rdbms import *
from pydtl.tables import *


class TestSQLite(unittest.TestCase):
    def setUp(self):
        self.db = SQLiteDB('sandbox.sqlite')
        self.loc_table = self.db.dump_table('events')
        self.rem_table = SQLiteTable('events', self.db)
    
    def test_count(self):
        self.assertEqual(self.loc_table.count(), self.rem_table.count())

    def test_mean(self, attr='activity'):
        lmean = self.loc_table.mean(attr)
        rmean = self.rem_table.mean(attr)
        self.assertTrue(abs(lmean - rmean) < 1e-5)

    def test_variance(self, attr='activity'):
        lvar = self.loc_table.variance(attr)
        rvar = self.rem_table.variance(attr)
        self.assertTrue(abs(lvar - rvar) < 1e-5)

    def test_sample(self, attr='activity'):
        rl = self.rem_table.sample_attr(attr, 31)
        self.assertEqual(len(rl), 31)

    def test_split(self):
        lt, rt, nt = self.rem_table.split('completion', 2)
        self.assertEqual(lt.count(), self.loc_table.count())
        self.assertEqual(rt.count(), 0)
        self.assertEqual(nt.count(), 0)

    def test_split_both(self):
        lt1, rt1, nt1 = self.loc_table.split('completion', .4)
        lt2, rt2, nt2 = self.rem_table.split('completion', .4)
        self.assertEqual(lt1.count(), lt2.count())
        self.assertEqual(rt1.count(), rt2.count())
        self.assertEqual(nt1.count(), nt2.count())

    def test_tree(self):
        tree = RegressionTree(self.rem_table, 'activity',
                              min_count=200, split_sampling=10)
        samples = self.rem_table.sample_rows(10)
        predictions = [tree.predict(inst) for inst in samples]


if __name__ == '__main__':
    unittest.main()
