# BEGIN PROB

Suppose you are performing a permutation test to check the following hypotheses:

 - **Null**: The time required to complete tasks in the `'hobbies'` category is drawn from the same distribution as the time required to complete tasks in the `'finance'` category.
 - **Alternative**: The time required to complete tasks in the `'hobbies'` category is drawn from a different distribution as the time required to complete tasks in the `'finance'` category.

When you plot a histogram for the distribution of times taken to complete tasks in each categories, you see the below:

<center><img src='../assets/images/fa22-midterm/minutes-hobbies_and_finance.png' width=35%></center>

What is the *best* test statistic for this test?

( ) the Kolmogorov-Smirnov statistic
( ) the Total Variation Distance
( ) the *signed* difference between the mean time taken for `'finance'` tasks, minus the mean time taken for `'hobbies'` tasks.
( ) the maximum time taken for `'finance'` tasks, minus the maximum time taken for `'hobbies'` tasks

# BEGIN SOLN
**Answer: ** Option A

Note that TVD doesn't work well for variables that aren't categorical so we can rule that out. Looking at the distributions in the graph, it isn't clear that the difference between the mean time will do much for us, since the means for both distributions seem pretty close in value to each other. Again, looking at the distributions, taking the difference between the max of each group is just a bad metric (plus, max doesn't really say much about the distribution anyways). Thus using the KS statistic would work best for this problem.

<average>81</average>

# END SOLN

# END PROB