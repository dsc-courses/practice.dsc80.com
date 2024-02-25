# BEGIN PROB
The following DataFrame contains the mean, median, and standard deviation of the number of students per year who took the SAT in New York and Texas between 2005 and 2015.

<center><img src='../assets/images/wi23-final/nyt.png' width=35%></center>

# BEGIN SUBPROB

Which of the following expressions creates the above DataFrame correctly and in the most efficient possible way (in terms of time and space complexity)?

*Note: The only difference between the options is the positioning of `"# Students"`.*

Option 1:

```py
(sat.loc[sat["State"].isin(["New York", "Texas"])]
["# Students"].groupby("State").agg(["mean", "median", "std"]))
```

Option 2:

```py
(sat.loc[sat["State"].isin(["New York", "Texas"])]
.groupby("State")["# Students"].agg(["mean", "median", "std"]))
```

Option 3:

```py
(sat.loc[sat["State"].isin(["New York", "Texas"])]
.groupby("State").agg(["mean", "median", "std"])["# Students"])
```

( ) Option 1
( ) Option 2
( ) Option 3
( ) Multiple options are equally correct and efficient

# BEGIN SOLN
**Answer: ** Option 2

- Option 1 is incorrect because it attempts to select the `"# Students"` column before grouping by `"State"`, which is not possible.
- Option 2 filters the DataFrame, groups by `"State"`, and then performs aggregation only on the `"# Students"` column, making it efficient.
- Option 3 does the aggregations for all columns first and then selects the `"# Students"` column, which is correct but less efficient because it computes aggregations for potentially many columns (like `"Math"`) that are not needed.

<average>75</average>

# END SOLN

# END SUBPROB

Suppose we want to run a statistical test to assess whether the distributions of the number of students between 2005 and 2015 in New York and Texas are significantly different. 

# BEGIN SUBPROB

What type of test is being proposed above?

( ) Hypothesis test
( ) Permutation test

# BEGIN SOLN
**Answer: ** Permutation test

Here, we're comparing whether two sample distributions – specifically, (1) the distribution of the number of students per year from 2005-2015 for New York and (2) the distribution of the number of students per year from 2005-2015 for Texas – are significantly different. This is precisely what a permutation test is used for. For the purposes of this test, we have 22 relevant rows of data – 11 for New York and 11 for Texas – and 2 columns, `"State"` and `"# Students"`.

<average>90</average>

# END SOLN
    
# END SUBPROB

# BEGIN SUBPROB
Given the information in the above DataFrame, which test statistic is **most likely** to yield a significant difference?

( ) $\text{mean number of students in Texas } - \text{ mean number of students in New York}$
( ) $\big|\text{mean number of students in Texas } - \text{ mean number of students in New York}\big|$
( ) $\big|\text{median number of students in Texas } - \text{ median number of students in New York}\big|$
( ) The Kolmogorov-Smirnov statistic

# BEGIN SOLN
**Answer: ** The Kolmogorov-Smirnov statistic

Here, the means and medians of the two samples are similar, so their observed difference in means and observed difference in medians are both small. This means that a permutation test using either one of those as a test statistic will likely fail to yield a significant difference. However, the standard deviations of both distributions are quite different, which means the shapes of the distributions are quite different. The Kolmogorov-Smirnov statistic measures the distance between two distributions by considering their entire shape, and since these distributions have very different shapes, they will likely have a larger Kolmogorov-Smirnov statistic than expected under the null.

<!-- The difference in means an median only focuses on the central tendency and is unable to consider the full distribution of the data. The Kolmogorov-Smirnov statistic is most likely to yield a significant difference if there are any differences in the distributions beyond just the central tendency. It is more comprehensive as it evaluates differences across the entire range of the distributions, making it a robust choice for comparing the two states' SAT student distributions. -->

<average>78</average>

# END SOLN
    
# END SUBPROB

Now, suppose we're interested in comparing the verbal score distribution of students who took the SAT in New York in 2015 to the verbal score distribution of all students who took the SAT in 2015.

The DataFrame `scores_2015`, shown in its entirety below, contains the verbal section score distributions of students in New York in 2015 and for all students in 2015.

<center><img src='../assets/images/wi23-final/ny_vs_all.png' width=25%></center>

# BEGIN SUBPROB

What type of test is being proposed above?

( ) Hypothesis test
( ) Permutation test

# BEGIN SOLN
**Answer: ** Hypothesis test

One way to think about "standard" hypothesis tests is that they test whether a given sample – in this case, the verbal score distribution of New York students in 2015 – looks like it was drawn from a given population – here, the verbal score distribution of all students in 2015. That's what's happening here.

<average>87</average>

# END SOLN
    
# END SUBPROB

# BEGIN SUBPROB
Suppose $\vec{a} = \begin{bmatrix} a_1 & a_2 & ... & a_n \end{bmatrix}^T$ and $\vec{b} = \begin{bmatrix} b_1 & b_2 & ... & b_n \end{bmatrix}^T$ are both vectors containing proportions that add to 1 (e.g. $\vec{a}$ could be the `"New York"` column above and $\vec{b}$ could be the `"All States"` column above). As we've seen before, the TVD is defined as follows:

$\text{TVD}(\vec{a}, \vec{b}) = \frac{1}{2} \sum_{i = 1}^n \left| a_i - b_i \right|$

The TVD is not the only metric that can quantify the distance between two categorical distributions. Here are three other possible distance metrics:

-  $\text{dis1}(\vec{a}, \vec{b}) = \vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2 + ... + a_nb_n$

-  $\text{dis2}(\vec{a}, \vec{b}) = \frac{\vec{a} \cdot \vec{b}}{|\vec{a} | | \vec{b} |} = \frac{a_1b_1 + a_2b_2 + ... + a_nb_n}{\sqrt{a_1^2 + a_2^2 + ... + a_n^2} \sqrt{b_1^2 + b_2^2 + ... + b_n^2}}$

-  $\text{dis3}(\vec{a}, \vec{b}) = 1 - \frac{\vec{a} \cdot \vec{b}}{|\vec{a} | | \vec{b} |}$

Of the above three possible distance metrics, only one of them has the same range as the TVD (i.e. the same minimum possible value and the same maximum possible value) **and** has the property that smaller values correspond to more similar vectors. Which distance metric is it?

( ) $\text{dis1}$
( ) $\text{dis2}$
( ) $\text{dis3}$

# BEGIN SOLN
**Answer: ** $\text{dis3}$

Let's look at the options carefully:

- $\text{dis1}$ does not have the property that smaller values correspond to more similar vectors. Consider $\vec{a} = [1, 0], \vec{b} = [0, 1], \vec{c} = [1, 0]$. Here, $\text{dis1}(\vec{a}, \vec{b}) = 1 \cdot 0 + 0 \cdot 1 = 0$ and $\text{dis1}(\vec{a}, \vec{c}) = 1 \cdot 1 + 0 \cdot 0 = 1$. $\vec{a}$ and $\vec{c}$ are the exact same vector, but they have a larger $\text{dis1}$ value than $\vec{a}$ and $\vec{b}$, which are very different vectors. $\text{dis1}$ has the property that larger values correspond to more similar vectors, which is what we're looking for.
- $\text{dis2}$ behaves the same way that $\text{dis1}$ does, in that larger values correspond to more similar vectors. Note that the numerator of $\text{dis2}$ is just $\text{dis1}$.
- By process of elimination, the answer must be $\text{dis3}$. But, for those who are curious, why does $\text{dis3}$ work? Here's why:
    - Remember from Math 18 that if $\vec{a}$ and $\vec{b}$ are two vectors, then their dot product can be expressed as $\vec{a} \cdot \vec{b} = | \vec{a} | | \vec{b} | \cos \theta$, where $\theta$ is the angle between the two vectors.
    - If all of the elements in $\vec{a}$ and $\vec{b}$ are non-negative, then the angle $\theta$ between $\vec{a}$ and $\vec{b}$ must be between 0 and 90 degrees, which means $\cos \theta$ must be between 1 (when $\theta$ is 0) and 0 (when $\theta$ is 90).
    - Rearranging the dot product, we have that $\cos \theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a} | | \vec{b} |}$. When $\vec{a}$ and $\vec{b}$ point in the same direction – that is, when they are as similar as possible – $\cos \theta$ is 1, and when they are as different as possible – that is, when they are orthogonal – $\cos \theta$ is 0. This is the exact opposite of the behavior we want in a distance metric, where we want smaller values to correspond to more similar vectors, not larger values. Note that $\cos \theta$ is the same as $\text{dis2}$.
    - By computing $\text{dis3}(\vec{a}, \vec{b}) = 1 - \cos \theta = 1 - \frac{\vec{a} \cdot \vec{b}}{|\vec{a} | | \vec{b} |}$, we reverse the behavior of $\cos \theta$: when $\vec{a} and $\vec{b}$ point in the same direction, $\text{dis3}(\vec{a}, \vec{b}) = 0$, and when they are very different, $\text{dis3}(\vec{a}, \vec{b}) = 1$. Now, $\text{dis3}(\vec{a}, \vec{b})$ behaves the same way as the TVD, in that a value of 0 means the vectors are identical and a value of 1 means the vectors are very different!

<average>75</average>

# END SOLN

# END SUBPROB

# END PROB