# BEGIN PROB

Define `small_students` to be the DataFrame with 8 rows and 2 columns
shown directly below, and define `districts` to be the DataFrame
with 3 rows and 2 columns shown below `small_students`.

<center><img src='../assets/images/sp22-midterm/small_students.png' width=30%></center>
<center><img src='../assets/images/sp22-midterm/districts.png' width=30%></center>

Consider the DataFrame `merged`, defined below.

```py
merged = small_students.merge(districts, 
                                left_on="High School", 
                                right_on="school", 
                                how="outer")
```

# BEGIN SUBPROB

How many total `NaN` values does `merged` contain? Give your answer as
an integer.

# BEGIN SOLN

**Answer: **4

`merged` is shown below.

<center><img src='../assets/images/sp22-midterm/merge-ans-1.png' width=45%></center>

<average>13</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider the DataFrame `concatted`, defined below.

    concatted = pd.concat([small_students, districts], axis=1)

How many total `NaN` values does `concatted` contain? Give your answer
as an integer.

*Hint: Draw out what `concatted` looks like. Also, remember that the
default `axis` argument to `pd.concat` is `axis=0`.*

# BEGIN SOLN

**Answer: **10

`concatted` is shown below.

<center><img src='../assets/images/sp22-midterm/merge-ans-2.png' width=45%></center>

<average>76</average>

# END SOLN

# END SUBPROB

# END PROB