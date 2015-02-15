


class TableInterface(object):
    def get_attrs(self):
        """Get all table attributes."""
        raise NotImplementedError
    
    def count(self):
        """Count the number of rows in the table."""
        raise NotImplementedError

    def mean(self, attr):
        """Compute the mean of all (real) values of an attribute."""
        raise NotImplementedError
    
    def variance(self, attr):
        """Compute the variance of the set of values of an attribute."""
        raise NotImplementedError

    def sample_rows(self, attr, sample_size):
        """Sample table rows uniformly at random."""
        raise NotImplementedError

    def sample_attr(self, attr, sample_size):
        """Sample uniformly at random from the set of values of an attribute.

        attr -- the attribute
        sample_size -- number of values to sample

        """
        raise NotImplementedError

    def split(self, attr, split_val):
        """Split according to a given attribute and a split value.
        Returns a 3-uple of tables: one for values <= split_val, one for
        values > split_val and one for undef values of the attribute.

        attr -- attribute to split on
        split_val -- split value

        """
        raise NotImplementedError

    def bootstrap(self):
        """Get a bootstrap for current table."""
        raise NotImplementedError


class LocalTable(TableInterface):
    """Table imported from the DB and stored in RAM"""
    
    def __init__(self, init_dict=None):
        if init_dict:
            assert isinstance(init_dict, dict)
            self._attrs = init_dict.keys()
            self.dict = init_dict.copy()
            self.size = len(self.dict)
        else:
            self._attrs = []
            self.dict = {}
            self.size = 0
 
    def insert(self, entry):
        row_id = self.size
        self.dict[row_id] = {}
        self.size += 1
        for key in entry.keys():
            if not key in self._attrs:
                self._attrs.append(key)
            self.dict[row_id][key] = entry[key]

    def get_attrs(self):
        return self._attrs
    
    def count(self):
        return self.size

    def mean(self, attr):
        assert self.size > 0, "Trying to compute mean of an empty set"
        total = float(sum([row[attr] for row in self.dict.itervalues()]))
        return total / self.size
    
    def variance(self, attr):
        assert self.size > 0, "Trying to compute variance of an empty set"
        totsq = float(sum([row[attr]**2 for row in self.dict.itervalues()]))
        return totsq / self.size - self.mean(attr)**2

    def sample_rows(self, sample_size):
        import random
        assert self.size > 0, "Trying to sample an empty table"
        return [self.dict[random.randint(0, self.size - 1)]
                for i in range(sample_size)]
    
    def sample_attr(self, attr, sample_size):
        return [row[attr] for row in self.sample_rows(sample_size)]

    def split(self, attr, split_val):
        left_table = LocalTable()
        right_table = LocalTable()
        null_table = LocalTable()
        for entry in self.dict.itervalues():
            if not attr in entry.keys():
                null_table.insert(entry)
            elif entry[attr] <= split_val:
                left_table.insert(entry)
            else:
                right_table.insert(entry)
        return left_table, right_table, null_table

    def bootstrap(self):
        bootstrap = LocalTable()
        for row in self.sample_rows(self.size):
            bootstrap.insert(row)
        return bootstrap
