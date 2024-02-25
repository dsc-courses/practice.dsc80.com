# BEGIN PROB

We decide to build a classifier that takes in a state's demographic information and predicts whether, in a given year:

-   The state's mean math score was greater than its mean verbal score (1), or

-   the state's mean math score was less than or equal to its mean verbal score (0).


# BEGIN SUBPROB
The simplest possible classifier we could build is one that predicts the same label (1 or 0) every time, independent of all other features.

Consider the following statement:

*If `a > b`, then the constant classifier that maximizes training accuracy predicts 1 every time; otherwise, it predicts 0 every time.*

For which combination of `a` and `b` is the above statement **not guaranteed** to be true? 

*Note: Treat `sat` as our training set.*

Option 1:
```py
a = (sat['Math'] > sat['Verbal']).mean()
b = 0.5
```

Option 2:
```py
a = (sat['Math'] - sat['Verbal']).mean()
b = 0
```

Option 3:
```py
a = (sat['Math'] - sat['Verbal'] > 0).mean()
b = 0.5
```

Option 4:
```py
a = ((sat['Math'] / sat['Verbal']) > 1).mean() - 0.5
b = 0
```

( ) Option 1
( ) Option 2
( ) Option 3
( ) Option 4

# BEGIN SOLN
**Answer: ** Option 2

Conceptually, we're looking for a combination of `a` and `b` such that when `a > b`, it's true that **in more than 50% of states, the `"Math"` value is larger than the `"Verbal"` value**. Let's look at all four options through this lens:

- Option 1: `sat['Math'] > sat['Verbal']` is a Series of Boolean values, containing `True` for all states where the `"Math"` value is larger than the `"Verbal"` value and `False` for all other states. The mean of this series, then, is the proportion of states satisfying this criteria, and since `b` is `0.5`, `a > b` is `True` only when the bolded condition above is `True`.
- Option 3 is the same as Option 1 – note that $x > y$ is equivalent to $x - y > 0$.
- Option 4: `sat['Math'] / sat['Verbal']` is a Series that contains values greater than 1 whenever a state's `"Math"` value is larger than its `"Verbal"` value and less than or equal to 1 in all other cases. As in the other options that work, `(sat['Math'] / sat['Verbal']) > 1` is a Boolean Series with `True` for all states with a larger `"Math"` value than `"Verbal"` values; `a > b` compares the proportion of `True` values in this Series to 0.5. (Here, $p - 0.5 > 0$ is the same as $p > 0.5$.)

Then, by process of elimination, Option 2 must be the correct option – that is, it must be the only option that **doesn't** work. But why? `sat['Math'] - sat['Verbal']` is a Series containing the difference between each state's `"Math"` and `"Verbal"` values, and `.mean()` computes the mean of these differences. The issue is that here, we don't care about _how different_ each state's `"Math"` and `"Verbal"` values are; rather, we just care about the proportion of states with a bigger `"Math"` value than `"Verbal"` value. It could be the case that 90% of states have a larger `"Math"` value than `"Verbal"` value, but one state has such a big `"Verbal"` value that it makes the mean difference between `"Math"` and `"Verbal"` scores negative. (A property you'll learn about in future probability courses is that this is equal to the difference in the mean `"Math"` value for all states and the mean `"Verbal"` value for all states – this is called the "linearity of expectation" – but you don't need to know that to answer this question.)


<average>58</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Suppose we train a classifier, named Classifier 1, and it achieves an accuracy of $\frac{5}{9}$ on our training set.

Typically, root mean squared error (RMSE) is used as a performance metric for regression models, but mathematically, nothing is stopping us from using it as a performance metric for classification models as well. 

What is the RMSE of Classifier 1 on our training set? Give your answer as a **simplified fraction**.

# BEGIN SOLN
**Answer: ** $\frac{2}{3}$

An accuracy of $\frac{5}{9}$ means that the model is such that out of 9 values, 5 are labeled correctly. By extension, this means that 4 out of 9 are not labeled correctly as 0 or 1.

Remember, RMSE is defined as

$$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i = 1}^n (y_i - H(x_i))^2}$$

where $y_i$ represents the $i$th actual value and $H(x_i)$ represents the $i$th prediction. Here, $y_i$ is either 0 or 1 and $H(x_i) is also either 0 or 1. We're told that $\frac{5}{9}$ of the time, $y_i$ and $H(x_i)$ are the same; in those cases, $(y_i - H(x_i))^2 = 0^2 = 0$. We're also told that $\frac{4}{9}$ of the time, $y_i$ and $H(x_i)$ are different; in those cases, $(y_i - H(x_i))^2 = 1$. So,

$$\text{RMSE} = \sqrt{\frac{5}{9} \cdot 0 + \frac{4}{9} \cdot 1} = \sqrt{\frac{4}{9}} = \frac{2}{3}$$

<average>55</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

While Classifier 1's accuracy on our training set is $\frac{5}{9}$, its accuracy on our test set is $\frac{1}{4}$. Which of the following scenarios is most likely?

( ) Classifier 1 overfit to our training set; we need to increase its complexity.
( ) Classifier 1 overfit to our training set; we need to decrease its complexity.
( ) Classifier 1 underfit to our training set; we need to increase its complexity.
( ) Classifier 1 underfit to our training set; we need to decrease its complexity.

# BEGIN SOLN
**Answer: ** Option 2

Since the accuracy of Classifier 1 is much higher on the dataset used to train it than the dataset it was tested on, it's likely Classifer 1 overfit to the training set because it was too complex. To fix the issue, we need to decrease its complexity, so that it focuses on learning the general structure of the data in the training set and not too much on the random noise in the training set.

<average>86</average>

# END SOLN

# END SUBPROB

For the remainder of this question, suppose we train another classifier, named Classifier 2, again on our training set. Its performance on the training set is described in the confusion matrix below. Note that the columns of the confusion matrix have been separately normalized so that each has a sum of 1.

<center><img src='../assets/images/wi23-final/conf-matrix.png' width=30%></center>

# BEGIN SUBPROB
Suppose `conf` is the DataFrame above. Which of the following evaluates to a Series of length 2 whose only unique value is the number `1`?

( ) `conf.sum(axis=0)`
( ) `conf.sum(axis=1)`

# BEGIN SOLN
**Answer: ** Option 1

Note that the columns of `conf` sum to 1 – $0.9 + 0.1 = 1$, and $0.4 + 0.6 = 1$. To create a Series with just the value 1, then, we need to sum the columns of `conf`, which we can do using `conf.sum(axis=0)`. `conf.sum(axis=1)` would sum the rows of `conf`.

<average>81</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Fill in the blank: the ___ of Classifier 2 is guaranteed to be 0.6.

( ) precision 
( ) recall
    
# BEGIN SOLN
**Answer: ** recall

The number 0.6 appears in the bottom-right corner of `conf`. Since  `conf` is column-normalized, the value 0.6 represents the proportion of values in the second column that were predicted to be 1. The second column contains values that were actually 1, so 0.6 is really **the proportion of values that were actually 1 that were predicted to be 1**, that is, $\frac{\text{actually 1 and predicted 1}}{\text{actually 1}}$. This is the definition of recall!

If you'd like to think in terms of true positives, etc., then remember that:
- True Positives (TP) are values that were actually 1 and were predicted to be 1.
- True Negatives (TN) are values that were actually 0 and were predicted to be 0.
- False Positives (FP) are values that were actually 0 and were predicted to be 1.
- False Negatives (FN) are values that were actually 1 and were predicted to be 0.

Recall is $\frac{\text{TP}}{\text{TP} + \text{FN}}$.

<average>77</average>


# END SOLN

# END SUBPROB

For your convenience, we show the column-normalized confusion matrix from the previous page below. You will need to use the specific numbers in this matrix when answering the following subpart.

<center><img src='../assets/images/wi23-final/conf-matrix.png' width=30%></center>

# BEGIN SUBPROB
Suppose a fraction $\alpha$ of the labels in the training set are actually 1 and the remaining $1 - \alpha$ are actually 0. The accuracy of Classifier 2 is 0.65. What is the value of $\alpha$? \textbf{Show your work in the box below, and give your answer as a simplified fraction in the box at the bottom of the page.}

Hint: If you're unsure on how to proceed, here are some guiding questions:

-    Suppose the number of $y$-values that are actually 1 is $A$ and that the number of $y$-values that are actually 0 is $B$. In terms of $A$ and $B$, what is the accuracy of Classifier 2? Remember, you'll need to refer to the numbers in the confusion matrix above.

-    What is the relationship between $A$, $B$, and $\alpha$? How does it simplify your calculation for the accuracy in the previous step?


# BEGIN SOLN
**Answer: ** $\frac{5}{6}$

Here is one way to solve this problem:

accuracy = $\frac{TP + TN}{TP + TN + FP + FN}$

Given the values from the confusion matrix:

accuracy = $\frac{0.6 \cdot \alpha + 0.9 \cdot (1 - \alpha)}{\alpha + (1 - \alpha)}$ \
accuracy = $\frac{0.6 \cdot \alpha + 0.9 - 0.9 \cdot \alpha}{1}$ \
accuracy = $0.9 - 0.3 \cdot \alpha$

Therefore:

0.65 = $0.9 - 0.3 \cdot \alpha$ \
$0.3 \cdot \alpha$  = $0.9 - 0.65$ \
$0.3 \cdot \alpha$  = $0.25$ \
$\alpha$  = $\frac{0.25}{0.3}$ \
$\alpha$  = $\frac{5}{6}$

<average>61</average>

# END SOLN

# END SUBPROB

# END PROB