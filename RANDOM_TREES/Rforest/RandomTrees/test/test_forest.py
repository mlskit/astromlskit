import unittest
from pydtl.rdbms import *
from pydtl.forest import *
from pydtl.tables import *


class TestForest(unittest.TestCase):
    def setUp(self):
        with SQLiteDB('sandbox.sqlite') as db:
            self.table = db.dump_table('events')
    
    def test_forest(self):
        forest = RandomForest(self.table, 'activity')
        forest.grow_trees(10)
        samples = self.table.sample_rows(10)
        predictions = [forest.predict(inst) for inst in samples]


if __name__ == '__main__':
    unittest.main()
