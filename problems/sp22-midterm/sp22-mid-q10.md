# BEGIN PROB

Consider the following pair of hypotheses.

-   **Null hypothesis:** The average GPA of UC San Diego admits from La
    Jolla Private is equal to the average GPA of UC San Diego admits
    from all schools.

-   **Alternative hypothesis:** The average GPA of UC San Diego admits
    from La Jolla Private is less than the average GPA of UC San Diego
    admits from all schools.

# BEGIN SUBPROB

What type of test is this?

( ) Hypothesis test
( ) Permutation test

# BEGIN SOLN

**Answer: ** Hypothesis test

Here, we are asking if one sample is a random sample of a known
population. While this may seem like a permutation test in which we
compare two samples, there is really only one sample here --- the GPAs
of admits from La Jolla Private. To simulate new data, we sample from
the distribution of all GPAs.

Note that this is similar to the bill lengths on Torgersen Island
example from Lecture 6 (in Spring 2022, at least).

<average>75</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which of the following test statistics would be appropriate to use in
this test? **Select all valid options.**

[ ] La Jolla Private mean GPA
[ ] Difference between La Jolla Private mean GPA and overall mean GPA
[ ] Absolute difference between La Jolla Private mean GPA and overall mean GPA
[ ] Total variation distance (TVD)
[ ] Kolmogorov-Smirnov (K-S) statistic

# BEGIN SOLN

**Answer: ** Option 1 and 2

-   In hypothesis tests where we test to see if a sample came from a
    larger distribution, we often use the sample mean as the test
    statistic (again, see the Torgersen Island bill lengths example from
    Lecture 12). Hence, the La Jolla Private mean GPA is a valid option.

-   Note that in this hypothesis test, we will simulate new data by
    generating random samples, each one being the same size as the
    number of applications from La Jolla Private. The **overall** mean
    GPA will not change on each simulation, as it is a constant. Hence,
    Option 2 reduces to Option 1 minus a constant, which purely shifts
    the distribution of the test statistic and the observed statistic
    horizontally but does not change their relative positions to one
    another. Hence, the difference between the La Jolla Private mean GPA
    and overall mean GPA is also a valid test statistic.

-   Option 3 is not valid because our alternative hypothesis has a
    **direction** (that the mean GPA of La Jolla Private admits is less
    than the mean GPA of all admits). The absolute difference would be
    appropriate for a directionless alternative hypothesis, e.g. that
    the mean GPA of La Jolla Private admits is different than the mean
    GPA of all admits.

-   Option 4 doesn't work because we are not dealing with categorical
    distributions.

-   Option 5 doesn't work because we are not running a permutation test
    to test if two samples come from the underlying population
    distribution; rather, here we are testing if one sample comes from a
    larger population (and our hypotheses explicitly mentioned the
    mean).

<average>81</average>

# END SOLN

# END SUBPROB

# END PROB