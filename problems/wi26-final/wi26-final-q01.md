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

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Determine the value of the following expression.

```py
list(med["WaitTime"].iloc[:5])
```

# BEGIN SOLUTION

**Answer:** `[20.0, 27.0, 28.0, 5.0, 61.0]`

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What kind of values can appear in the `"WaitTime"` column? Select all that apply.

[ ] Negative
[ ] Zero
[ ] Positive

# BEGIN SOLUTION

**Answer:** Zero and Positive

# END SOLUTION

# END SUBPROB

Now that we've added a `"WaitTime"` column to `med`, we'll also add a `"Wait"` column containing `int` values, defined as follows.

```py
med["Wait"] = (med["WaitTime"] > 0).astype(int)
```

For the rest of the exam, `med` has `"WaitTime"` and `"Wait"` columns.

# END PROB
