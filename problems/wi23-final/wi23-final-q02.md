# BEGIN PROB
The following DataFrame contains the mean, median, and standard deviation of the number of students per year who took the SAT in New York and Texas between 2005 and 2015.

<center><img src='../assets/images/wi23-final/nyt.png' width=30%></center>

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

# END SOLN

# END SUBPROB

Suppose we want to run a statistical test to assess whether the distributions of the number of students between 2005 and 2015 in New York and Texas are significantly different. 

# BEGIN SUBPROB
What type of test is being proposed above?
    
( ) Hypothesis test
( ) Permutation test

# BEGIN SOLN
**Answer: ** Permutation test

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

# END SOLN
    
# END SUBPROB

Now, suppose we're interested in comparing the verbal score distribution of students who took the SAT in New York in 2015 to the verbal score distribution of all students who took the SAT in 2015.

The DataFrame `scores_2015`, shown in its entirety below, contains the verbal section score distributions of students in New York in 2015 and for all students in 2015.

<center><img src='../assets/images/wi23-final/ny_vs_all.png' width=30%></center>

    
# BEGIN SUBPROB
What type of test is being proposed above?
    
( ) Hypothesis test
( ) Permutation test

# BEGIN SOLN
**Answer: ** Hypothesis test

# END SOLN
    
# END SUBPROB

# BEGIN SUBPROB
Suppose $\vec{a} = \begin{bmatrix} a_1 & a_2 & ... & a_n \end{bmatrix}^T$ and $\vec{b} = \begin{bmatrix} b_1 & b_2 & ... & b_n \end{bmatrix}^T$ are both vectors containing proportions that add to 1 (e.g. $\vec{a}$ could be the `"New York"` column above and $\vec{b}$ could be the `"All States"` column above). As we've seen before, the TVD is defined as follows:

$\text{TVD}(\vec{a}, \vec{b}) = \frac{1}{2} \sum_{i = 1}^n \left| a_i - b_i \right|$

The TVD is not the only metric that can quantify the distance between two categorical distributions. Here are three other possible distance metrics:

-  $\text{dis1}(\vec{a}, \vec{b}) &= \vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2 + ... + a_nb_n$

-  $\text{dis2}(\vec{a}, \vec{b}) &= \frac{\vec{a} \cdot \vec{b}}{|\vec{a} | | \vec{b} |} = \frac{a_1b_1 + a_2b_2 + ... + a_nb_n}{\sqrt{a_1^2 + a_2^2 + ... + a_n^2} \sqrt{b_1^2 + b_2^2 + ... + b_n^2}}$

-  $text{dis3}(\vec{a}, \vec{b}) &= 1 - \frac{\vec{a} \cdot \vec{b}}{|\vec{a} | | \vec{b} |}$

Of the above three possible distance metrics, only one of them has the same range as the TVD (i.e. the same minimum possible value and the same maximum possible value) **and** has the property that smaller values correspond to more similar vectors. Which distance metric is it?

( ) $\text{dis1}$
( ) $\text{dis2}$
( ) $\text{dis3}$

# BEGIN SOLN
**Answer: ** $\text{dis3}$

# END SOLN

# END SUBPROB

# END PROB