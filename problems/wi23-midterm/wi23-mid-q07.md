# BEGIN PROB

The `"IMDb"` column in `tv_excl` contains several missing values.

***Note***: Answer each subpart of this question independently of other
subparts.

# BEGIN SUBPROB

Given no other information other than a TV show's `"Title"` and `"IMDb"`
rating, what is the most likely missingness mechanism of the `"IMDb"`
column?

( ) Missing by design 
( ) Not missing at random 
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN

**Answer**:

- Full credit: Not missing at random
- Partial credit: Missing completely at random

The answer we were looking for is not missing at random (NMAR). As we saw repeatedly in lectures and Lab 5, in cases where all we have access to is a single column with missing values, potentially with other unrelated columns (like `"Title"` here), the best explanation is that there is some inherent reason as to why the values in the column with missing values are missing. Here, a reasonable interpretation is that the `"IMDb"` scores that are missing are likely to come from worse TV shows, and so lower scores are more likely to be missing. Think about it like this – if a TV show is really great, presumably more people would know about it, and it would be rated. If a TV show wasn't as good and wasn't as popular, it is more likely to be ignored.

However, partial credit was awarded to those who answered missing completely at random.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Now, suppose we discover that the median `"Rotten Tomatoes"` rating
among TV shows with a missing `"IMDb"` rating is a 13, while the median
`"Rotten Tomatoes"` rating among TV shows with a present `"IMDb"` rating
is a 52.

Given this information, what is the most likely missingness mechanism of
the `"IMDb"` column?

( ) Missing by design 
( ) Not missing at random 
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN

**Answer**: Missing at random

The problem tells us that the distribution of `"Rotten Tomatoes"` when `"IMDb"` is missing (mean 13) is very different from the distribution of `"Rotten Tomatoes"` when `"IMDb"` is not missing (mean 52). As such, the missingness of `"IMDb"` appears to depend on `"Rotten Tomatoes"`, and so the most likely missingness mechanism is missing at random.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we want to perform a statistical test to determine whether the
missingness of `"IMDb"` depends on `"Age"`. Which of the following test
statistics could we use? Select all that apply.

[ ] Difference in means
[ ] Absolute difference in means
[ ] Total variation distance
[ ] The Kolmogorov-Smirnov statistic
[ ] None of the above

# BEGIN SOLN

**Answer**: Total variation distance only

Our permutation test here needs to compare two distributions:

- The distribution of `"Age"` when `"IMDb"` is missing.
- The distribution of `"Age"` when `"IMDb"` is not missing.

Since `"Age"` is a categorical variable – remember, its only possible values are `"7+"`, `"13+"`, `"16+"`, `"18+"`, and `"all"` – the above two distributions are categorical. The only test statistic of the options provided that compares categorical distributions is the total variation distance.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

To determine whether the missingness of `"IMDb"` depends on `"Year"`, we
produce the following plot.

<center><img src='../assets/images/wi23-midterm/year-imdb.png' width=50%></center>

Suppose we want to perform a statistical test to determine whether the
two distributions above come from the same population distribution.
Which test statistic is most likely to yield a significant result?

( ) Difference in means
( ) Absolute difference in means
( ) Total variation distance
( ) The Kolmogorov-Smirnov statistic

# BEGIN SOLN

**Answer**: The Kolmogorov-Smirnov statistic

First, note that the two distributions are quantitative, which means the TVD can't be used here (the TVD only measures the difference between two categorical distributions).

To decide between the remaining options, note that the two distributions visualized appear to have the same mean, but different shapes. The Kolmogorov-Smirnov statistic is designed to detect differences in the shapes of distributions with the same center, and as such, it is the most likely to yield a significant result here. The others may not; since the means of the two distributions are very similar, the observed difference in means will be close to 0, which is a typical value under the null.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

To determine whether the missingness of `"IMDb"` depends on `"Service"`,
we produce the following plot.

<center><img src='../assets/images/wi23-midterm/service-imdb.png' width=50%></center>

We'd like to fill in missing `"IMDb"` values in the fastest, most
efficient way possible, such that the mean of the imputed `"IMDb"`
column is as close to the true mean of the `"IMDb"` column in nature as
possible. Which imputation technique should we use?

( ) Unconditional mean imputation 
( ) Mean imputation, conditional on `"Service"`
( ) Unconditional probabilistic imputation
( ) Probabilistic imputation, conditional on `"Service"`

# BEGIN SOLN

Since the missingness of `"IMDb"` appears to depend on `"Service"`, in order to accurately estimate the true mean of the `"IMDb"` column, we must impute conditionally on `"Service"`, otherwise the imputed mean will be biased.

To decide between conditional mean imputation and conditional probabilistic imputation, note that we were asked to find the **fasted, most efficient** technique possible, such that the imputed mean is close to the true mean. Conditional mean imputation is more efficient than conditional probabilistic imputation, as probabilistic imputation requires sampling. While mean imputation shrinks the variance of the imputed distribution relative to the true distribution, we weren't asked to preserve the variance of the true distribution, so conditional mean imputation is the right choice.

# END SOLN

# END SUBPROB

# END PROB