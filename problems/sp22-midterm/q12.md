# BEGIN PROB

After getting bored of working with her students, Valentina decides to
experiment with different ways of simulating data for the following pair
of hypotheses:

-   **Null hypothesis:** The coin is fair.

-   **Alternative hypothesis:** The coin is biased in favor of heads.

As her test statistic, Valentina uses the number of heads. She defines
the 2-D array `A` as follows:

    # .flatten() reshapes from 50 x 2 to 1 x 100
    A = np.array([
        np.array([np.random.permutation([0, 1]) for _ in range(50)]).flatten() 
        for _ in range(3000)
    ])

She also defines the 2-D array `B` as follows:

    # .flatten() reshapes from 50 x 2 to 1 x 100
    B = np.array([
        np.array([np.random.choice([0, 1], 2) for _ in range(50)]).flatten() 
        for _ in range(3000)
    ])

Below, we see a histogram of the distribution of her test statistics.

<center><img src='../assets/images/sp22-midterm/hist.png' width=60%></center>

Which one of the following arrays are visualized above?

( ) `A.sum(axis=1)`
( ) `B.sum(axis=1)`

# BEGIN SOLN

**Answer: ** Option 2

Note that `arr.sum(axis=1)` takes the sum of each **row** of `arr`.

The difference comes down to the behavior of
`np.random.permutation([0, 1])` and `np.random.choice([0, 1])`.

Each call to `np.random.permutation([0, 1])` will either return
`array([0, 1]` or `array([1, 0])` --- one head and one tail. As a
result, each row of `A` will consist of 50 1s and 50 0s, and so the sum
of each row of `A` will be exactly 50. If we drew a histogram of this
distribution, it would be a single spike at the number 50.

On the other hand, each call to `np.random.choice([0, 1], 2)` could
either return `array([0, 0])`, `array([0, 1])`, `array([1, 0])`, or
`array([1, 1])`. Each of these are returned with equal probabilities. In
effect, `np.random.choice([0, 1], 2)` flips a fair coin twice, so
`[np.random.choice([0, 1], 2) for _ in range(50)]` flips a fair coin 100
times. When we take the sum of each row of `B`, we will get the number
of heads in 100 coin flips; the histogram drawn is consistent with this
interpretation.

<average>83</average>

# END SOLN

# END PROB