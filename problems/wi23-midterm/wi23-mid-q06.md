# BEGIN PROB

For the remainder of the exam, we will only consider TV shows that are
available to stream *exclusively* on a single streaming service. The
DataFrame `tv_excl` contains all of the information we have for these TV
shows. Note that instead of containing separate columns for each
streaming service, as `tv` did, `tv_excl` instead has a single
`"Service"` column that contains the name of the one streaming service
that the TV show is available for streaming on.

The first few rows of `tv_excl` are shown below (though, of course,
`tv_excl` has many more rows than are pictured here). Note that *Being
Erica* is not in `tv_excl`, since it is available to stream on multiple
services.

<center><img src='../assets/images/wi23-midterm/tv-excl.png' width=65%></center>


# BEGIN SUBPROB

The DataFrame `counts`, shown in full below, contains the number of TV
shows for every combination of `"Age"` and `"Service"`.

<center><img src='../assets/images/wi23-midterm/pivot.png' width=40%></center>

Given the above information, what does the following expression evaluate
to?

```py
tv_excl.groupby(["Age", "Service"]).sum().shape[0]
```

( ) 4 
( ) 5 
( ) 12
( ) 16
( ) 18
( ) 20
( ) 25

# BEGIN SOLN

**Answer**: 18

Note that the DataFrame `counts` is a pivot table, created using `tv_excl.pivot_table(index="Age", columns="Service", aggfunc="size")`. As we saw in lecture, pivot tables contain the same information as the result of grouping on two columns.

The DataFrame `tv_excl.groupby(["Age", "Service"]).sum()` will have one row for every unique combination of `"Age"` and `"Service"` in `tv_excl`. (The same is true even if we used a different aggregation method, like `.mean()` or `.max()`.) As `counts` shows us, `tv_excl` contains every possible combination of a single element in {`"13+"`, `"16+"`, `"18+"`, `"7+"`, `"all"`} with a single element in {`"Disney+"`, `"Hulu"`, `"Netflix"`, `"Prime Video"`}, except for (`"13+"`, `"Disney+"`) and (`"18+"`, `"Disney+"`), which were not present in `tv_excl`; if they were, they would have non-null values in `counts`. 

As such, `tv_excl.groupby(["Age", "Service"]).sum()` will have $20 - 2 = 18$ rows, and `tv_excl.groupby(["Age", "Service"]).sum().shape[0]` evaluates to 18.

<average>34</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Tiffany would like to compare the distribution of `"Age"` for Hulu and
Netflix. Specifically, she'd like to test the following hypotheses:

-   **Null Hypothesis**: The distributions of `"Age"` for Hulu and
    Netflix are drawn from the same population distribution, and any
    observed differences are due to random chance.

-   **Alternative Hypothesis**: The distributions of `"Age"` for Hulu
    and Netflix are drawn from different population distributions.

What type of test is this?

( ) Hypothesis test
( ) Permutation test

# BEGIN SOLN

**Answer**: Permutation test

A permutation test is a statistical test in which we aim to determine if two samples look like they were drawn from the same unknown population. Here, our two samples are the distribution of `"Age"`s for Hulu and the distribution of `"Age"`s for Netflix.

<average>97</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider the DataFrame `distr`, defined below.

```py
hn = counts[["Hulu", "Netflix"]]
distr = (hn / hn.sum()).T  # Note that distr has 2 rows and 5 columns.
```

To test the hypotheses in part (b), Tiffany decides to use the total
variation distance as her test statistic. Which of the following
expressions **DO NOT** correctly compute the observed statistic for her
test? Select all that apply.

[ ] `distr.diff().iloc[-1].abs().sum() / 2`
[ ] `distr.diff().sum().abs().sum() / 2` 
[ ] `distr.diff().sum().sum().abs() / 2`
[ ] `(distr.sum() - 2 * distr.iloc[0]).abs().sum() / 2`
[ ] `distr.diff().abs().sum(axis=1).iloc[-1] / 2`
[ ] None of the above: all above options correctly compute the observed statistic.

# BEGIN SOLN

**Answer**: `distr.diff().sum().sum().abs() / 2` only

First, note that the difference between the TVD calculation here and those in lecture is that our pivot table contains one **row** for each distribution, rather than one **column** for each distribution. This is because of the `.T` in the code snippet above. `distr` may look something like:

<center><img src='../assets/images/wi23-midterm/distr.png' width=50%></center>

<br>

As such, here we need to apply the `.diff()` method to each column first, not each row (meaning we should supply `axis=0` to `diff`, not `axis=1`; `axis=0` is the default, so we don't need to explicitly specify it). `distr.diff()` may look something like:

<center><img src='../assets/images/wi23-midterm/distr-diff.png' width=50%></center>

<br>

With that in mind, let's look at each option, remembering that the TVD is the **sum of the absolute differences in proportions, divided by 2**.

- `distr.diff().iloc[-1].abs().sum() / 2`: 
    - `distr.diff().iloc[-1]` contains the differences in proportions. 
    - `distr.diff().iloc[-1].abs()` contains the absolute differences in proportions.
    - `distr.diff().iloc[-1].abs().sum() / 2` contains the sum of the absolute differences in proportions, divided by 2. **This is the TVD.**
- `distr.diff().sum().abs().sum() / 2`: 
    - `distr.diff().sum()` is a Series containing just the last row in `distr.diff()`; remember, null values are ignored when using methods such as `.mean()` and `.sum()`.
    - `distr.diff().sum().abs()` contains the absolute differences in proportions, and hence `distr.diff().sum().abs().sum() / 2` contains the sum of the absolute differences in proportions, divided by 2. **This is the TVD.**
- `distr.diff().sum().sum().abs() / 2`:
    - `distr.diff().sum()` contains the differences in proportions (explained above).
    - `distr.diff().sum().sum()` contains the sum of the differences in proportions. **This is 0**; remember, the reason we use the absolute value is to prevent the positive and negative differences in proportions from cancelling each other out. As a result, this option **does not compute the TVD**; in fact, it errors, because `distr.diff().sum().sum()` is a single `float`, and `float`s don't have an `.abs()` method.
- `(distr.sum() - 2 * distr.iloc[0]).abs().sum() / 2`:
    - This option seems strange, but does actually compute the TVD. The key idea is the fact that $a - b$ is the same as $(a + b) - 2 \cdot b)$. `distr.sum()` is the same as `distr.iloc[0] + distr.iloc[1]`, so `distr.sum() - 2 * distr.iloc[0]` is `distr.iloc[0] + distr.iloc[1] - 2 * distr.iloc[0]` which is `distr.iloc[1] - distr.iloc[0]`, which is just `distr.diff().iloc[-1]`.
    - Then, this option reduces to `distr.diff().iloc[-1].abs().sum() / 2`, which is the same as Option 1. **This is the TVD.**
- `distr.diff().abs().sum(axis=1).iloc[-1] / 2`:
    - `distr.diff().abs()` is a DataFrame in which the last row contains the absolute differences in proportions.
    - `distr.diff().abs().sum(axis=1)` is a Series in which the first element is null and the second element is the sum of the absolute differences in proportions.
    - As such, `distr.diff().abs().sum(axis=1).iloc[-1] / 2` is the sum of the absolute differences in proportions divided by 2. **This is the TVD.**

<average>67</average>

# END SOLN

# END SUBPROB

Doris proposes a novel approach for testing the hypotheses in part (b).
She proposes we compute the distribution of `"Age"` for all TV shows in
`tv_excl`, ignoring the streaming service they're available on. Then,
she suggests we run two separate tests of the following hypotheses,
using the same significance level as used for the tests in part (b):

-   **Null Hypothesis**: The distribution of `"Age"` for service $X$ is
    drawn from the distribution of `"Age"` for all services we have data
    for.

-   **Alternative Hypothesis**: The distribution of `"Age"` for service
    $X$ is not drawn from the distribution of `"Age"` for all services
    we have data for.

She suggests we test the above pair of hypotheses separately for Hulu
and Netflix, and gives the following interpretations:

1.  If we fail to reject both null hypotheses here, we can also fail to
    reject the null hypothesis in part (b).

2.  If we reject both null hypotheses here, we can also reject the null
    hypothesis in part (b).

# BEGIN SUBPROB

What type of test is Doris proposing we run?

( ) Hypothesis test 
( ) Permutation test

# BEGIN SOLN

**Answer**: Hypothesis test

A hypothesis test is a statistical test in which we aim to determine whether a sample looks like it was drawn at random from a known population. Here, Doris is proposing we run two separate hypothesis tests: one in which we determine whether the distribution of `"Age"` for Hulu (sample) is drawn from the distribution of `"Age"` in our entire dataset (population), and one in which we determine whether the distribution of `"Age"` for Netflix (sample) is drawn from the distribution of `"Age"` in our entire dataset (population).

<average>93</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Which of Doris' interpretations are valid? Select all that apply.

[ ] Interpretation 1: If we fail to reject both null hypotheses here, we can also fail to reject the null hypothesis in Problem 6.2.
[ ] Interpretation 2: If we reject both null hypotheses here, we can also reject the null hypothesis in Problem 6.2.
[ ] Neither interpretation is valid.

# BEGIN SOLN

**Answer**: Interpretation 1 only

Let's consider each option.

- **Interpretation 1**: Suppose we fail to reject both null hypotheses here. If that's the case, then the distribution of `"Age"` for Hulu _looks_ like a random sample from the distribution of `"Age"` in our full dataset, and so does the distribution of `"Age"` for Netflix. (Note that we can't conclude they _are_ random samples from the distribution of `"Age"` in our full dataset, since we can't prove the null, we can only fail to reject it). If that's the case, the distributions of `"Age"` for Hulu and Netflix both look like they're drawn from the same population, which means we fail to reject the null from Problem 6.2.
- **Interpretation 2**: Suppose we reject both null hypotheses here. If that's the case, then neither the distribution of `"Age"` for Hulu nor the distribution of `"Age"` for Netflix look like a random sample of `"Age"` in our full dataset. However, that doesn't imply that these two distributions don't look like samples of the same population; all it implies is that they don't look like samples of this particular population. It is still possible that there exists some population distribution that the distributions of `"Age"` for Hulu and Netflix both look like they're drawn from, which means we can't automatically reject the null from Problem 6.2.

<average>60</average>

# END SOLN

# END SUBPROB

# END PROB