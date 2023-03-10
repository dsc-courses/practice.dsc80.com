# BEGIN PROB

Which of the following blocks of code correctly assign `max_AP` to the
maximum number of APs taken by a student who was rejected by UC San
Diego?

Option 1:

```py
cond1 = students["Admit"] == "N"
cond2 = students["University"] == "UC San Diego"
max_AP = students.loc[cond1 & cond2, "APs"].sort_values().iloc[-1]
```

Option 2:

```py
cond1 = students["Admit"] == "N"
cond2 = students["University"] == "UC San Diego"
d3 = students.groupby(["University", "Admit"]).max().reset_index()
max_AP = d3.loc[cond1 & cond2, "APs"].iloc[0]
```

Option 3:

```py
p = students.pivot_table(index="Admit", 
                            columns="University", 
                            values="APs", 
                            aggfunc="max")
max_AP = p.loc["N", "UC San Diego"]
```

Option 4:

```py
# .last() returns the element at the end of a Series it is called on
groups = students.sort_values(["APs", "Admit"]).groupby("University")
max_AP = groups["APs"].last()["UC San Diego"]
```

**Select all that apply.** There is at least one correct option.

[ ] Option 1
[ ] Option 2
[ ] Option 3
[ ] Option 4

# BEGIN SOLN

**Answer: ** Option 1 and Option 3

-   Option 1 works correctly, it is probably the most straightforward
    way of answering the question. `cond1` is `True` for all rows in
    which students were rejected, and `cond2` is `True` for all rows in
    which students applied to UCSD. As such,
    `students.loc[cond1 & cond2]` contains only the rows where students
    were rejected from UCSD. Then,
    `students.loc[cond1 & cond2, "APs"].sort_values()` sorts by the
    number of `"APs"` taken in increasing order, and `.iloc[-1]` gets
    the largest number of `"APs"` taken.

-   Option 2 doesn't work because the lengths of `cond1` and `cond2` are
    not the same as the length of `d3`, so this causes an error. 

-   Option 3 works correctly. For each combination of `"Admit"`
    status (`"Y"`, `"N"`, `"W"`) and `"University"` (including UC San
    Diego), it computes the max number of `"APs"`. The usage of
    `.loc["N", "UC San Diego"]` is correct too.

-   Option 4 doesn't work. It currently returns the maximum number of
    `"APs"` taken by someone who applied to UC San Diego; it does not
    factor in whether they were admitted, rejected, or waitlisted. 

<average>85</average>

# END SOLN

# END PROB