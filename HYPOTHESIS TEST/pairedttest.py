baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

paired_sample = stats.ttest_rel(baseline, follow_up)

print "The t-statistic is %.3f and the p-value is %.3f." % paired_sample
