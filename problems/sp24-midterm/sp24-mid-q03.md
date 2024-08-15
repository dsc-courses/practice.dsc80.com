# BEGIN PROB

Consider the following code which defines a DataFrame named `df`:

```python
def hour(df):       return df.assign(hour=df['time'].dt.hour)
def is_morning(df): return df.assign(is_morning=df['hour'] < 12)

df = (h.merge(j, left_index=True, right_on='hid', how='inner')
      .merge(o, left_on='oid', right_index=True, how='inner')
      .reset_index(drop=True)
      .pipe(hour)
      .pipe(is_morning))
```

The first few rows of df are shown below.

<center><img src="../../assets/images/sp24-midterm/df.png" width=750></center>

Suppose we define a DataFrame `p` and functions `a`, `b`, `c`, and `d` as follows:

```python
p = df.pivot_table(index='street', columns='hour', values='duration',
                   aggfunc='count', fill_value=0)

def a(n):    return p[n].sum()
def b(s):    return p.loc[s].sum()
def c():     return p.sum().sum()
def d(s, n): return p.loc[s, n]
```

Write a single expression to compute each of the probabilities below. **Your code can only use the functions `a`, `b`, `c`, `d`, and arithmetic operators (`+`, `-`, `/`, `*`).**

# BEGIN SUBPROB

The probability that a randomly selected row from `df` has the street `Mission Blvd`.

# BEGIN SOLN

**Answer:** `b('Mission Blvd') / c()`

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

The probability that a randomly selected row from `df` has the street `Gilman Dr` given that its hour is `21`.

# BEGIN SOLN

**Answer:** `d('Gilman Dr', 21) / a(21)`

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

The probability that a randomly selected row from `df` either has the street `Mission Blvd` or the hour `12`.

# BEGIN SOLN

**Answer:** `(b('Mission Blvd') + a(12) - d('Mission Blvd', 12)) / c()`

# END SOLN

# END SUBPROB

# END PROB