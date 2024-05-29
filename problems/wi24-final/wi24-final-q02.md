# BEGIN PROB

At the Estancia La Jolla, the hotel manager enters information about each reservation in the DataFrame `guests`, after guests check into their rooms. Specifically, `guests` has the columns:

- `"id" (str):` The booking ID (e.g. `"SN1459"`).
- `"age" (int):` The age of the primary occupant (the person who made the reservation).
- `"people" (int):` The total number of occupants.
- `"is_business" (str):` Whether or not the trip is a business trip for the primary occupant (possible values: `"yes"`, `"no"`, and `"partially"`).
- `"company" (str):` The company that the primary occupant works for, if this is a business trip.
- `"loyalty" (int):` The loyalty number of the primary occupant. Note that most business travelers have a loyalty number.

Some of the values in `guests` are missing.

# BEGIN SUBPROB

What is the most likely missingness mechanism of the `"loyalty"` column?

( ) Missing by design
( ) Missing at random
( ) Not missing at random
( ) Missing completely at random

# BEGIN SOLUTION

**Answer:** missing at random

The description of `loyalty` indicates that most business travelers have a loyalty number -- in other words, that depending on the value of `is_business`, the probability of a present value for `loyalty` can increase or decrease. This is therefore an example of MAR.

<average>67</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the most likely missingness mechanism of the `"company"` column?

( ) Missing by design
( ) Missing at random
( ) Not missing at random
( ) Missing completely at random

# BEGIN SOLUTION

**Answer:** missing by design

The value of `company` is missing if the trip is a business trip, and since this relationship should be deterministic, then this column is missing by design.

<average>60</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blanks: To assess whether the missingness of `"is_business"` depends on `"age"`, we should perform a `__(i)__` with `__(ii)__` as the test statistic.

1. What goes in blank (i)?

( ) standard hypothesis test
( ) permutation test

2. What goes in blank (ii)?

( ) the total variation distance
( ) the sample mean
( ) the (absolute) difference in means
( ) the K-S statistic
( ) either the (absolute) difference in means or the K-S statistic, depending on the shapes of the observed distributions

# BEGIN SOLUTION

**Answers:**

1. permutation test
2. either the (absolute) difference in means or the K-S statistic, depending on the shapes of the observed distributions

In part 1, we use a permutation test because we're comparing two sampled distributions (the values of `age` for rows with missing vs. present values of `is_business`), rather than comparing our sample distribution to a known population distribution/metric.

For part 2, we should note that the test statistic, for each iteration of our permutation test, is meant to compare two distributions of the variable `age`, which is continuous. TVD is not well-suited for this, since it compares discrete, categorical distributions, and neither is "sample mean," since we have two samples to compare. Differences in means or the K-S statistic work because they both compare two continuous distributions. However, there are cases in which the difference in means might not capture differences in distributions (for example, two distributions with the same mean but very different standard deviation); this is the reason for the caveat in the correct solution.

<average>68</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blanks: To assess whether the missingness of `"age"` depends on `"is business"`, we should perform a `__(i)__` with `__(ii)__` as the test statistic.

1. What goes in blank (i)?

( ) standard hypothesis test
( ) permutation test

2. What goes in blank (ii)?

( ) the total variation distance
( ) the sample mean
( ) the (absolute) difference in means
( ) the K-S statistic
( ) either the (absolute) difference in means or the K-S statistic, depending on the shapes of the observed distributions

# BEGIN SOLUTION

**Answers:**

1. permutation test
2. total variation distance

For part 1, the reasoning is the same as the previous part -- the only difference is that now, we're comparing two categorical distributions rather than two continuous ones.

In part 2, we can note that we're now comparing the categorical distributions of `is_business`, which can only have values of `"yes"`, `"no"`, and `"partially"`, for rows with missing vs. present values of `age`. (Even though `age` is continuous, since we're only using whether or not `age` is missing and not the actual values in the column, this doesn't really matter.) The only test statistic listed that is meant to compare two categorical distributions is TVD, so this is the correct solution.

<average>72</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

After running the code below, `p` is equal to the simulated p-value for a statistical test.

```py
    obs = guests.groupby("is_business")["age"].median().loc["no"]
    p = 0
    for _ in range(10000):
        s = guests.sample((guests["is_business"] == "no").sum(),
        replace=False)
        sm = s["age"].median()
        p += (obs >= sm) / 10000
```

1. What type of test is this?

( ) standard hypothesis test
( ) permutation test

Fill in the blanks: The alternative hypothesis being tested above is that the median age of primary occupants **not** on a business trip is `__(ii)__` the median age of `__(iii)__`.

2. What goes in blank (ii)?

( ) greater than or equal to
( ) greater than
( ) equal to
( ) not equal to
( ) less than or equal to
( ) less than

3. What goes in blank (iii)?

( ) all primary occupants
( ) primary occupants at least partially on a business trip (that is, primary occupants who have an `"is_business"` value of `"yes"` or `"partially"`)

# BEGIN SOLUTION

**Answers:**

1. standard hypothesis test
2. less than
3. all primary occupants

For part 1, this is a standard hypothesis test, because instead of shuffling the values of a particular column, we are sampling entire rows of the DataFrame; the size of these samples is the same as the number of guests who are not (even partially) on business trips. By sampling randomly from the entire DataFrame, this assumes the null hypothesis that the distribution of age of primary occupants *not* on a business trip is equal to the distribution of age for occupants as a whole. Therefore, this procedure is meant to simulate values of the median `age` of a sample of size `guests["is_business"] == "no").sum()`, and sampling random rows means that we're assuming that `is_business == "no"` and `age` are unrelated.

For part 2, the samples capture how likely the deviation of the observed statistic is to happen under the null hypothesis, but the p-value is being calculated by adding up whenever the observed statistic is greater or equal to the sample. This indicates that we're doing a one-tailed test, and since to reject the null hypothesis and provide some evidence towards the alternate hypothesis, the p-value should be lower, the alternate hypothesis should be the complement of `obs >= sum`.

For part 3, the answer is "all primary occupants" because our sampling procedure doesn't sample just from (full or partial) business travelers, but from the entire DataFrame. (In the line where we sample, the only arguments are the number of rows we're sampling, and that we're doing so without replacement -- nothing about restricting which rows in `guest` to sample.) In other words, we're not comparing primary occupants not on business trips to those on business trips, but rather we're comparing primary occupants to the entire dataset of occupants. 

<average>58</average>

# END SOLUTION

# END SUBPROB

# END PROB
