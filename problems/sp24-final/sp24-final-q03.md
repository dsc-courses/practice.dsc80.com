# BEGIN PROB

The code snippet below uses a `for` loop.

```python
mystery = 0
for i in df['id'].unique():
    temp = df[df['id'] == i]
    if temp['q'].sum() > 100:
        mystery += 1
```

# BEGIN SUBPROB

Rewrite the snippet without using any loops.

```python
mystery = (df.groupby(__(a)__)
           .__(b)__(lambda x: __(c)__)
           [__(d)__].__(e)__())
```

# BEGIN SOLN

**Answer:**

(a): `'id'`

(b): `filter`

(c): `x['q'].sum() > 100`

(d): `'id'`

(e): `nunique`

# END SOLN

# END SUBPROB



# BEGIN SUBPROB

Suppose you see the output below:

```python
>>> df['id'].value_counts()
P2955    200
P3001    150
P3125    100
Name: id, Length: 3, dtype: int64
```
Fill in the blank in the sentence below with a single number.

The code without `for` loops runs approximately _______ times faster than the code with a `for` loop.


# BEGIN SOLN

**Answer:** 3


# END SOLN

# END SUBPROB

# END PROB