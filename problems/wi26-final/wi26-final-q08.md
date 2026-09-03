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

**Answers:** (a) `"Provider"`, (b) `"WaitTime"`, (c) `transform`, (d) `np.median`

`.groupby("Provider")["WaitTime"]` groups wait times by provider. `.transform(np.median)` computes the median wait time for each provider and broadcasts it back to every row with that provider — exactly what we need for `"EstimatedWaitTime"`.

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

**Answers:** (a) `"Department"`, (b) `filter`, (c) `lambda df: df["Wait"].mean() >= 0.75`, (d) `"Department"`, (e) `"WaitTime"`, (f) `agg` (or `aggregate` or `apply`), (g) `lambda s: np.percentile(s, 95)`

First, `.groupby("Department").filter(...)` keeps only departments where at least 75% of appointments have a wait (`"Wait"` mean $\geq 0.75$). Then we group again by `"Department"`, select `"WaitTime"`, and aggregate with the 95th percentile. Departments that fail the filter are excluded from the final Series.

# END SOLUTION

# END SUBPROB

# END PROB
