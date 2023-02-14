# BEGIN PROB

Consider the following snippet of code.

```py
pivoted = students.assign(Admit=students["Admit"] == "Y") \
                    .pivot_table(index="High School", 
                                columns="University", 
                                values="Admit", 
                                aggfunc="sum")
```

Some of the rows and columns of `pivoted` are shown below.

<center><img src='../assets/images/sp22-midterm/pivot.png' width=55%></center>

No students from Warren High were admitted to Columbia or Stanford.
However,\
`pivoted.loc["Warren High", "Columbia"]` and
`pivoted.loc["Warren High", "Stanford"]` evaluate to different values.
What is the reason for this difference?

( ) Some students from Warren High applied to Stanford, and some others
applied to Columbia, but none applied to both.
( ) Some students from Warren High applied to Stanford but none admitted
to Columbia.
( ) Some students from Warren High applied to Columbia but none admitted
to Stanford.
( ) The students from Warren High that applied to both Columbia and
Stanford were all rejected from Stanford, but at least one was admitted
to Columbia.
( ) When using `pivot_table`, `pandas` was not able to sum strings of
the form `"Y"`, `"N"`, and `"W"`, so the values in `pivoted` are
unreliable.

# BEGIN SOLN

**Answer: ** Option 3

`pivoted.loc["Warren High", "Stanford"]` is `NaN` because there were no
rows in `students` in which the `"High School"` was `"Warren High"` and
the `"University"` was `"Stanford"`, because nobody from Warren High
applied to Stanford. However, `pivoted.loc["Warren High", "Columbia"]`
is not `NaN` because there was at least one row in `students` in which
the `"High School"` was `"Warren High"` and the `"University"` was
`"Columbia"`. This means that at least one student from Warren High
applied to Columbia.

Option 3 is the only option consistent with this logic.

<average>93</average>

# END SOLN

# END PROB