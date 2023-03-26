# BEGIN PROB

We decide to build a classifier that takes in a state's demographic information and predicts whether, in a given year:

-   The state's mean math score was greater than its mean verbal score (1), or

-   the state's mean math score was less than or equal to its mean verbal score (0).


# BEGIN SUBPROB
(2 pts) The simplest possible classifier we could build is one that predicts the same label (1 or 0) every time, independent of all other features.

Consider the following statement:

*If `a > b`, then the constant classifier that maximizes training accuracy predicts 1 every time; otherwise, it predicts 0 every time.*

For which combination of `a` and `b` is the above statement **not guaranteed** to be true? 

*Note: Treat \texttt{sat} as our training set.*

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

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Suppose we train a classifier, named Classifier 1, and it achieves an accuracy of $\frac{5}{9}$ on our training set.

Typically, root mean squared error (RMSE) is used as a performance metric for regression models, but mathematically, nothing is stopping us from using it as a performance metric for classification models as well. 

What is the RMSE of Classifier 1 on our training set? Give your answer as a **simplified fraction**.

# BEGIN SOLN
**Answer: ** $\frac{2}{3}$

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

# END SOLN

# END SUBPROB

For the remainder of this question, suppose we train another classifier, named Classifier 2, again on our training set. Its performance on the training set is described in the confusion matrix below. Note that the columns of the confusion matrix have been separately normalized so that each has a sum of 1.

<center><img src='../assets/images/wi23-final/conf_matrix.png' width=30%></center>

# BEGIN SUBPROB
Suppose `conf` is the DataFrame above. Which of the following evaluates to a Series of length 2 whose only unique value is the number `1`?

( ) `conf.sum(axis=0)`
( ) `conf.sum(axis=1)`

# BEGIN SOLN
**Answer: ** Option 1

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Fill in the blank: the ___ of Classifier 2 is guaranteed to be 0.6.

( ) precision 
( ) recall
    
# BEGIN SOLN
**Answer: ** recall

# END SOLN

# END SUBPROB

For your convenience, we show the column-normalized confusion matrix from the previous page below. You will need to use the specific numbers in this matrix when answering the following subpart.

<center><img src='../assets/images/wi23-final/conf_matrix.png' width=30%></center>

# BEGIN SUBPROB
Suppose a fraction $\alpha$ of the labels in the training set are actually 1 and the remaining $1 - \alpha$ are actually 0. The accuracy of Classifier 2 is 0.65. What is the value of $\alpha$? \textbf{Show your work in the box below, and give your answer as a simplified fraction in the box at the bottom of the page.}

Hint: If you're unsure on how to proceed, here are some guiding questions:

-    Suppose the number of $y$-values that are actually 1 is $A$ and that the number of $y$-values that are actually 0 is $B$. In terms of $A$ and $B$, what is the accuracy of Classifier 2? Remember, you'll need to refer to the numbers in the confusion matrix above.

-    What is the relationship between $A$, $B$, and $\alpha$? How does it simplify your calculation for the accuracy in the previous step?


# BEGIN SOLN
**Answer: ** $\frac{5}{6}$

# END SOLN

# END SUBPROB

# END PROB