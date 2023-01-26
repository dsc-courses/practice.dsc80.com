# BEGIN PROB

Write *one line of code* which returns a Series containing the median number of minutes taken for tasks in each category.

# BEGIN SOLN

**Answer: ** `tasks.groupby('category')['minutes'].median()`

The idea is that we have to groupby `'category'` in order to consider the median number of minutes for each group of tasks based on their categories. Then we simply aggregate by `median()` to get the median of each category. Note that this automatically outputs the result as a Series so no further code is needed.

<average>89</average>

# END SOLN

# END PROB