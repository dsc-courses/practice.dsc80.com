# BEGIN PROB

In the sample of penguins in the table `df` above, 40% are Gentoo penguins, 30% are Adelie, and 30% are Chinstrap. It is known that, overall, 45% of penguins in Antarctica are Gentoo, 35% are Adelie, and 20% are Chinstrap. It therefore seems that the distribution of penguin species in your sample may differ from the population distribution.

You will test this with a hypothesis test. Your null hypothesis is that the sample in `df` was drawn at random from the population. The alternative hypothesis is that your sample was drawn with different probabilities than those shown above.

Write a piece of code to calculate the p-value of the observed data. You must choose a test statistic, calculate the observed value of the test statistic, compute simulated values of the test statistic, and calculate a p-value. For that reason, this question is worth 7 points, and partial credit will be awarded for each of the above.

**Note**: your code will be graded manually, and it is not expected to be perfect. Be careful to not spend too much time trying to make your code perfect!

# BEGIN SOLN
**Answer: **
```py
observed = (abs(0.45 - 0.4) + abs(0.35 - 0.3) + abs(0.3 - 0.2)) / 2
arr = []
for i in range(1000):
    sample = np.random.multinomial(330, p = [0.45, 0.35, 0.2]) / 330
    test_stat = sum(abs(sample - np.array([0.4, 0.3, 0.3]))) / 2
    arr += [test_stat]

p_value = sum(np.array(arr) >= observed) / 1000
```

Note that there were many different ways to do this problem. The main things we looked for were: whether or not you used TVD as your test statistic, whether or not you computed an observed test statistic correctly, generated samples using `np.random.multinomial` or `np.random.choice`, and calculated your p-value correctly.

<average>83</average>

# END SOLN

# END PROB