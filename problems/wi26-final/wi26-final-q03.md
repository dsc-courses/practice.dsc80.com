# BEGIN PROB

Consider the small subset of `med` shown in full below. Recall that the `"Wait"` column was added after Question 1. The data is sorted by `"Age"`.

<center><img src="../../assets/images/wi26-final/q3-table.png" width=350></center>

# BEGIN SUBPROB

If we train a decision tree on this data to predict `"Wait"` based on `"Age"` and `"NumProviders"`, what is the maximum possible accuracy the decision tree could achieve? Give your answer as an exact decimal or simplified fraction.

# BEGIN SOLUTION

**Answer:** $\frac{11}{12}$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Select the expression below that gives the weighted entropy associated with using `"Age" >= 15` as the root node of the decision tree.

( ) $\frac{1}{6}\left(-\frac{2}{5}\log_2\frac{2}{5} - \frac{3}{5}\log_2\frac{3}{5}\right)$
( ) $-\frac{2}{5}\log_2\frac{2}{5} - \frac{3}{5}\log_2\frac{3}{5}$
( ) $\frac{1}{6}\left(-\frac{1}{2}\log_2\frac{1}{2} - \frac{1}{2}\log_2\frac{1}{2}\right)$
( ) $-\frac{1}{2}\log_2\frac{1}{2} - \frac{1}{2}\log_2\frac{1}{2}$
( ) $\frac{5}{6}\left(-\frac{2}{5}\log_2\frac{2}{5} - \frac{3}{5}\log_2\frac{3}{5}\right)$

# BEGIN SOLUTION

**Answer:** $\frac{5}{6}\left(-\frac{2}{5}\log_2\frac{2}{5} - \frac{3}{5}\log_2\frac{3}{5}\right)$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

All but one of the following questions splits the data in such a way that the weighted entropy is the same. Which question yields a **different** weighted entropy than the others?

( ) `"NumProviders" <= 2`
( ) `"NumProviders" <= 3`
( ) `"NumProviders" <= 4`
( ) `"NumProviders" <= 5`
( ) `"NumProviders" <= 6`

# BEGIN SOLUTION

**Answer:** `"NumProviders" <= 3`

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the weighted entropy associated with any one of the questions you did **not** pick in part (c)? Give your answer as an exact decimal or simplified fraction.

# BEGIN SOLUTION

**Answer:** $1$

# END SOLUTION

# END SUBPROB

# END PROB
