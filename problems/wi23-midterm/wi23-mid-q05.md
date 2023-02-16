# BEGIN PROB

For your convenience, the first few rows of `tv` are shown again below.

<center><img src='../assets/images/wi23-midterm/data-info-wi23-mt.png' width=30%></center>

For the purposes of this question only, suppose we have also access to
another similar DataFrame, `movies`, which contains information about a
variety of movies. The information we have for each movie in `movies` is
the same as the information we have for each TV show in `tv`, except for
IMDb ratings, which are missing from `movies`.

The first few rows of `movies` are shown below (though `movies` has many
more rows than are pictured here).

<center><img src='../assets/images/wi23-midterm/movies-dinfo-wi23-mt.pngg' width=30%></center>

# BEGIN SUBPROB

The function `total_null`, defined below, takes in a DataFrame and
returns the total number of null values in the DataFrame.

```py
total_null = lambda df: df.isna().sum().sum()
```

Consider the function `delta`, defined below.

```py
def delta(a, b):
    tv_a = tv.head(a)
    movies_b = movies.head(b)
    together = pd.concat([tv_a, movies_b])
    return total_null(together) - total_null(tv_a) - total_null(movies_b)
```

Which of the following functions is equivalent to `delta`?

( ) `lambda a, b: a` 
( ) `lambda a, b: b` 
( ) `lambda a, b: 9 * a` 
( ) `lambda a, b: 8 * b` 
( ) `lambda a, b: min(9 * a, 8 * b)`

# BEGIN SOLN
**Answer: ** Option B

Let's understand what each function does. First, `total_null` just counts all the null values in a dataframe. Second, `delta` just takes the first a rows of `tv`, and the first b rows of ` movies`, and concatenates the two heads of each DataFrame. Then it computes the number of null values in the combined DataFrame, subtracted by the number of null values in the corresponding heads of each DataFrame. 

While this might just seem like it would be 0, we have to remember that `movies` has one less column than `tv` (the `IMDb` column), so when we concatenate `movies` to `tv`, every row from `movies` has a null value in the `IMDb` column. And these null values aren't accounted for in `total_null(movies_b)` since the `IMDb` column doesn't exist in `movies`. Thus the answer is Option B because we aren't accounting for the b null values that are generated in the `IMDb` column of the concatenated DataFrame.

# END SOLN

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

```py
def size_of_merge(col):
    return (____).sum()
```

***Hint***: Consider the behavior below.

```py
>>> s1 = pd.Series({'a': 2, 'b': 3})
>>> s2 = pd.Series({'c': 4, 'a': -1, 'b': 4})
>>> s1 * s2
a    -2.0
b    12.0
c     NaN
dtype: float64
```

# BEGIN SOLN
**Answer: `tv[col].value_counts() * movies[col].value_counts`

Essentially, by taking the `value_counts()` of each columns, we could take advantage of the product of the resulting two series. For instance, consider what happens if we had the following: 

```py
>>> s1 = pd.Series({'a': 2, 'b': 3})
>>> s2 = pd.Series({'c': 4, 'a': 1, 'b': 4})
>>> s1 * s2
a    2.0
b    12.0
c     NaN
dtype: float64
```

We could think of each series as the resulting `value_counts()` we get from the corresponding columns, and multiplying and summing would give us the number of rows in the merged DataFrame. (Note that obviously the numbers above are just an example, try to convince yourself that this is true for all such `value_counts()` Series.)

# END SUBPROB

# END PROB