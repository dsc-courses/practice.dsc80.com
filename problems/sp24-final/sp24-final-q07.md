# BEGIN PROB

Suppose that `df` doesn't have any missing data in the `cost` column.
Sam accidentally loses values from the `cost` column and values are more
likely to be missing for `states` with expensive purchases. Sam's data
is stored in a DataFrame called `missing`.

To recover the missing values, Sam applies the imputation methods below to the
`cost` column in `missing`, then recalculates the mean of the
`cost` column. For each imputation method, choose whether the new mean will
be lower (-), higher (+), exactly the same (=), or approximately the same ($\approx$)
as the original mean of the `cost` column in `df` (the data without any missing observations).


# BEGIN SUBPROB

```python
missing['cost'].fillna(missing['cost'].mean())
```

( ) -  
( ) +  
( ) =  
( ) $\approx$

# BEGIN SOLN

**Answer:** -

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

```python
def mystery(s):
    return s.fillna(s.mean())
missing.groupby('state')['cost'].transform(mystery).mean()
```

( ) -  
( ) +  
( ) =  
( ) $\approx$

# BEGIN SOLN

**Answer:** $\approx$

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

```python
def mystery2(s):
    s = s.copy()
    n = s.isna().sum()
    fill_values = np.random.choice(s.dropna(), n)
    s[s.isna()] = fill_values
    return s

missing.groupby('state')['cost'].transform(mystery2).mean()
```

( ) -  
( ) +  
( ) =  
( ) $\approx$

# BEGIN SOLN

**Answer:** $\approx$

# END SOLN

# END SUBPROB

# END PROB