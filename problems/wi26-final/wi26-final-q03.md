# BEGIN PROB

Consider the small subset of `med` shown in full below. Recall that the `"Wait"` column was added after Question 1. The data is sorted by `"Age"`.

<center><img src="../../assets/images/wi26-final/wait.jpg" width=350></center>

# BEGIN SUBPROB

If we train a decision tree on this data to predict `"Wait"` based on `"Age"` and `"NumProviders"`, what is the maximum possible accuracy the decision tree could achieve? Give your answer as an exact decimal or simplified fraction.

# BEGIN SOLUTION

**Answer:** $\frac{11}{12}$

A decision tree can achieve perfect classification on 11 of the 12 rows; at least one row cannot be separated from the rest using only `"Age"` and `"NumProviders"`.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Select the expression below that gives the weighted entropy associated with using `"Age" >= 15` as the root node of the decision tree.

( ) $\frac{2}{12} \left(-\frac{2}{2}\log_2\frac{2}{2} - \frac{0}{2}\log_2\frac{0}{2}\right) + \frac{10}{12}\left(-\frac{6}{10}\log_2\frac{6}{10} - \frac{4}{10}\log_2\frac{4}{10}\right)$
( ) $\frac{2}{6}\left(-\frac{2}{5}\log_2\frac{2}{5} - \frac{3}{5}\log_2\frac{3}{5}\right) + \frac{3}{6}\left(-\frac{2}{2}\log_2\frac{2}{2} - \frac{1}{2}\log_2\frac{1}{2}\right)$
( ) $-\frac{6}{12}\log_2\frac{6}{12} - \frac{6}{12}\log_2\frac{6}{12}$
( ) $\frac{1}{2}\left(-\frac{1}{2}\log_2\frac{1}{2} - \frac{1}{2}\log_2\frac{1}{2}\right) + \frac{1}{2}\left(-\frac{1}{2}\log_2\frac{1}{2} - \frac{1}{2}\log_2\frac{1}{2}\right)$

# BEGIN SOLUTION

**Answer:** $\frac{2}{12} \left(-\frac{2}{2}\log_2\frac{2}{2} - \frac{0}{2}\log_2\frac{0}{2}\right) + \frac{10}{12}\left(-\frac{6}{10}\log_2\frac{6}{10} - \frac{4}{10}\log_2\frac{4}{10}\right)$

Splitting on `"Age" >= 15` gives a left group of 2 rows (both `"Wait"` = 0, entropy 0) and a right group of 10 rows (6 waits, 4 no-waits). The weighted entropy weights each child group's entropy by its proportion of the 12 total rows.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

All but one of the following question splits the data in such a way that the weighted entropy is the same. Which question yields a **different** weighted entropy than the others?

( ) `"NumProviders" <= 2`
( ) `"NumProviders" <= 3`
( ) `"NumProviders" <= 4`
( ) `"NumProviders" <= 5`
( ) `"NumProviders" <= 6`

# BEGIN SOLUTION

**Answer:** `"NumProviders" <= 3`

All of the listed splits except `"NumProviders" <= 3` produce the same weighted entropy of 1. The split at 3 providers gives a different weighted entropy (about 0.918).

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What is the weighted entropy associated with any one of the questions you did **not** pick in part (c)? Give your answer as an exact decimal or simplified fraction.

# BEGIN SOLUTION

**Answer:** $1$

Each of the splits other than `"NumProviders" <= 3` has weighted entropy 1.

# END SOLUTION

# END SUBPROB

# END PROB
