# BEGIN PROB

# BEGIN SUBPROB

(3 pts\*) Billy and Daisy each decide what songs to stream by rolling
dice. Billy rolls a six-sided die 36 times and sees the same number of
1s, 2s, 3s, 4s, 5s, and 6s. Daisy rolls a six-sided die 72 times and
sees 36 1s, 18 4s, and 18 6s.

What is the total variation distance (TVD) between their distributions
of rolls? Give your answer as a number.

# BEGIN SOLN

**Answer: ** $\frac{1}{2}$

First, we must normalize their distributions so they sum to 1.
$$\text{billy} = \begin{bmatrix} \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6} \end{bmatrix}, \: \: \: \text{daisy} = \begin{bmatrix} \frac{1}{2}, 0, 0, \frac{1}{4}, 0, \frac{1}{4} \end{bmatrix}$$

Then, recall that the TVD is the sum of the absolute differences in
proportions, all divided by 2:

$$\begin{aligned}
\text{TVD} &= \frac{1}{2} \Bigg( \Big| \frac{1}{2} - \frac{1}{6} \Big| + \Big| 0 - \frac{1}{6} \Big| +  \Big| 0 - \frac{1}{6} \Big|  +  \Big| \frac{1}{4} - \frac{1}{6} \Big| +  \Big| 0 - \frac{1}{6} \Big| +  \Big| \frac{1}{4} - \frac{1}{6} \Big|    \Bigg) \\
&= \frac{1}{2} \Bigg( \frac{2}{6} + \frac{1}{6} + \frac{1}{6} + \frac{1}{12} + \frac{1}{6} + \frac{1}{12} \Bigg) \\
&= \frac{1}{2} \cdot 1 \\
&= \frac{1}{2}\end{aligned}$$

<average>42</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(2 pts\*) Consider two categorical distributions, each made up of the
same $n$ categories. Given no other information, what is the smallest
possible TVD between the two distributions, and what is the largest
possible TVD between the two distributions? Give both answers as
numbers.

smallest possible TVD =

largest possible TVD =

# BEGIN SOLN

**Answer: ** Smallest: 0, Largest: 2

There is an absolute value in the definition of TVD, so it must be at
least 0. The TVD does not scale with the number of categories; its
maximum possible value is 1. We will not provide a rigorous proof here,
but intuitively, the most "different\" two distributions can be is if
they both have 100% of their values in different categories. In such a
case, the TVD is 1.

<average>74</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

(1 pt\*) Consider the following pair of distributions.

::: center
<center><img src='../assets/images/sp22-final/dists.png' width=35%></center>

Suppose we want to perform a permutation test to test whether the two
distributions come from the same population distribution. Which test
statistic is most likely to yield a significant result?

( ) Difference in means
( ) Absolute difference in means
( ) Kolmogorov-Smirnov (K-S) statistic
( ) Total variation distance

# BEGIN SOLN

**Answer: ** Option 3

-   These are two quantitative distributions, and the total variation
    distance only applies for categorical distributions.

-   These two distributions have similar means, so the difference in
    means and absolute difference in means won't be able to tell them
    apart.

-   As such, the correct answer is the Kolmogorov-Smirnov statistic,
    which roughly measures the largest "gap\" between two cumulative
    distribution functions.

<average>87</average>

# END SOLN

# END SUBPROB

# END PROB