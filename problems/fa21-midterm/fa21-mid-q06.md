# BEGIN PROB

Suppose a penguin is considered "little" if its body mass is less than 3250 grams. Write a piece of code that computes the number of each species which are considered little. Your code should return a series. To receive full credit, your code should not modify the dataframe `df`.

**Note**: your code will be graded manually, and it is not expected to be perfect. Be careful to not spend too much time trying to make your code perfect!

# BEGIN SOLN
**Answer: **
```py
df.loc[df['Body Mass'] < 3250].groupby('Species').count()
```

Note that there are many different approaches to this question. You can filter the DataFrame for "little" penguins first and then groupby (such as the code above). You could create an "indicator" column that indicates whether each penguin is "little" or not and sum that column for each group using group by again. You can create a custom aggregator, among other solutions. 

<average>89</average>

# END SOLN

# END PROB