# BEGIN PROB

The following function accepts a series of numbers and returns a series of the same size in which every number has been standardized (also known as "z-scored"):

```py
def standardize(ser):
    return (ser - ser.mean()) / ser.std()
```

Which of the following lines of code will return a series of standardized flipper lengths of length 330 (same as the number of rows in `df`), where the standardization is done *within each species*? That is, the flipper sizes of Adelie penguins are standardized as a group, the flipper sizes of Gentoo penguins are standardized as another group, and so on.

( ) `df.groupby('Species')['Flipper Length (mm)'].transform(standardize)`
( ) `df.groupby('Species')['Flipper Length (mm)'].aggregate(standardize)`
( ) `df.groupby('Species')['Flipper Length (mm)'].standardize()`
( ) `df.groupby('Species')['Flipper Length (mm)'].agg(standardize)`

# BEGIN SOLN
**Answer: ** Option A

Option A: We want to standardize the flipper length of EACH penguin within each group. This is done using the transform function and applying the standardize fucntion.
Option B: Aggregate is used to generate a singular value for each group (so like count of each species for example), not to apply a function to each column within each group.
Option C: We can't directly call the function standardize as our aggregate function.
Option D: This doesn't work for the same reason as Option B.

<average>93</average>

# END SOLN

# END PROB