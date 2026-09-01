# BEGIN PROB

To start, we need to calculate patient wait times, which are not provided in our data. Suppose we execute the line of code below to add a `"WaitTime"` column to `med`.

```py
med["WaitTime"] = (med["StartTime"] - med[["ArrivalTime", "AppointmentTime"]].max(axis=1)).dt.seconds / 60
```

Note that when we subtract two `pd.Timestamp` objects, the result is a `pd.Timedelta` object, whose `.seconds` attribute gives the time difference in seconds. There is no way to access the time difference in minutes directly.

# BEGIN SUBPROB

Fill in the blanks in the code below so that the `"WaitTime"` column remains exactly the same as calculated above. In other words, the code below should give an equivalent way to calculate `"WaitTime"`.

```py
def wait_time(x):
    return __(a)__
med["WaitTime"] = med.apply(__(b)__)
```

1. What goes in blank (a)?

2. What goes in blank (b)?

# BEGIN SOLUTION

**Answers:**

1. `(x["StartTime"] - max(x["ArrivalTime"], x["AppointmentTime"])).seconds / 60` (or an equivalent expression using `.max(axis=1)` on the two timestamp columns)
2. `wait_time, axis=1`

The vectorized version uses `.max(axis=1)` to take the later of `"ArrivalTime"` and `"AppointmentTime"` for each row. With `.apply(..., axis=1)`, each row is passed to `wait_time` as a Series, so we replicate that logic row-by-row using Python's `max` on the two timestamp values. We then subtract from `"StartTime"`, take `.seconds`, and divide by 60 — just like in the original code (note that we use `.seconds`, not `.dt.seconds`, because the row-wise subtraction already returns a `Timedelta`, not a Series of timedeltas).

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the data type of the `"WaitTime"` column?

( ) `pd.Timestamp`
( ) `pd.Timedelta`
( ) `int`
( ) `float`

# BEGIN SOLUTION

**Answer:** `float`

After subtracting timestamps and taking `.seconds`, we have integers (seconds). Dividing those integers by `60` produces floating-point values, so the resulting column has dtype `float`.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the value of the following expression.

```py
list(med["WaitTime"].iloc[:5])
```

# BEGIN SOLUTION

**Answer:** `[20.0, 27.0, 28.0, 5.0, 61.0]`

This evaluates the wait-time calculation on the first five rows of `med` as defined in the exam dataset.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What kind of values can appear in the `"WaitTime"` column? Select all that apply.

[ ] Negative
[ ] Zero
[ ] Positive

# BEGIN SOLUTION

**Answer:** Zero and Positive

The data description states that `"StartTime"` is always at or after both `"ArrivalTime"` and `"AppointmentTime"`. That means the wait time in minutes is always zero (if the appointment started exactly when the patient was ready) or positive (if the patient waited). It cannot be negative.

# END SOLUTION

# END SUBPROB

Now that we've added a `"WaitTime"` column to `med`, we'll also add a `"Wait"` column containing `int` values, defined as follows.

```py
med["Wait"] = (med["WaitTime"] > 0).astype(int)
```

For the rest of the exam, `med` has `"WaitTime"` and `"Wait"` columns.

# END PROB
