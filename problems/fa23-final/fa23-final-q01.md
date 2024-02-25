# BEGIN PROB
(M) Fill in Python code below so that the last line of each code snippet evaluates to each desired result, using the `bus` and `stop` DataFrames describe on Page 1 of the Reference Sheet. **You may not use `for` or `while` loops in any answer for this question.**

The `bus` table (left) records bus arrivals over $1$ day for all the bust stops within a $2$ mile radius of UCSD. The data dictionary (right) describes each column.

<center><img src='../../assets/images/fa23-final/dsc80_final_bus.png' width=65%></center>

The `stop` table (left) contains information for al the bus lines in San Diego (not just the ones near UCSD). The data dictionary (right) describes each column.

<center><img src='../../assets/images/fa23-final/dsc80_final_stop.png' width=65%></center>
# BEGIN SUBPROB

Compute the median minutes late for the $101$ bus.
`bus.loc[____].median()`
# BEGIN SOLN

**Answer**: `bus.loc[bus['line'] == 101, 'late'].median()`

`.loc[]` will grab the rows of the first parameter and columns of the second parameter. In this case, we want all the rows that belong to bus $101$, so we filter by `bus['line'] == 101`. We then want to see how late the buses are, so we grab the `'late'` column in the second parameter.

<average>72</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Compute a copy of `bus` with only the bus lines that made at least one stop containing the string 'Myers Ln'.

```
def f(x):
	return ____
bus.groupby(____).____(f)
```
# BEGIN SOLN
**Answer**:  
```
def f(x):
	return any(x['stop'].str.contains('Meyers Ln'))
bus.groupby('line').filter(f)
```
We can start with the bottom `groupby` function because we know we are asked to look per bus line, so we want to aggregate the data by 'line'. Then, since we are going to make a copy of the original DataFrame with only the bus lines meeting our criteria, `filter` will keep rows that meet what we want. Then, we just need to define our criteria in `f(x)`, which is that the rows of data, `x`, have a stop containing the string 'Myers Ln'. This can be done by looking at the `'stop'` column and using the Series string functions to check across all values if the string 'Meyers Ln' is included with `.str.contains('Meyers Ln')`. This will return a boolean Series, and we can check if "at least one" stop contains the string by passing the boolean Series into the `any` function. This will then return `True` or `False`, which determines if that bus line is kept in our computed DataFrame.

<average>58</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Compute the number of buses in `bus` whose next stop is 'UTC'.
```
x = stop.merge(____, on = ____, how = ____)
x[____].shape[0]
```
# BEGIN SOLN
**Answer**:
```
x = stop.merge(bus, on = ['line', 'stop'], how = 'inner')
x[x['next'] == 'UTC'].shape[0]
```
OR
```
x = stop.merge(bus, on = ['line', 'stop'], how = 'right')
x[x['next'] == 'UTC'].shape[0]
```
OR
```
x = stop.merge(bus, on = ['line', 'stop'], how = 'left')
x[(x['next'] == 'UTC') & (~x['time'].isna())].shape[0]
```
OR
```
x = stop.merge(bus, on = 'line', how = 'left')
x[(x['next'] == 'UTC') & (x['stop_x'] == x['stop_y'])].shape[0]
```
The top solution is our internal solution, the additional three are student solutions that we also accepted.
First, we merge the `stop` DataFrame with the `bus` DataFrame because the question specifically wants to know about the number of buses from the `bus` DataFrame. We want to merge on both `'line'` and `'stop'` because we need to find the number of bus lines that are at a specific stop. We then choose to do an inner merge, but a right merge has the same effect because the buses in `bus` are all in the scope of `stop`, but `stop` has extra bus lines we don't care about for this question. Finally, we filter our DataFrame `x` by checking which `['line', 'stop']` combinations are headed to 'UTC' next by looking at the `'next'` column.

<average>64</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Computer the number of unique pairs of bust stops that are exactly two stops away from each other. For example, if you only use the first four rows of the `stop` table, then your code should evaluate to the numebr $2$, since you can go from 'Gilman Dr & Mandeville Ln' to 'La Jolla Village Dr & Lebon Dr' and from 'Gilman Dr & Mandeville Ln' to 'Villa La Jolla Dr & Holidat Ct' in two stops.
_Hint_: The `suffixes = (1, 2)` argument to `merge` appends a $1$ to column labels in the left table and a $2$ to column labels in the right table whenever the merged tables share column labels.

```
m = ____.merge(____, left_on = ____, right_on = ____, how = ____, suffixes = (1, 2))
(m[____].drop_duplicates().shape[0])
```
# BEGIN SOLN
**Answer**:
```
m = stop.merge(stop, left_on = 'next', right_on = 'stop', how = 'inner', suffixes = (1, 2))
(m[['stop1', 'next2']].drop_duplicates().shape[0])
```
We want to look at all stops in San Diego, so we will not be using the `bus` DataFrame for this question. Instead, we will merge `stop` with itself, but on the left we will merge on the `'next'` column, and on the right we will merge on the `'stop'` column. This means we get the first stop on the left DataFrame, the next stop from the left DataFrame matching with the right DataFrame, and then the next stop from the right DataFrame. That results in the `'stop'` column of the left DataFrame being $2$ stops away from the `'next'` column of the right DataFrame. That means all we need to do is use an `inner` merge to drop any stops that do not have a match $2$ stops away. 
Since we are now left with a DataFrame of stops that we want, we just grab the correctly formatted output by selecting the `['stop1', 'next2']` columns from `m`, recalling that we use $1$ and $2$ to distinguish the columns from the left and right DataFrames.

<average>54</average>

# END SOLN
# END SUBPROB
# END PROB