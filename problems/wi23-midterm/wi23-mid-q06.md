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

::: center
![image](midterm_images/tv-excl.png){width="80%"}
:::

# BEGIN SUBPROB

The DataFrame `counts`, shown in full below, contains the number of TV
shows for every combination of `"Age"` and `"Service"`.

::: center
![image](midterm_images/pivot.png){width="50%"}
:::

Given the above information, what does the following expression evaluate
to?

        tv_excl.groupby(["Age", "Service"]).sum().shape[0]

( ) 4 ( ) 5 ( ) 12 ( ) 16 ( ) 18 ( ) 20 ( ) 25

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

( ) Hypothesis test ( ) Permutation test

# END SUBPROB

# BEGIN SUBPROB

Consider the DataFrame `distr`, defined below.

    hn = counts[["Hulu", "Netflix"]]
    distr = (hn / hn.sum()).T  # Note that distr has 2 rows and 5 columns.

To test the hypotheses in part (b), Tiffany decides to use the total
variation distance as her test statistic. Which of the following
expressions **DO NOT** correctly compute the observed statistic for her
test? Select all that apply.

[ ] `distr.diff().iloc[-1].abs().sum() / 2` [ ]
`distr.diff().sum().abs().sum() / 2` [ ]
`distr.diff().sum().sum().abs() / 2` [ ]
`(distr.sum() - 2 * distr.iloc[0]).abs().sum() / 2` [ ]
`distr.diff().abs().sum(axis=1).iloc[-1] / 2` [ ] None of the above:
all above options correctly compute the observed statistic.

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

( ) Hypothesis test ( ) Permutation test

# END SUBPROB

# BEGIN SUBPROB

Which of Doris' interpretations are valid? Select all that apply.

[ ] Interpretation 1: If we fail to reject both null hypotheses here,
we can also fail to reject the null hypothesis in part (b). [ ]
Interpretation 2: If we reject both null hypotheses here, we can also
reject the null hypothesis in part (b). [ ] Neither interpretation is
valid.

# END SUBPROB

# END PROB