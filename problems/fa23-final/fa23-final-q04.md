# BEGIN PROB

Answer the following questions about missingness mechanisms. For each question, choose either not missing at random (NMAR), missing at random (MAR), missing completely at random (MCAR), or missing by design (MD).

# BEGIN SUBPROB

What is the missingness mechanism for the `'next'` column in the `stop` DataFrame?

# BEGIN SOLN
**Answer**: Missing by design (MD)

When there are missing values for the `'next'` column, it means there is no next stop and the line has reached the end of its route. This could have been designed differently to have an empty string, a string saying `"end"`, etc. Therefore, the missing values are intentionally marked as missing by design.

<average>68</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Suppose that the missing values in the `'late'` column from the `bus` DataFrame are missing because Sam got suspicious of negative values and deleted a few of them. What is the missingness mechanism for the values in the `'late'` column?
# BEGIN SOLN
**Answer**: Not missing at random (NMAR)

Since Sam deleted `'late'` values that were negative, the missingness of `'late'` values depends on the values themselves, making the missingness mechanism not missing at random.

<average>86</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Suppose that the missing values in the `'late'` column from the `bus` DataFrame are missing because Tiffany made an update to the GPS system at 8 AM and the system was down for $15$ minutes afterwards. What is the missingness mechanism for the values in the `late` column?
# BEGIN SOLN
**Answer**: Missing at random (MAR)

Since Tiffany updated the system at 8 AM, the missing values in `'late'` are dependent on the `'time'` column. Therefore, `'late'` values are missing at random.

<average>68</average>

# END SOLN
# END SUBPROB

# END PROB