# BEGIN PROB
Dylan wants to answer the following questions using hypothesis tests on the `bus` DataFrame. For each test, select the **one** correct procedure to simulate a single sample under the null hypothesis, and select the **one** correct test statistic for the hypothesis test among the choices given. Assume that the `'time'` column of the `bus` DataFrame has already been parsed into timestamps.

# BEGIN SUBPROB
Are buses more likely to be late in the morning (before 12 PM) or the afternoon (after 12 PM)?
*Note: while the problem says there is only one solution, post-exam two options for the test statistic were given credit. Pick one of the two.*

**Simulation procedure**:

( ) `np.random.choice([-1, 1], bus.shape[0])`
( ) `np.random.choice(bus['late'], bus.shape[0], replace = True)`
( ) Randomly permute the `'late'` column

**Test statistic**:

( ) Difference in means 
( ) Absolute difference in means
( ) Difference in proportions
( ) Absolute difference in proportions

# BEGIN SOLN
**Answer**: Simulation procedure: Randomly permute the `'late'` column; Test statistic: Difference in means or difference in proportions

**Simulation procedure**:
We have two samples here: a sample of `'late'` values for buses in the morning and a sample of `'late'` values for buses in the afternoon. The question is whether the observed difference between these two samples is statistically significant, making this a permutation test.  Note that Option B is similar, but with `replace=True` so it is bootstrapping, not permuting.

**Test statistic**:
Depending on your interpretation of the question, either difference in means or difference in proportions is correct. First, we can't choose absolute difference as a solution because then we can't answer when buses will be more likely to be late, as we need the test statistic to be directional to determine _which_ bus category is more likely to be late. If you interpret the question to mean which group of buses has the higher average lateness, then you would want to choose the difference in means; if you interpret the question to mean which group of buses has a higher count of late buses, then you choose difference in proportions.

<average>56</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Are buses equally likely to be early or late?
*Note: while the problem says there is only one solution, post-exam two options for the test statistic were given credit. Pick one of the two.*

**Simulation procedure**:

( ) A. `np.random.choice([-1, 1], bus.shape[0])`
( ) B. `np.random.choice(bus['late'], bus.shape[0], replace = True)`
( ) C. Randomly permute the `'late'` column

**Test statistic**:

( ) A. Number of values below $0$
( ) B. `np.mean`
( ) C. `np.std`
( ) D. TVD
( ) E. K-S statistic

# BEGIN SOLN
**Answer**: Simulation procedure: `np.random.choice([-1, 1], bus.shape[0])`; Test statistic: Number of values below $0$ or `np.mean`

**Simulation procedure**:
The sample we have here is something like 152 early buses, 125 late buses (these numbers are made up – in practice, these two numbers need to add to `bus.shape[0]`). The question is whether this sample looks like it was drawn from a population that is 50-50 (an equal number of early and late buses), which makes this a hypothesis test. In terms of examples from class, this most closely resembles the very first hypothesis testing example we looked at – the "coin flipping" example.

`np.random.choice([-1, 1], bus.shape[0])` will return an array of length `bus.shape[0]`, where each element is equally likely to be either `-1` (late) or `1` (early). (Note that we could also take `-1` to mean early and `1` to mean late – it doesn't really matter.)

**Test statistic**:
Each time we simulate an arrays of `-1`s and `1`s, we'd like to compute a statistic that helps us differentiate between the number of late (`-1`) and the number of early (`1`) simulated buses. The number of values below $0$ will give us the number of late simulated buses, so we could use that. The mean of the `-1`s and `1`s will give us a value that is negative if there were more late buses and positive if there were more early buses, so we could use that too.

<average>96</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Is the `'late'` column MAR dependent on the `'line'` column?

**Simulation procedure**:

( ) `np.random.choice([-1, 1], bus.shape[0])`
( ) `np.random.choice(bus['late'], bus.shape[0], replace = True)`
( ) Randomly permute the `'late'` column

**Test statistic**:

( ) Absolute difference in means 
( ) Absolute difference in proportions
( ) TVD
( ) K-S statistic

# BEGIN SOLN
**Answer**: Simulation procedure: Randomly permute the `'late'` column; Test statistic: TVD

**Simulation procedure**:
To determine if `'late'` is missing at random dependent on the `'line'` column, we conduct a permutation test and compare (1) the distribution of the `'line'` column when the `'late'` column is missing to (2) the distribution of the `'line'` column when the `'late'` column is not missing to see whether they're significantly different. If the distributions are indeed significantly different, then it is likely that the `'late'` column is MAR dependent on `'line'`.
**Test statistic**:
Since we are comparing the distributions of *categorical* data (`'line'` is categorical) for our permutation test, Total Variation Distance is the best test statistic to use.

<average>57</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Is the `'late'` column MAR dependent on the `'time'` column?

**Simulation procedure**:

( ) A. `np.random.choice([-1, 1], bus.shape[0])`
( ) B. `np.random.choice(bus['late'], bus.shape[0], replace = True)`
( ) C. Randomly permute the `'late'` column

**Test statistic**:

( ) A. Absolute difference in proportions
( ) B. TVD
( ) C. K-S statistic
# BEGIN SOLN
**Answer**: Simulation procedure: Randomly permute the `'late'` column; Test statistic: K-S statistic

**Simulation procedure**:
Like in the previous part, to determine if `'late'` is missing at random dependent on the `'time'` column, we conduct a permutation test and compare (1) the distribution of the `'time'` column when the `'late'` column is missing to (2) the distribution of the `'time'` column when the `'late'` column is not missing to see whether they're significantly different.

**Test statistic**:
Since we are comparing the distributions of *numerical* data (`'time'` is numerical) for our permutation test, K-S statistic is the best test statistic to use of the options provided.

# END SOLN
# END SUBPROB
# END PROB