# BEGIN PROB
The function `state_perm` is attempting to implement a test of the null hypothesis that the distributions of mean math section scores between 2005 and 2015 for two states are drawn from the same population distribution.

```py
def state_perm(states):
    if len(states) != 2:
        raise ValueError(f"Expected 2 elements, got {len(states)}")

    def calc_test_stat(df):
        return df.groupby("State")["Math"].mean().abs().diff().iloc[-1]
    
    states = sat.loc[sat["State"].isin(states), ["State", "Math"]]
    
    test_stats = []
    for _ in range(10000):
        states["State"] = np.random.permutation(states["State"])
        test_stat = calc_test_stat(states)
        test_stats.append(test_stat)
        
    obs = calc_test_stat(states)
    return (np.array(test_stats) >= obs).mean()
```

Suppose we call `state_perm(["California", "Washington"])` and see `0.514`.

# BEGIN SUBPROB
What test statistic is being used in the above call to `state_perm`?

( ) $\text{mean Washington score } - \text{mean California score}$
( ) $\text{mean California score } - \text{mean Washington score}$
( ) $\big|\text{mean Washington score } - \text{mean California score} \big|$
    
# BEGIN SOLN
**Answer: ** Option 1

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
There is exactly one issue with the implementation of `state_perm`. In **exactly one sentence**, identify the issue and state how you would fix it.

*Hint: The issue is **not** with the implementation of the function `calc_test_stat`.*

# BEGIN SOLN

**Answer: ** Since we are permuting in-place on the `states` DataFrame, we must calculate the observed test statistic before we permute.

# END SOLN
    
# END SUBPROB

# END PROB