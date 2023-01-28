# BEGIN PROB
Suppose it is determined that the missingness in the `'urgency'` column is Missing at Random due to an association with the `'category'`column, and that tasks in the `'work'` category are least likely to be missing an urgency. You can assume that tasks in the `'work'` category have higher-than-average urgencies.

Suppose the missing urgencies are imputed by randomly sampling from the observed urgencies. If the mean urgency of tasks in the `'hobbies'` category is computed, what is likely to be true?

( ) It will be unbiased.
( ) It will be biased high (higher than the true average).
( ) It will be biased low (lower than the true average).

# BEGIN SOLN
**Answer: ** Option B

Since the average urgency of `'work'` category tasks is higher than average, and since `'work'` category tasks are less likely to have a missing urgency value, we conclude that the mean urgency of tasks will be biased high if we randomly sample from the observed urgencies.

<average>80</average>

# END SOLN

# END PROB

