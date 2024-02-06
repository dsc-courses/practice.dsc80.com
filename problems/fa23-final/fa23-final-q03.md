# BEGIN PROB
Dylan wants to answer the following questions using hypothesis tests on the `bus` DataFrame. For each test, select the **one** correct procedure to simulate a single sample under the null hypothesis, and select the **one** correct test statistic for the hypothesis test among the choices given. Assume that the `'time'` column of the `bus` DataFrame has already been parsed into timestamps.

# BEGIN SUBPROB
Are buses more likely to be late in the morning (before $12$pm) or the afternoon (after $12$pm)?
*Note: while the problem says there is only one solution, post-exam two options for test statistic were given credit. Pick one of the two.*

**Simulation procedure**:

( ) A. `np.random.choice([-1, 1], bus.shape[0])`
( ) B. `np.random.choice(bus['late'], bus.shape[0], replace = True)`
( ) C. Randomly permute the `'late'` column

**Test statistic**

( ) A. Difference in means 
( ) B. Absolute difference in means
( ) C. Difference in proportions
( ) D. Absolute difference in proportions
# BEGIN SOLN
**Answer**: Simulation procedure - C). Test statistic - A) or C).

**Simulation procedure**:
We have two different populations here - morning buses and afternoon buses. We are measuring one sample - whether a bus is late or not. This means we want to conduct a permutation test to see if the morning and afternoon buses are from the same distribution, so the correct answer is to permute the `'late'` column. Note that option B) is similar, but with `replace = True` so it is bootstrapping, not permutation.
**Test statistic**:
Depending on your interpretation of the question, either option A) or C) is correct. First, we can't choose absolute difference as a solution because then we can't answer when buses will be more likely to be late, as we need the test statistic to be directional to determine *which* bus. If you interpret the question to mean which population has the higher average lateness, then you would want to choose option A). If you interpret the question to mean which population has a higher count of late buses, then you choose option C).
# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Are buses equally likely to be early or late?
*Note: while the problem says there is only one solution, post-exam two options for test statistic were given credit. Pick one of the two.*

**Simulation procedure**:

( ) A. `np.random.choice([-1, 1], bus.shape[0])`
( ) B. `np.random.choice(bus['late'], bus.shape[0], replace = True)`
( ) C. Randomly permute the `'late'` column

**Test statistic**

( ) A. Number of values below $0$
( ) B. `np.mean`
( ) C. `np.std`
( ) D. TVD
( ) E. K-S statistic
# BEGIN SOLN
**Answer**: Simulation procedure - A). Test statistic - A) or B).

**Simulation procedure**:
We now have only one population, which is just all buses. We then want to see if a sample is from that population, so we conduct a hypothesis test under the null. The null would be that buses are equally likely to be early or late, so we can simulate this by randomly generating `[-1, 1]` for all buses. This is what option A) does. 
**Test statistic**:
Since we know the number of buses, we can use the number of values below $0$ to determine whether we have more early buses, more late buses, or the same amount. Similarly, the mean will give us a value between $-1$ and $1$, where $0$ means we have the equal early and late buses, while $-1$ represents only early buses, and $1$ represents only late buses.
# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Is the `'late'` column MAR dependent on the `'line'` column?

**Simulation procedure**:

( ) A. `np.random.choice([-1, 1], bus.shape[0])`
( ) B. `np.random.choice(bus['late'], bus.shape[0], replace = True)`
( ) C. Randomly permute the `'late'` column

**Test statistic**

( ) A. Absolute difference in means 
( ) B. Absolute difference in proportions
( ) C. TVD
( ) D. K-S statistic
# BEGIN SOLN
**Answer**: Simulation procedure - C). Test statistic - C).

**Simulation procedure**:
To determine MAR, we run a permutation test and compare the distributions of the `'line'` column when the `'late'` column is missing or not to see if it changes. If the distributions are similar then the data is likely MCAR, but if the distributions change then it is likely the `'late'` column is MAR on `'line'`.
**Test statistic**:
Since we are comparing the distributions of *categorical* data for our permutation test, Total Variation Distance is the best test statistic to use.
# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Is the `'late'` column MAR dependent on the `'time'` column?

**Simulation procedure**:

( ) A. `np.random.choice([-1, 1], bus.shape[0])`
( ) B. `np.random.choice(bus['late'], bus.shape[0], replace = True)`
( ) C. Randomly permute the `'late'` column

**Test statistic**

( ) A. Absolute difference in proportions
( ) B. TVD
( ) C. K-S statistic
# BEGIN SOLN
**Answer**: Simulation procedure - C). Test statistic - C).

**Simulation procedure**:
Again, to determine MAR, we run a permutation test and compare the distributions of the `'time'` column when the `'late'` column is missing or not to see if it changes. If the distributions are similar then the data is likely MCAR, but if the distributions change then it is likely the `'late'` column is MAR on `'time'`.
**Test statistic**:
Since we are comparing the distributions of *numerical* data for our permutation test, K-S statistic is the best test statistic to use.
# END SOLN
# END SUBPROB
# END PROB