# BEGIN PROB

Weiyue proposes the following imputation scheme.

```py
    def impute(s):
        return s.fillna(np.random.choice(s[s.notna()]))
```

# BEGIN SUBPROB

**True or False:** `impute` performs probabilistic imputation, using the same definition of probabilistic imputation we learned about in class.

( ) True
( ) False

# BEGIN SOLUTION

**Answer:** False

In `impute`, `np.random.choice` will return a single non-null value from `s`, and `.fillna()` will fill every null value with this single value. Meanwhile, probabilistic imputation draws a different value from a specified distribution to fill each missing value, making it such that there won't be a single "spike" in the imputed distribution at a single chosen value.

<average>41</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the following expressions and values.

```
    >>> vals.isna().mean()
    0.2
    >>> vals.describe().loc[["min", "mean", "max"]]
    min     2.0
    mean    4.0
    max     7.0
    dtype: float64
```

Given the above, what is the **maximum** possible value of `impute(vals).mean()`?
Give your answer as a number rounded to one decimal place.

# BEGIN SOLUTION

**Answer:** 4.6

The maximum possible value of `impute(vals).mean()` would occur when every single missing value in `vals` is filled in with the highest possible non-null value in `vals`. (As discussed in the previous solution, `impute` selects only one value from `s` to fill into every missing space.)

If this occurs, then the mean of the imputed Series will be weighted mean of the available data and the filled data, and given the numbers in the question, this is $0.8 \cdot 4 + 0.2 \cdot 7$, or 4.6.

<average>50</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Which of the following statements below will always evaluate to `True`?

( ) `vals.std() < impute(vals).std()`
( ) `vals.std() <= impute(vals).std()`
( ) `vals.std() == impute(vals).std()`
( ) `vals.std() >= impute(vals).std()`
( ) `vals.std() > impute(vals).std()`
( ) None of the above

# BEGIN SOLUTION

**Answer:** None of the above

Since the value which `impute()` will choose to impute with is random, the effect that it has on the standard deviation of `vals` is unknown. If the missing values are filled with a value close to the mean, this could reduce standard deviation; if they are filled with a value far from the mean, this could increase standard deviation. (Of course, the imputation will also shift the mean, so without knowing details of the Series, it's impossible to come up with thresholds.) In any case, since the value for imputation is chosen at random, none of these statements will *always* be true, and so the correct answer is "none of the above."

<average>38</average>

# END SOLUTION

# END SUBPROB

# END PROB





