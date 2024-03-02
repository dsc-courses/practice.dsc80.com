# BEGIN PROB

In this question only, assume that there are more than 12 districts in `dogs`.

Suppose we merge the `dogs` DataFrame with itself as follows.

```py
# on="x" is the same as specifying both left_on="x" and right_on="x".
double = dogs.merge(dogs, on="district")

# sort_index sorts a Series in increasing order of its index.
square = double["district"].value_counts().value_counts().sort_index()
```

The first few rows of `square` are shown below.

```py
1     5500
4      215
9       40
```

# BEGIN SUBPROB

In `dogs`, there are 12 rows with a `"district"` of `8`. How many rows
of `double` have a `"district"` of `8`? Give your answer as a positive
integer.

# BEGIN SOLUTION

**Answer**: $144$

When we merge `dogs` with `dogs` on `"district"`, each `8` in the first `dogs` DataFrame will be combined with each `8` in the second `dogs` DataFrame. Since there are 12 in the first and 12 in the second, there are $12 \cdot 12 = 144$ combinations.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What does the following expression evaluate to? Give your answer as a
positive integer.

```py
dogs.groupby("district").filter(lambda df: df.shape[0] == 3).shape[0]
```

*Hint: Unlike in 5.1, your answer to 5.2 depends on the values
in `square`.*

# BEGIN SOLUTION

**Answer**: $120$

`square` is telling us that:
- There are 5500 districts that appeared just 1x in `dogs`.
- There are 215 districts that appeared 2x in `dogs` (2x, not 4x, because of the logic explained in the 5a rubric item).
- There are 40 districts that appeared 3x in `dogs`.

The expression given in this question is keeping all of the rows corresponding to districts that appear 3 times. There are 40 districts that appear 3 times. So, the total number of rows in this DataFrame is $40 \cdot 3 = 120$.

# END SOLUTION

# END SUBPROB

# END PROB