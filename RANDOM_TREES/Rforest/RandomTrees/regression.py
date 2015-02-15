

import random


class RegressionTree(object):
    """Wrapper for a whole regression tree."""
    
    def __init__(self, table, target, attr_frac=.75, debug=False,
                 exclude=[], min_count=10, min_gain=None, split_sampling=100):
        """Build a new regression tree.

        table -- complete training table
        target -- attribute to learn
        attr_frac -- fraction of attributes to use for splitting
        debug -- turn on/off debug messages and tests
        exclude -- list of attributes to exclude from learning
        min_count -- threshold for leaf size
        min_gain -- minimum gain in variance for splitting
        split_sampling -- number of values to sample when considering
                          a new split on an attribute

        """
        self.target = target
        self.attr_frac = attr_frac 
        self.debug = debug
        self.min_count = min_count
        self.min_gain = min_gain
        self.split_sampling = split_sampling

        self.attrs = [attr for attr in table.get_attrs()
                      if attr != target and attr not in exclude]
        self.nb_split_attr = int(attr_frac * len(self.attrs))

        self.root = RegressionNode(table, self)

    #
    # PREDICTION
    #
    
    def predict(self, inst):
        """Regress a new instance"""
        return self.root.predict(inst)

    def neigh_predict(self, inst, attr, min_val, max_val):
        """For attribute `attr`, predict the regressand value as well
        as its two closest split values and the regressand values beyond
        (but close to) these bounds.

        inst -- instance to lookup
        attr -- attribute whose neighborhood we explore
        min_val -- attribute's minimum value on the training set
        max_val -- attribute's maximum value on the training set

        """
        class AttrNeighborhood(object):
            def __init__(self, left_bound, right_bound):
                self.left_bound = left_bound
                self.right_bound = right_bound
                self.left_reg = None
                self.cur_reg = None
                self.right_reg = None
            
            def __str__(self):
                return "%s |%.3f| %s |%.3f| %s" \
                       % (str(self.left_reg), self.left_bound,
                          str(self.cur_reg), self.right_bound,
                          str(self.right_reg))
        
        neigh = AttrNeighborhood(min_val, max_val)
        self.root.neigh_predict(inst, attr, neigh)
        return neigh    

    #
    # DUMPING
    #
    
    def dump_to_graph(self, g):
        """Dump to a (GraphViz) representation."""
        return self.root.dump_to_graph(g)
    
    def __str__(self):
        """Give a (multi-line) string representation."""
        return self.root.__str__()


class RegressionNode(object):
    def __init__(self, table, tree):
        """Grow a new node in a given regression tree.

        table -- LocalTable/RemoteTable to train from
        tree -- tree to grow in
        
        """
        self.table = table
        self.tree = tree
        self.variance = table.variance(tree.target)
        if table.count() < tree.min_count or self.variance == 0.:
            return self.become_leaf()
        
        best_split = self.try_split()
        gain = 1 - best_split.exp_var / self.variance
        if gain <= tree.min_gain:
            return self.become_leaf()
        
        if tree.debug:
            assert issubclass(table, TableInterface)            
            print "  --"
            print "  | count: %d" % table.count()
            print "  | variance: %.3e" % self.variance
            print "  | variance gain: %.1f%%" % (100. * gain)
        
        self.split = best_split
        self.left_branch  = RegressionNode(best_split.left_table, tree)
        self.right_branch = RegressionNode(best_split.right_table, tree)
    
    def become_leaf(self):
        self.split = None
        self.left_branch = None
        self.right_branch = None
        self.leaf_value = self.table.mean(self.tree.target)
        if self.tree.debug:
            print "  --"
            print "  | becoming a leaf"
            print "  | count: %d" % self.table.count()
    
    def is_leaf(self):
        return self.left_branch == None or self.right_branch == None
    
    #
    # SPLITTING
    #
    
    class AttrSplit:
        """Computes an attribute split and stores the resulting tables."""

        def __init__(self, node, attr, split_val):
            table = node.table
            left_table, right_table, null_table = table.split(attr, split_val)
            if null_table.count() > 0:
                raise NotImplementedError, "No unknown attributes for now"

            self.attr = attr
            self.val = split_val
            self.left_table = left_table
            self.right_table = right_table
            self.null_table = null_table

            if left_table.count() == 0 or right_table.count() == 0:
                self.exp_var = table.variance(node.tree.target)
            else:
                q = float(left_table.count()) / table.count()
                left_var = left_table.variance(node.tree.target)
                right_var = right_table.variance(node.tree.target)
                self.exp_var = q * left_var + (1 - q) * right_var


    def try_split(self):
        # don't use all attributes
        # e.g. to avoid cross-correlation in Random Forests
        split_attrs = random.sample(self.tree.attrs, self.tree.nb_split_attr)
        sampling = self.tree.split_sampling
        best_split = None
        for attr in split_attrs:
            for split_val in self.table.sample_attr(attr, sampling):
                split = self.AttrSplit(self, attr, split_val)
                if not best_split or split.exp_var < best_split.exp_var:
                    best_split = split
        if self.tree.debug:
            assert best_split, "Found no split in %s" % split_attrs
        return best_split

    #
    # PREDICTIONS
    #
    
    def predict(self, inst):
        """Predict the regressand value for instance `inst`."""
        # TODO: unknown attributes
        if self.is_leaf():
            return self.leaf_value
        elif inst[self.split.attr] <= self.split.val:
            return self.left_branch.predict(inst)
        else:
            return self.right_branch.predict(inst)

    def neigh_predict(self, inst, attr, neigh):
        """Internal, side-effect part of RegressionTree.neigh_predict().

        inst -- instance to predict from
        attr -- the attribute whose neighborhood we are exploring
        neigh -- datastructure where neighborhood infos are to be stored

        """
        if self.is_leaf():
            neigh.cur_reg = self.leaf_value
            return neigh

        assert (self.split.attr in inst.keys())
            
        if inst[self.split.attr] <= self.split.val:
            self.left_branch.neigh_predict(inst, attr, neigh)
            if self.split.attr == attr \
                   and neigh.right_bound > self.split.val:
                neigh.right_bound = self.split.val
                neigh.right_reg = self.right_branch.predict(inst)
        else:
            self.right_branch.neigh_predict(inst, attr, neigh)
            if self.split.attr == attr \
                   and neigh.left_bound < self.split.val:
                neigh.left_bound = self.split.val
                neigh.left_reg = self.left_branch.predict(inst)

    #
    # DUMPING
    #
    
    def __str__(self, depth=0):
        s = '  | ' * depth
        if self.is_leaf():
            s += '%.2f [c=%d, V=%.1e]\n' \
                % (self.leaf_value, self.table.count(), self.variance)
        else:
            s += '%s(%.2f) [c=%d, V=%.1e]\n' \
                % (self.split.attr, self.split.val,
                   self.table.count(), self.variance)
            s += "%s%s" \
                % (self.left_branch.__str__(depth + 1),
                   self.right_branch.__str__(depth + 1))
        return s

    def dump_to_graph(self, g):
        count = self.table.count()
        var = self.variance
        sub_label = 'count = %d\\nVar = %.2e' % (count, var)
        if self.is_leaf():
            label = '%.2f\\n%s' % (self.leaf_value, sub_label)
            g.add_node(self.table.name, label=label, shape='box',
                       fillcolor='#FFFFBB', style='filled')
        else:
            attr = self.split.attr.replace('_', ' ').upper()
            label = '%s\\n%s' % (attr, sub_label)
            g.add_node(self.table.name, label=label, shape='egg',
                       fillcolor='#BBFFFF', style='filled')
            self.left_branch.dump_to_graph(g)
            self.right_branch.dump_to_graph(g)
            g.add_edge(self.table.name, self.left_branch.table.name,
                       label='≤ %.2f' % self.split.val)
            g.add_edge(self.table.name, self.right_branch.table.name,
                       label='> %.2f' % self.split.val)
