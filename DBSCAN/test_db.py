import ddbscan

# Create a DDBSCAN model with eps = 2 and min_pts = 5
scan = ddbscan.DDBSCAN(2, 5)

# Add points to model
data = [[1,  100], [2,  2], [1,  3], [2, 3], [3, 3], [8, 9],
        [7,  6], [9,  7], [6, 9], [6, 8], [5, 5], [7, 8]]

for point in data:
    scan.add_point(point=point, count=1, desc="")

# Compute clusters
scan.compute()

print 'Clusters found and its members points index:'
cluster_number = 0
for cluster in scan.clusters:
    print '=== Cluster %d ===' % cluster_number
    print 'Cluster points index: %s' % list(cluster)
    cluster_number += 1

print '\nCluster assigned to each point:'
for i in xrange(len(scan.points)):
    print '=== Point: %s ===' % scan.points[i]
    print 'Cluster: %2d' % scan.points_data[i].cluster,
    # If a point cluster is -1, it's an anomaly
    if scan.points_data[i].cluster == -1:
        print '\t <== Anomaly found!'
    else:
        print

# Print ASCII plot
print
print ' ===== Data plot ====='
print
print 'Legend => x: anomaly'

symbols = 'x#=~+-opwbcnkjhf@uyt()987654321' # Symbols used to plot points
cluster_number = 0
for cluster in scan.clusters:
    print '          %s: cluster %d' % (symbols[cluster_number + 1], cluster_number)
    cluster_number += 1
print

print '-----------------------'
for x in range(0,10):
    print '|',
    for y in range(0, 10):
        if [x, y] in data:
            index = data.index([x,y])
            cluster = scan.points_data[index].cluster + 1
            #print cluster
            print symbols[cluster],
        else:
            print ' ',
    print '|'
print '-----------------------'
