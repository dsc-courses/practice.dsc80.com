# BEGIN PROB

Write a single line of code that evaluates to the most common value in
the `"High School"` column of `students`, as a string. Assume there are
no ties.

# BEGIN SOLN

**Answer: ** `students["High School"].value_counts().idxmax()`

or

`students.groupby("High School")["Name"].count().sort_values().index[-1]`

<average>89</average>

# END SOLN

# END PROB