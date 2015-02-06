import numpy as np
import random

__all__ = [
    'get_nprandom',
    'get_pyrandom',
    ]

def get_nprandom(R):
    '''
    R' = get_nprandom(R)

    Returns a numpy.RandomState from R

    Parameters
    ----------
    R : can be one of:
        None          : Returns the default numpy global state
        integer       : Uses it as a seed for constructing a new random generator
        RandomState   : returns R

    Returns
    -------
    R' : np.RandomState
    '''
    if R is None:
        return np.random.mtrand._rand
    if type(R) == int:
        return np.random.RandomState(R)
    if type(R) is random.Random:
        return np.random.RandomState(R.randint(0, 2**30))
    if type(R) is np.random.RandomState:
        return R
    raise TypeError("get_nprandom() does not know how to handle type {0}.".format(type(R)))

def get_pyrandom(R):
    '''
    R = get_pyrandom(R)

    Returns a random.Random object based on R

    Parameters
    ----------
    R : can be one of:
        None          : Returns the default numpy global state
        integer       : Uses it as a seed for constructing a new random generator
        RandomState   : returns R

    Returns
    -------
    R' : random.Random
    '''
    if R is None:
        return random.seed.im_self
    if type(R) is int:
        return random.Random(R)
    if type(R) is np.random.RandomState:
        return random.Random(R.randint(2**30))
    if type(R) is random.Random:
        return R
    raise TypeError("get_pyrandom() does not know how to handle type {0}.".format(type(R)))


