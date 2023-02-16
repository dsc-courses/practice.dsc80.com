# BEGIN PROB

The `"IMDb"` column in `tv_excl` contains several missing values.

***Note***: Answer each subpart of this question independently of other
subparts.

# BEGIN SUBPROB

Given no other information other than a TV show's `"Title"` and `"IMDb"`
rating, what is the most likely missingness mechanism of the `"IMDb"`
column?

( ) Missing by design ( ) Not missing at random ( ) Missing at random (
) Missing completely at random

# END SUBPROB

# BEGIN SUBPROB

Now, suppose we discover that the median `"Rotten Tomatoes"` rating
among TV shows with a missing `"IMDb"` rating is a 13, while the median
`"Rotten Tomatoes"` rating among TV shows with a present `"IMDb"` rating
is a 52.

Given this information, what is the most likely missingness mechanism of
the `"IMDb"` column?

( ) Missing by design ( ) Not missing at random ( ) Missing at random (
) Missing completely at random

# END SUBPROB

# BEGIN SUBPROB

Suppose we want to perform a statistical test to determine whether the
missingness of `"IMDb"` depends on `"Age"`. Which of the following test
statistics could we use? Select all that apply.

[ ] Difference in means [ ] Absolute difference in means [ ] Total
variation distance [ ] The Kolmogorov-Smirnov statistic [ ] None of
the above

# END SUBPROB

# BEGIN SUBPROB

To determine whether the missingness of `"IMDb"` depends on `"Year"`, we
produce the following plot.

::: center
![image](midterm_images/year-imdb.png){width="70%"}
:::

Suppose we want to perform a statistical test to determine whether the
two distributions above come from the same population distribution.
Which test statistic is most likely to yield a significant result?

( ) Difference in means ( ) Absolute difference in means ( ) Total
variation distance The Kolmogorov-Smirnov statistic

# END SUBPROB

# BEGIN SUBPROB

To determine whether the missingness of `"IMDb"` depends on `"Service"`,
we produce the following plot.

::: center
![image](midterm_images/service-imdb.png){width="70%"}
:::

We'd like to fill in missing `"IMDb"` values in the fastest, most
efficient way possible, such that the mean of the imputed `"IMDb"`
column is as close to the true mean of the `"IMDb"` column in nature as
possible. Which imputation technique should we use?

( ) Unconditional mean imputation ( ) Mean imputation, conditional on
`"Service"`

Unconditional probabilistic imputation

Probabilistic imputation, conditional on `"Service"`

# END SUBPROB

# END PROB