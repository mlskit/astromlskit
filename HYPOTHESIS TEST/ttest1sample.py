from scipy import stats
one_sample_data = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]

one_sample = stats.ttest_1samp(one_sample_data, 175.3)

print "The t-statistic is %.3f and the p-value is %.3f." % one_sample
