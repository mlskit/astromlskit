

from rdbms.sqlite import SQLiteTable
from regression import RegressionTree
from tables import TableInterface


class RandomForest(object):
    """Random Forest built from bagging regression trees."""

    def __init__(self, table, target, attr_frac=.3, debug=False,
                 exclude=[], min_count=10, min_gain=None, split_sampling=42):
        """Build a new regression tree.

        table -- complete training set
        target -- attribute to learn
        attr_frac -- fraction of attributes to use for splitting
        debug -- turn on/off debug messages and tests
        exclude -- list of attributes to exclude from learning
        min_count -- threshold for leaf size
        min_gain -- minimum gain in variance for splitting
        split_sampling -- number of values to sample when considering
                          a new split on an attribute

        """
        assert isinstance(table, TableInterface)
        self.table = table
        self.target = target
        self.attr_frac = attr_frac 
        self.debug = debug
        self.exclude = exclude
        self.min_count = min_count
        self.min_gain = min_gain
        self.split_sampling = split_sampling

        self.target = target
        self.trees = []
        self.size = 0

    def grow_tree(self):
        """Grow new tree from a fresh bootstrap."""
        bootstrap = self.table.bootstrap()
        tree = RegressionTree(bootstrap, self.target,
                              attr_frac=self.attr_frac,
                              debug=self.debug,
                              exclude=self.exclude,
                              min_count=self.min_count,
                              min_gain=self.min_gain,
                              split_sampling=self.split_sampling)
        self.trees.append(tree)
        self.size += 1

    def grow_trees(self, nb_trees):
        """Grow a given number of trees."""
        for i in range(nb_trees):
            self.grow_tree()

    def predict(self, inst):
        """Predict the regressand for a new instance."""
        s = sum([tree.predict(inst) for tree in self.trees])
        return float(s) / self.size

    #
    # DUMPING
    #
    
    def draw(self, outfile='forest.pdf'):
        import pygraphviz, os, os.path
        g = pygraphviz.AGraph(directed=True)
        for tree in self.trees:
            tree.dump_to_graph(g)
        g.layout(prog='dot')
        if os.path.isfile(outfile):
            os.unlink(outfile)
        g.draw(outfile)
        #os.system('evince %s' % outfile)

    def __str__(self):
        s = ''
        for tree in self.trees:
            s += "\n" + str(tree) + "\n"
        return s
