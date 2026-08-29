# BEGIN PROB

# BEGIN SUBPROB

We suspect that some `"Provider"`s have longer `"WaitTime"`s than
others. Fill in the blanks below to add a column to `med` called
`"EstimatedWaitTime"` which contains the median `"WaitTime"` for
appointments with the same `"Provider"`.

    med["EstimatedWaitTime"] = (med.groupby(__(a)__)[__(b)__]
                                   .__(c)__(__(d)__))

  -------- --------
  `(a)`:   `(b)`:
  `(c)`:   `(d)`:
  -------- --------

# BEGIN SOLUTION

**Answer:** '\"Provider\"\`

**Answer:** '\"WaitTime\"\`

**Answer:** 'transform'

**Answer:** 'np.median'

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

We suspect that some `"Department"`s are frequently running behind
schedule and may occasionally have very high wait times. Fill in the
blanks below so the result is a Series, indexed by `"Department"`,
containing the 95th percentile of `"WaitTime"` for each `"Department"`
in which at least 75 percent of appointments have a `"Wait"`. If less
than 75 percent of appointments in a given `"Department"` have a
`"Wait"`, the `"Department"` should not appear in the Series. Recall
that `np.percentile(x, 95)` calculates the 95th percentile of `x`.

        (med.groupby(__(a)__).__(b)__(__(c)__)
            .groupby(__(d)__)[__(e)__].__(f)__(__(g)__))

`(a)`:

`(b)`:

`(c)`:

`(d)`:

`(e)`:

`(f)`:

`(g)`:

# BEGIN SOLUTION

**Answer:** '\"Department\"\`

**Answer:** 'filter'

**Answer:** 'lambda df: df.mean() \>= 0.75'

**Answer:** '\"Department\"\`

**Answer:** '\"WaitTime\"\`

**Answer:** 'agg' or 'aggregate' or 'apply'

**Answer:** 'lambda s: np.percentile(s, 95)'

# END SOLUTION

# END SUBPROB

# END PROB