# BEGIN PROB
Answer the following questions about missingness mechanisms. For each question, choose one of the following options:

- NMAR
- MAR
- MCAR
- Missing by design
# BEGIN SUBPROB
What is the missingness mechanism for the `'next'` column in the `stop` DataFrame?
# BEGIN SOLN
**Answer**: D. Missing by design

When there are missing values for the `'next'` column, it means there is no next stop and the line has reached the end of its route. This could have been designed differently to have an empty string, a string saying "end", etc. Therefore, the missing values are intentionally marked as missing by design.
# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Suppose that the missing values in the `'late'` column from the `bus` DataFrame are missing because Same got suspicious of negative values and deleted a few of them. What is the missingness mechanism for the values in the `'late'` column?
# BEGIN SOLN
**Answer**: A. NMAR

Since Sam is suspicious of `'late'` values based on the values themselves in `'late'` being negative, this is NMAR.
# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Suppose that the missing values in the `'late'` column from the `bus` DataFrame are missing because Tiffany made an update to the GPS system at $8$am and the system was down for $15$ minutes afterwards. What is the missingness mechanism for the values in the `late` column?
# BEGIN SOLN
**Answer**: B. MAR

Since Tiffany updated the system at $8$am, the missing values in `'late'` are dependent on the `'time'` column. Therefore it is MAR.
# END SOLN
# END SUBPROB

# END PROB