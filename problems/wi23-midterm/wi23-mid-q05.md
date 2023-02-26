# BEGIN PROB

For your convenience, the first few rows of `tv` are shown again below.

<center><img src='../assets/images/wi23-midterm/data-info-wi23-mt.png' width=65%></center>

For the purposes of this question only, suppose we have also access to
another similar DataFrame, `movies`, which contains information about a
variety of movies. The information we have for each movie in `movies` is
the same as the information we have for each TV show in `tv`, except for
IMDb ratings, which are missing from `movies`.

The first few rows of `movies` are shown below (though `movies` has many
more rows than are pictured here).

<center><img src='../assets/images/wi23-midterm/movies-dinfo-wi23-mt.png' width=65%></center>

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

**Answer**: `lambda a, b: b`

Let's understand what each function does. 

- `total_null` just counts all the null values in a DataFrame. 
- `delta` concatenates the first `a` rows of `tv` with the first `b` rows of `movies` **vertically**, that is, on top of one another (over axis 0). It then returns the difference between the total number of null values in the concatenated DataFrame and the total number of null values in the first `a` rows of `tv` and first `b` rows of `movies` – in other words, it returns **the number of null values that were added as a result of the concatenation**.

The key here is recognizing that `tv` and `movies` have all of the same column names, **except** `movies` doesn't have an `"IMDb"` column. As a result, when we concatenate, the `"IMDb"` column will contain null values for every row that was originally from `movies`. Since `b` rows from `movies` are in the concatenated DataFrame, `b` new null values are introduced as a result of the concatenation, and thus `lambda, a, b: b` does the same thing as `delta`.

<average>58</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Fill in the blank to complete the implementation of the function
`size_of_merge`, which takes a string `col`, corresponding to the name
of a **single** column that is shared between `tv` and `movies`, and
returns the **number of rows in** the DataFrame
`tv.merge(movies, on=col)`.

-   For instance, `size_of_merge("Year")` should return the number of
    rows in `tv.merge(movies, on="Year")`.

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

**Answer**: `tv[col].value_counts() * movies[col].value_counts()`

`tv.merge(movies, on=col)` contains one row for every "match" between `tv[col]` and `movies[col]`. Suppose, for example, that `col="Year"`. If `tv["Year"]` contains 30 values equal to 2019, and `movies["Year"]` contains 5 values equal to 2019, `tv.merge(movies, on="Year")` will contain $30 \cdot 5 = 150$ rows in which the `"Year"` value is equal to 2019 – one for every combination of a 2019 row in `tv` and a 2019 row in `movies`.

`tv["Year"].value_counts()` and `movies["Year"].value_counts()` contain, respectively, the frequencies of the unique values in `tv["Year"]` and `movies["Year"]`. Using the 2019 example from above, `tv["Year"].value_counts() * movies["Year"].value_counts()` will contain a row whose index is 2019 and whose value is 150, with similar other entries for the other years in the two Series. (The hint is meant to demonstrate the fact that no matter how the two Series are sorted, the product is done element-wise by matching up indexes.) Then, `(tv["Year"].value_counts() * movies["Year"].value_counts()).sum()` will sum these products across all years, ignoring null values. 

As such, the answer we were looking for is `tv[col].value_counts() * movies[col].value_counts()` (remember, `"Year"` was just an example for this explanation).

<average>14</average>

# END SOLN

# END SUBPROB

# END PROB