# BEGIN PROB

Write a piece of code that imputes missing flipper lengths with the **median** flipper length of the species that the penguin belongs to.

**Note**: your code will be graded manually, and it is not expected to be perfect. Be careful to not spend too much time trying to make your code perfect!

# BEGIN SOLN
**Answer: **

```py
df.groupby('Species')['Length'].transform(lambda x: x.fillna(x.median()))
```

<average>84</average>

# END SOLN

# END PROB