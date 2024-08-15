# BEGIN PROB

Fill in Python code below so that the last line of each part evaluates to each desired result using the tables `h`, `o`, and `j` as shown on the Reference Sheet.

# BEGIN SUBPROB

Find the median duration of outages that happened in the early morning (before 8am).

```python
o.loc[__(a)__,__(b)__].median()
```

# BEGIN SOLN

**Answer:** 

(a): `o['time'].dt.hour < 8`

(b): `'duration'`

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

A Series containing the mean outage duration for outages that happened on the weekend and outages that happened on weekdays.

*Hint: If `s` is a Series of timestamps, `s.dt.dayofweek` returns a Series of integers where 0 is Monday and 6 is Sunday.*

```python
(o.assign(__(a)__)
.groupby(__(b)__)[__(c)__].mean())
```

# BEGIN SOLN

**Answer:** 

(a): `is\_weekend=o['time'].dt.dayofweek >= 5`

(b): `'is\_weekend'`, (c): `'duration'`

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

A DataFrame containing the proportion of 4-digit address numbers for each unique street in `h`.

```python
def foo(x):
    lengths = __(a)__
    return (lengths == 4).mean()

h.groupby(__(b)__).__(c)__(foo)
```

# BEGIN SOLN

**Answer:** 

(a): `x.astype(str).str.len()`

(b): `'street'`

(c): `agg`

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

What does the following code compute?

```python
a = h.merge(j, left_index=True, right_on='hid', how='left')
a.loc[a['oid'].isna(), 'hid'].shape[0]
```

( ) The number of addresses with exactly one outage.  
( ) The number of addresses with at least one outage.  
( ) The number of addresses with no outages.  
( ) The total number of addresses affected by all power outages.  
( ) The number of power outages.  
( ) The number of power outages that affected exactly one address.  
( ) The number of power outages that affected at least one address.  
( ) The number of power outages that affected no addresses.  
( ) 0  
( ) The code will raise an error.  
( ) None of the above.  



# BEGIN SOLN

**Answer:** The number of addresses with no outages.

# END SOLN

# END SUBPROB

# END PROB