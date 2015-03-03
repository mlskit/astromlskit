import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from numpy import array
import numpy as np


mat = array([184, 222, 177, 216, 231,
             45, 123, 128, 200,
             129, 121, 203,
             46, 83,
             83])

dist_mat = mat

linkage_matrix = linkage(dist_mat, 'single')
print linkage_matrix

plt.figure(101)
plt.subplot(1, 2, 1)
plt.title("ascending")
dendrogram(linkage_matrix,
           color_threshold=1,
           truncate_mode='lastp',
           labels=array(['a', 'b', 'c', 'd', 'e', 'f']),
           distance_sort='ascending')

plt.subplot(1, 2, 2)
plt.title("descending")
dendrogram(linkage_matrix,
           color_threshold=1,
           truncate_mode='lastp',
           labels=array(['a', 'b', 'c', 'd', 'e', 'f']),
           distance_sort='descending')
plt.show()
