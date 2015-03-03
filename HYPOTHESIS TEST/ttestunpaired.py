female = [63.8, 56.4, 55.2, 58.5, 64.0, 51.6, 54.6, 71.0]
male = [75.5, 83.9, 75.7, 72.5, 56.2, 73.4, 67.7, 87.9]

two_sample = stats.ttest_ind(male, female)

print "The t-statistic is %.3f and the p-value is %.3f." % two_sample

# assuming unequal population variances
two_sample_diff_var = stats.ttest_ind(male, female, equal_var=False)

print "If we assume unequal variances than the t-statistic is %.3f and the 
p-value is %.3f." % two_sample_diff_var
