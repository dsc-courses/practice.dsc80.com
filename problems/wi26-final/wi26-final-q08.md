# BEGIN PROB

# BEGIN SUBPROB

We suspect that some `"Provider"`s have longer `"WaitTime"`s than others. Fill in the blanks below to add a column to `med` called `"EstimatedWaitTime"` which contains the median `"WaitTime"` for appointments with the same `"Provider"`.

```py
med["EstimatedWaitTime"] = (med.groupby(__(a)__)[__(b)__]
                            .__(c)__(__(d)__))
```

1. What goes in blank (a)?

2. What goes in blank (b)?

3. What goes in blank (c)?

4. What goes in blank (d)?

# BEGIN SOLUTION

**Answers:**

1. `"Provider"`
2. `"WaitTime"`
3. `transform`
4. `np.median`

`.groupby("Provider")["WaitTime"].transform(np.median)` computes the median wait time for each provider and broadcasts it back to every row with that provider.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

We suspect that some `"Department"`s are frequently running behind schedule and may occasionally have very high wait times. Fill in the blanks below so the result is a Series, indexed by `"Department"`, containing the 95th percentile of `"WaitTime"` for each `"Department"` in which at least 75 percent of appointments have a `"Wait"`. If less than 75 percent of appointments in a given `"Department"` have a `"Wait"`, the `"Department"` should not appear in the Series. Recall that `np.percentile(x, 95)` calculates the 95th percentile of `x`.

```py
(med.groupby(__(a)__).__(b)__(__(c)__)
 .groupby(__(d)__)[__(e)__].__(f)__(__(g)__))
```

1. What goes in blank (a)?

2. What goes in blank (b)?

3. What goes in blank (c)?

4. What goes in blank (d)?

5. What goes in blank (e)?

6. What goes in blank (f)?

7. What goes in blank (g)?

# BEGIN SOLUTION

**Answers:**

1. `"Department"`
2. `filter`
3. `lambda df: df["Wait"].mean() >= 0.75`
4. `"Department"`
5. `"WaitTime"`
6. `agg`
7. `lambda s: np.percentile(s, 95)`

First, `.groupby("Department").filter(...)` keeps only departments where at least 75% of appointments have a wait. Then, group again by department and aggregate the 95th percentile of `"WaitTime"`.

# END SOLUTION

# END SUBPROB

# END PROB
