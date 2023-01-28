# BEGIN PROB

Suppose you wish to run a permutation test to determine whether the missingness in the `'urgency'` column is Missing at Random because of an association with values in the `'category'` column. Which test statistic should be used?

( ) The TVD between the distribution of categories in tasks where the urgency is missing, and the distribution of categories in tasks where the urgency is not missing.
( ) The Kolmogorov-Smirnov statistic between the distribution of categories in tasks where the urgency is missing, and the distribution of categories in tasks where the urgency is not missing.
( ) The TVD between the distribution of urgencies in tasks where the category is missing, and the distribution of urgencies in tasks where the category is not missing.
( ) The Kolmogorov-Smirnov statistic between the distribution of urgencies in tasks where the category is missing, and the distribution of urgencies in tasks where the category is not missing.

# BEGIN SOLN
**Answer: ** Option A

Note that category and urgency is a categorical variable, so if we're going to be looking at the distribution of either one, we'd ideally like to use TVD. Also, since we're considering the missigness of `'urgency'`, the two groups we're looking at are the distribution of categories where urgency is missing vs when urgency is not missing. Thus the right answer is Option A.

<average>91</average>

# END SOLN

# END PROB