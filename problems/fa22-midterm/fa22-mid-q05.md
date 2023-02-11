# BEGIN PROB

Fill in the code below so that it computes a Series containing, for each
category, the proportion of completed tasks which took more than 30 minutes to complete. That is, out of all tasks which were completed in a given category, what percentage took more than 30 minutes?

```py
def proportion_more_than_30(df):
    ____
    

result = (
    tasks.groupby('category')[['completed', 'minutes']]
    .____(proportion_more_than_30)
)
```

# BEGIN SOLN
**Answer: ** `return (df[df['completed']]['minutes'] > 30).mean()`, `apply`

Note that for the first part, there are many different ways to complete this question. The point is that we first want to query for all the completed tasks. Then we get the proportion of all completed tasks that took 30 minutes to complete.

For part 2, if your `proportion_more_than_30` function was implemented correctly, simply calling `apply` should suffice.

<average>73</average>

# END SOLN

# END PROB