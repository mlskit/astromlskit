from __future__ import division

class supervised_model(object):
    def apply_many(self, fs):
        '''
        labels = model.apply_many( examples )

        This is equivalent to ``map(model.apply, examples)`` but may be
        implemented in a faster way.

        Parameters
        ----------
        examples : sequence of training examples

        Returns
        -------
        labels : sequence of labels
        '''
        return map(self.apply, fs)


class base_adaptor(object):
    def __init__(self, base):
        self.base = base

    def set_option(self, k, v):
        self.base.set_option(k, v)
