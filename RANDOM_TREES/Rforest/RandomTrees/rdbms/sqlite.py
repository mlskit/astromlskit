

import sqlite3
from pydtl.tables import *


class SQLiteDB(object):
    """Wrapper for sqlite3 cursors."""
    
    def __init__(self, fname):
        """Open connection and get cursor."""
        self.conn = sqlite3.connect(fname)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self._next_table_id = 0

    def __enter__(self):
        """For use within a `with` context."""
        return self

    def __exit__(self, type, value, traceback):
        """Close connection when leaving a `with` context."""
        self.close()

    def query(self, q):
        """Pass a query through the cursor."""
        self.cursor.execute(q)

    def commit(self):
        """Commit pending transactions."""
        self.conn.commit()

    def fetchone(self):
        """Fetch one row from last query."""
        return self.cursor.fetchone()

    def close(self):
        """Clean the database and close the handler."""
        last_id = self._next_table_id
        for i in range(1, last_id + 1):
            self.cursor.execute('DROP TABLE IF EXISTS `tmp_%d`' % i)
            self.cursor.execute('DROP INDEX IF EXISTS `tmp_%d_index`' % i)
        self.conn.commit()
        self.cursor.close()

    def count(self, table_name, where=''):
        query = 'SELECT COUNT(*) FROM %s ' % table_name
        if len(where) > 0:
            query += 'WHERE %s' % where
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def next_name(self):
        """Provide a new, temporary table name."""
        self._next_table_id += 1
        return 'tmp_%d' % self._next_table_id

    def dump_table(self, table):
        """Dump some table into a local object."""
        loc_table = LocalTable()
        self.query("SELECT * FROM %s" % table)
        for row in self.cursor:
            loc_table.insert(row)
        return loc_table


class SQLiteTable(TableInterface):
    """Table read/written from/to the DB. Useful for big datasets."""
    
    def __init__(self, table_name, db, where='', shuffle=False, limit=0):
        """Create a new table in `db` from `table_name`.

        table_name -- name of the initial table
        db -- database handler
        where -- where condition to apply
        shuffle -- include an ORDER BY clause in the query
        limit -- maximum table size

        """
        self.db = db
        self.name = self.db.next_name()        
        qselect = 'SELECT * FROM %s ' % table_name
        if len(where) > 0:
            qselect += 'WHERE %s ' % where
        if shuffle:
            qselect += 'ORDER BY RANDOM() '
        if limit > 0:
            qselect += 'LIMIT %d ' % limit
        self.db.query('DROP TABLE IF EXISTS %s' % self.name)
        self.db.query('CREATE TABLE %s AS %s' % (self.name, qselect))
        self.db.query('CREATE INDEX %s_index ON %s(player_id)'
                      % (self.name, self.name))

    def get_attrs(self):
        self.db.query('SELECT * FROM %s LIMIT 1' % self.name)
        row = self.db.fetchone()
        return row.keys()
    
    def count(self):
        return self.db.count(self.name)

    def mean(self, attr):
        if self.count() == 0:
            return None
        self.db.query('SELECT AVG(%s) FROM %s' % (attr, self.name))
        row = self.db.fetchone()
        return row[0]
    
    def variance(self, attr):
        if self.count() == 0:
            # 0 convention: no gain in attribute split anyway
            return 0
        avg = self.mean(attr)
        e = '(%s - %.20f)' % (attr, avg)
        self.db.query('SELECT AVG(%s * %s) FROM %s' % (e, e, self.name))
        row = self.db.fetchone()
        return row[0]

    def sample_rows(self, sample_size):
        qselect = 'SELECT * FROM %s ' % self.name
        qselect += 'ORDER BY RANDOM() LIMIT %d' % sample_size
        self.db.query(qselect)
        return [row for row in self.db.cursor]
        
    def sample_attr(self, attr, sample_size):
        qselect = 'SELECT %s FROM %s ' % (attr, self.name)
        qselect += 'ORDER BY RANDOM() LIMIT %d' % sample_size
        self.db.query(qselect)
        return [row[0] for row in self.db.cursor]

    def split(self, attr, split_val):
        cnull = '%s IS NULL' % attr
        cleft = '%s <= %f' % (attr, split_val)
        cright = '%s > %f' % (attr, split_val)
        
        left_table = SQLiteTable(self.name, self.db, where=cleft)
        right_table = SQLiteTable(self.name, self.db, where=cright)
        null_table = SQLiteTable(self.name, self.db, where=cnull)
        return left_table, right_table, null_table

    def bootstrap(self):
        bootstrap = SQLiteTable(self.name, self.db, shuffle=True, limit=1)
        qsample = 'SELECT * FROM %s ORDER BY RANDOM() LIMIT 1' % self.name
        for r in range(self.count() - 1):
            self.db.query('INSERT INTO `%s` %s' % (bootstrap.name, qsample))
        return bootstrap
    
