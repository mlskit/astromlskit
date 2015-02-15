

import unittest
from pydtl.tables import *
from pydtl.rdbms import *


class TestTables(unittest.TestCase):
    def setUp(self):
        with SQLiteDB('sandbox.sqlite') as db:
            self.table = db.dump_table('events')
    
    def test_count(self):
        self.assertEqual(self.table.count(), 1000)

    def test_mean(self, attr='activity'):
        pass

    def test_variance(self, attr='activity'):
        pass

    def test_sample(self, attr='activity'):
        rows = self.table.sample_rows(12)
        self.assertEqual(len(rows), 12)
        self.assertEqual(len(rows[0].keys()), len(self.table.get_attrs()))
        self.assertEqual(len(self.table.sample_attr(attr, 42)), 42)

    def test_split(self):
        lt, rt, nt = self.table.split('completion', 2)
        self.assertEqual(lt.count(), self.table.count())
        self.assertEqual(rt.count(), 0)
        self.assertEqual(nt.count(), 0)


if __name__ == '__main__':
    unittest.main()
