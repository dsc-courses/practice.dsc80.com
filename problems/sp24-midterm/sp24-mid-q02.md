# BEGIN PROB

# BEGIN SUBPROB

Consider the following code:

```python
whoa = (h.merge(j, left_index=True, right_on='hid', how='left')
        .merge(o, left_on='oid', right_index=True, how='right')
        .reset_index(drop=True))
```

Consider the following variables:

```python
a = j['hid'] <= 50
b = j['hid'] > 50
c = j['oid'] <= 100
d = j['oid'] > 100
e = (j[j['hid'] <= 50]
     .groupby('hid')
     .filter(lambda x: all(x['oid'] > 100))
     ['hid']
     .nunique())
f = (j[j['oid'] <= 100]
     .groupby('oid')
     .filter(lambda x: all(x['hid'] > 50))
     ['oid']
     .nunique())
g = len(set(h.index) - set(j['hid']))
i = len(set(o.index) - set(j['oid']))
```

Write a **single expression** that evaluates to the number of rows in `whoa`. In your code, you may only use the variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, `i` as defined above, arithmetic and bitwise operators (`+`, `-`, `/`, `*`, `&`, `|`), and the `np.sum()` function. **You may not use any other variables or functions.** Your code might not need to use all of the variables defined above.


# BEGIN SOLN

**Answer:** `np.sum(a & c) + f + i`

We know that `h` has the numbers 1-50 as unique integers in its index, and `o` has the numbers 1-100 as unique integers in its index. However, the `hid` and `oid` columns in `j` have values outside these ranges. To approach this problem, it's easiest to come up with smaller versions of `h`, `j`, and `o`, then perform the join by hand. For example, consider the following example `h`, `j`, and `o` tables:

| **hid** |
|---------|
| 1       |
| 2       |
| 3       |

---

| **hid** | **oid** |
|---------|---------|
| 1       | 1       |
| 2       | 1       |
| 2       | 10      |
| 2       | 11      |
| 10      | 3       |
| 11      | 3       |

---

| **oid** |
|---------|
| 1       |
| 2       |
| 3       |


In this example, `whoa` would look like the following (omitting other columns besides `hid` and `oid` for brevity):

| **hid** | **oid** |
|---------|---------|
| 1       | 1       |
| 2       | 1       |
| NaN     | 2       |
| NaN     | 3       |

There are 3 cases where rows will be kept for `whoa`:

1. When both `hid` and `oid` match in the three tables (when `a` and `c` are both true). In the example above, this corresponds to the first two rows of `whoa`.
2. When the `oid` in `o` doesn't appear at all in `j` (calculated by `i`). In the example above, this corresponds to the third row of `whoa`.
3. When the `oid` in `o` does appear in `j`, but none of the `hid` values appear in `h` (calculated by `f`). In the example above, this corresponds to the fourth row of `whoa`.

Therefore, the number of rows in `whoa` is:

```python
np.sum(a & c) + f + i
```

# END SOLN

# END SUBPROB

# END PROB