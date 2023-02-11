# BEGIN PROB

You observe that tasks in the `'consulting'` category seem to be completed
at a higher rate than tasks in the `'work'` category. Could this be due to
chance? To check, you'll run a permutation test. Your hypotheses are:
 - **Null**: The true probability of completing a `'work'` task is the same as the probability of completing a `'consulting'` task.
 - **Alternative**: The true probability of completing a `'consulting'` is higher than the probability of completing a `'work'` task.


In the box below, write code which performs a permutation test and computes a p-value. The choice of an appropriate test statistic is left to you. You should check 10,000 permutations.

Note: you do not need to do anything special to account for missing values.

# BEGIN SOLN

**Answer: ** There are multiple ways of doing this problem.

For test statistic, we'll use the signed difference between the
proportion of `'consulting'` tasks which are completed, and the
proportion of `'work'` tasks which are completed.

```py
df = tasks[tasks['category'].isin(['work', 'consulting'])]
df = df[['category', 'completed']]

def test_stat(df):
    """Difference in proportion completed: consulting - work."""
    props = df.groupby('category')['completed'].mean()
    return props['consulting'] - props['work']

observed_stat = test_stat(df)

simulated = []
for i in range(10000):
    df['completed'] = np.random.permutation(df['completed'])
    simulated.append(test_stat(df))
    
p_value = (np.array(simulated) >= observed_stat).mean()
```

The main things we looked for was that your test statistic computes the difference in proportion of the two groups (and that it was a signed difference). We also looked to see if you properly seperated your data into a `'consulting'` group and `'work'` group. Finally, we looked to see that you performed the permutations properly (by either permuting the `'completed`' column or `'categor'` column), as well as calculated a proper p-value.

<average>82</average>

# END SOLN

# END PROB