# BEGIN PROB

Currently, `students` has a lot of repeated information --- for
instance, if a student applied to 10 universities, their GPA appears 10
times in `students`.

We want to generate a DataFrame that contains a single row for each
student, indexed by `"Email"`, that contains their `"Name"`,
`"High School"`, `"GPA"`, and `"APs"`.

One attempt to create such a DataFrame is below.

```py
students.groupby("Email").aggregate({"Name": "max",
                                        "High School": "mean",
                                        "GPA": "mean",
                                        "APs": "max"})
```

There is exactly one issue with the line of code above. **In one
sentence**, explain what needs to be changed about the line of code
above so that the desired DataFrame is created.

# BEGIN SOLN

**Answer: ** The problem right now is that aggregating High School by mean doesn't work since you can't aggregate a column with strings using `"mean"`. Thus changing it to something that works for strings like `"max"` or `"min"` would fix the issue.

<average>79</average>

# END SOLN

# END PROB