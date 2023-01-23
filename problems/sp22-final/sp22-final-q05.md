# BEGIN PROB

The DataFrame `random_10` contains the `"track_name"` and `"genre"` of
10 randomly-chosen songs in Spotify's Top 200 today, along with their
`"genre_rank"`, which is their rank in the Top 200 **among songs in
their `"genre"`**. For instance, "the real slim shady\" is the
20th-ranked Hip-Hop/Rap song in the Top 200 today. `random_10` is shown
below in its entirety.

<center><img src='../assets/images/sp22-final/imp-with-nan.png' width=35%></center>

The `"genre_rank"` column of `random_10` contains missing values. Below,
we provide four different imputed `"genre_rank"` columns, each of which
was created using a different imputation technique. On the next page,
match each of the four options to the imputation technique that was used
in the option.

<center><img src='../assets/images/sp22-final/imp-options-grid.png' width=80%></center>

Note that each option (A, B, C, D) should be used exactly once between
parts (a) and (d).

# BEGIN SUBPROB

In which option was unconditional mean imputation used?

# BEGIN SOLN

**Answer: ** Option B

Explanation given in part d) below

<average>99</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

In which option was mean imputation conditional on `"genre"`
used?

# BEGIN SOLN

**Answer: ** Option D

Explanation given in part d) below

<average>96</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

In which option was unconditional probabilistic imputation
used?

# BEGIN SOLN

**Answer: ** Option C

Explanation given in part d) below

<average>92</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

In which option was probabilistic imputation conditional on
`"genre"` used?

# BEGIN SOLN

**Answer: ** Option A

-   First, note that in Option B, all three missing values are filled in
    with the same number, 7. The mean of the observed values in
    `random_10["genre rank"]` is 7, so we must have performed
    unconditional mean imputation in Option B. (Technically, it's
    possible for Option B to be the result of unconditional
    probabilistic imputation, but we stated that each option could only
    be used once, and there is another option that can only be
    unconditional probabilistic imputation.)

-   Then note that in Option C, the very last missing value (in the
    `"Pop"` `"genre"`) is filled in with a 7, which is not the mean of
    the observed `"Pop"` values, but rather a value from the
    `"Alternative"` `"genre"`. This must mean that unconditional
    probabilistic imputation was used in Option C, since that's the only
    way a value from a different group can be used for imputation (if we
    are not performing some sort of mean imputation).

-   This leaves Option A and Option D. The last two missing values (the
    two in the `"Pop"` `"genre"`) are both filled in with the same
    value, 2 in Option A and 5 in Option D. The mean of the observed
    values for the `"Pop"` `"genre"` is $\frac{9+2+4}{3} = 5$, so mean
    imputation conditional on `"genre"` must have been used in Option D
    and thus probabilistic imputation conditional on `"genre"` must have
    been used in Option A.

<average>92</average>

# END SOLN

# END SUBPROB

In parts (e) and (f), suppose we want to run a permutation test to
determine whether the missingness of `"genre rank"` depends on
`"genre"`.

# BEGIN SUBPROB

Name a valid test statistic for this permutation test.

# BEGIN SOLN

**Answer: ** Total Variation Distance (TVD)

We are comparing two distributions:

-   The distribution of `"genre"` when `"genre rank"` is missing.

-   The distribution of `"genre"` when `"genre rank"` is not missing.

Since the distribution of `"genre"` is categorical, the above two
distributions are also categorical. The only test statistic we have for
comparing categorical distributions is the total variation distance
(TVD).

<average>63</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we conclude that the missingness of `"genre rank"`
likely **depends on** `"genre"`. Which imputation technique should we
choose if we want to preserve the variance of the `"genre rank"` column?

( ) Unconditional mean imputation
( ) Mean imputation conditional on `"genre"`
( ) Unconditional probabilistic imputation
( ) Probabilistic imputation conditional on `"genre"`

# BEGIN SOLN

**Answer: ** Option D: Probabilistic imputation conditional on `"genre"`

Mean imputation does not preserve the variance of the imputed values ---
since it fills in all missing numbers with the same number (either
overall, or within each group), the variance of the imputed dataset is
less than the pre-imputed dataset. To preserve the variance of the
imputed values, we must use probabilistic imputation of some sort. Since
the missingness of `"genre rank"` was found to be dependent on
`"genre"`, we perform probabilistic imputation **conditional** on
`"genre"`, i.e. impute `"genre rank"`s randomly within each `"genre"`.

<average>75</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

The DataFrame `trends` contains the the number of streams
yesterday (`"yest"`) and the number of streams the day before yesterday
(`"day_before_yest"`) for songs in Spotify's Top 200. Remember, a song
was in the Top 200 yesterday if it was one of the 200 most streamed
songs yesterday.

The first few rows of `trends` are shown below.

<center><img src='../assets/images/sp22-final/streams_yday.png' width=70%></center>

The `"yest"` column contains missing values. What is the most likely
missingness mechanism for `"yest"`?

( ) Missing by design
( ) Not missing at random
( ) Missing at random
( ) Missing completely at random

# BEGIN SOLN

**Answer: ** Option B: NMAR or Option C: MAR

We accepted two answers here --- not missing at random and missing at
random.

-   MCAR is ruled out right away, since there is some "pattern\" to the
    missingness, i.e. some sort of relationship between
    `"day_before_yest"` and the missingness of `"yest"`.

-   One could argue not missing at random, because stream counts are
    more likely to be missing from `"yest"` if they are smaller. A song
    is missing from `"yest"` but present in `"day_before_yest"` if its
    number of streams was in the Top 200 yesterday but not today; if
    this is true, this must mean that its number of streams is less than
    any of the songs whose stream counts are actually in `"yest"`.

-   One could also argue missing at random, because the missingness of
    `"yest"` does indeed depend on `"day_before_yest"`.

-   Missing by design is **not** a valid answer here. While it is true
    that `"day_before_yest"` tells you something about the missingness
    of `"yest"`, it is **not** the case that you can 100% of the time
    predict if `"yest"` will be missing just by looking at
    `"day_before_yest"`; this would need to be the case if `"yest"` were
    missing by design.

<average>64</average>

# END SOLN

# END SUBPROB

# END PROB