# BEGIN PROB

In the next five questions, assume you have access to a DataFrame
named `pts`, shown below:

<center><img src='../assets/images/fa22-final/pts.png' width=30%></center>

# BEGIN SUBPROB

What is the type of the result of the following line of code?

`pts.groupby('group')['x'].max()`

( ) int
( ) float
( ) str
( ) pandas.Series
( ) pandas.DataFrame

# BEGIN SOLN
**Answer: ** Option D

Calling `pts.groupby('group')['x'].max()` will return a Series with the the index consisting of each of the unique groups and a column containing the max `'x'` value within each group.

<average>68</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose `z` is a pandas Series containing the data shown below:

```py
>>> z
5    20
0     1
2     3
Name: z, dtype: int64
```

Notice that the index of this Series does not match the index of `pts`.

Which of the following will be the result of running:

```py
>>> pts['z'] = z
>>> pts
```

Below are some of the options:

- Option 1: <center><img src='../assets/images/fa22-final/opt3.png' width=30%></center>
- Option 2: <center><img src='../assets/images/fa22-final/opt2.png' width=30%></center>
- Option 3: <center><img src='../assets/images/fa22-final/opt1.png' width=30%></center>

( ) Option 1
( ) Option 2
( ) Option 3
( ) An exception will be raised because `z` is missing some of the rows that are in `pts`.

# BEGIN SOLN
**Answer: ** Option 3

The code above will simply create a new column `'z'`, and match the corresponding value of `'z'` with the corresponding index of `'z'` that exists in `pts`. For the indeces in `pts` that aren't present in `'z'`, there will be a `NaN` value in the appropriate spot in the `'z'` column.

<average>97</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What is the result of the following code? 

```py
>>> pivot = pts.pivot_table(
    values='x',
    index='group',
    columns='color',
    aggfunc='count')
>>> pivot.loc['A', 'red']
```

Your answer should be in the form of a number (or possibly `NaN`).
Your answer does NOT need to be exactly what is displayed by
Python.

# BEGIN SOLN
**Answer: ** 2

The pivot table simply counts the number of rows in `pts` that have `'group'` value 'A' AND `'color'` value red, which we could see that there are only two rows that satisfy those conditions.

<average>70</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose the `costs` DataFrame contains the following data:

<center><img src='../assets/images/fa22-final/costs.png' width=25%></center>

Suppose we run:

```py
>>> res = pts.merge(costs, how='left')
```

How many rows will `res` have?

# BEGIN SOLN
**Answer: ** 6

Note that in a left merge, we retain all the rows in the left DataFrame, regardless of whether or not those rows are shared between the left and right DataFrames. Thus we also realize that it must be the case that the resulting merged DataFrame has the same number of rows as the left DataFrame when performing a left merge. Since  `'pts'` is the left DataFrame, we'll be left with 6 rows after the merge since `'pts'` has 6 rows.

<average>95</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we have defined:

```py
def foo(ser):
    return (ser - ser.min()).max()
```

What will be the result of:

```py
>>> pts.groupby('group')[['x', 'y']].aggregate(foo).loc['A', 'x']
```

Your answer should be in the form of a number.

# BEGIN SOLN
**Answer: ** 4

The `foo` function essentially takes in a Series, and returns the difference between the maximum value in the Series and the minimum value in that same Series.

Thus when we call `foo` as our aggregate function, we'll perform this `foo` function on the values of each column within each group. Also, `.loc['A', 'x']` means that we just want get the resulting `foo` value computed on column 'x' within group 'A'. Focusing our attention on the values of column 'x' that are of group 'A', we see that the largest value in 'x' of group 'A' is just 5, and the smallest value is just 1. Therefore our answer is just 5 - 1 or 4.

<average>90</average>

# END SOLN

# END SUBPROB

# END PROB
