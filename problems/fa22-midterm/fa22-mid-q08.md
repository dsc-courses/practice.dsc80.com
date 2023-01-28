# BEGIN PROB
Write a line of code which creates a pivot table showing the number of tasks of each urgency level for each client. The index should contain the urgency levels, and the columns should contain the client names.

# BEGIN SOLN
**Answer: ** code shown below

```py
tasks.pivot_table(
    columns='client', index='urgency', values='category', aggfunc='count'
)
```

We're given that the index should be filled out with `'urgency'` and the columns should be `'clients'`. The values should be any other column that has no missing values such as `'category'` or `'completed'`. The aggfunc is just `count` since we want the number of tasks within each group.

<average>82</average>

# END SOLN

# END PROB