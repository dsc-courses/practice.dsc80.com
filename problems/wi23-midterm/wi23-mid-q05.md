# BEGIN PROB

For your convenience, the first few rows of `tv` are shown again below.

::: center
![image](midterm_images/data-info-wi23-mt.png){width="\\textwidth"}
:::

For the purposes of this question only, suppose we have also access to
another similar DataFrame, `movies`, which contains information about a
variety of movies. The information we have for each movie in `movies` is
the same as the information we have for each TV show in `tv`, except for
IMDb ratings, which are missing from `movies`.

The first few rows of `movies` are shown below (though `movies` has many
more rows than are pictured here).

::: center
![image](midterm_images/movies-dinfo-wi23-mt.png){width="\\textwidth"}
:::

# BEGIN SUBPROB

The function `total_null`, defined below, takes in a DataFrame and
returns the total number of null values in the DataFrame.

    total_null = lambda df: df.isna().sum().sum()

Consider the function `delta`, defined below.

    def delta(a, b):
        tv_a = tv.head(a)
        movies_b = movies.head(b)
        together = pd.concat([tv_a, movies_b])
        return total_null(together) - total_null(tv_a) - total_null(movies_b)

Which of the following functions is equivalent to `delta`?

( ) `lambda a, b: a` ( ) `lambda a, b: b` ( ) `lambda a, b: 9 * a` ( )
`lambda a, b: 8 * b` ( ) `lambda a, b: min(9 * a, 8 * b)`

# END SUBPROB

# BEGIN SUBPROB

Fill in the blank to complete the implementation of the function
`size_of_merge`, which takes a string `col`, corresponding to the name
of a **single** column that is shared between `tv` and `movies`, and
returns the **number of rows in** the DataFrame
`tv.merge(movies, on=col)`.

-   For instance, `size_of_merge("Year")` should return the number of
    rows in

    `tv.merge(movies, on="Year")`.

-   The purpose of this question is to have you think conceptually about
    how merges work. As such, **solutions containing `merge` or `concat`
    will receive 0 points.**

**What goes in the blank below?**

    def size_of_merge(col):
        return (____).sum()

***Hint***: Consider the behavior below.

    >>> s1 = pd.Series({'a': 2, 'b': 3})
    >>> s2 = pd.Series({'c': 4, 'a': -1, 'b': 4})
    >>> s1 * s2
    a    -2.0
    b    12.0
    c     NaN
    dtype: float64

::: responsebox
0.75in
:::

# END SUBPROB

# END PROB