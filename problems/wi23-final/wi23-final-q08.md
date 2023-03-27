# BEGIN PROB

Let's continue with the premise from the previous question. That is, we will aim to build a classifier that takes in demographic information about a state from a particular year and predicts whether or not the state's mean math score is higher than its mean verbal score that year.

In honor of the rotisserie chicken event on UCSD's campus a few weeks ago, `sklearn` released a new classifier class called `ChickenClassifier`.

# BEGIN SUBPROB
`ChickenClassifier`s have many hyperparameters, one of which is `height`. As we increase the value of `height`, the model variance of the resulting `ChickenClassifier` also increases.

First, we consider the training and testing accuracy of a `ChickenClassifier` trained using various values of `height`. Consider the plot below.

<center><img src='../assets/images/wi23-final/accuracy.png' width=30%></center>

Which of the following depicts **training accuracy vs. `height`**?

( ) Option 1
( ) Option 2
( ) Option 3


Which of the following depicts **testing accuracy vs. `height`**?

( ) Option 1
( ) Option 2
( ) Option 3

# BEGIN SOLN
**Answer: ** Option 2, Option 3

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
`ChickenClassifier`s have another hyperparameter, `color`, for which there are four possible values: `"yellow"`, `"brown"`, `"red"`, and `"orange"`. To find the optimal value of `color`, we perform $k$-fold cross-validation with $k=4$. The results are given in the table below.

<center><img src='../assets/images/wi23-final/CV.png' width=30%></center>


Which value of `color` has the best average validation accuracy?

( ) `"yellow"`
( ) `"brown"`
( ) `"red"`
( ) `"orange"`

True or False: It is possible for a hyperparameter value to have the best average validation accuracy across all folds, but not have the best validation accuracy in any one particular fold.

( ) True
( ) False

# BEGIN SOLN
**Answer: ** `"red"`, True

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Now, instead of finding the best `height` and best `color` individually, we decide to perform a grid search that uses $k$-fold cross-validation to find the combination of `height` and `color` with the best average validation accuracy.

For the purposes of this question, assume that:
-    We are performing $k$-fold cross validation.

-    Our training set contains $n$ rows, where $n$ is greater than 5 and is a multiple of $k$.

-    There are $h_1$ possible values of `height` and $h_2$ possible values of `color`.

What is the size of each fold?

( ) $k$
( ) $\frac{k}{n}$
( ) $\frac{n}{k}$
( ) $\frac{n}{k} \cdot (k - 1)$
( ) $h_1h_2k$
( ) $h_1h_2(k-1)$
( ) $\frac{nh_1h_2}{k}$
( ) None of the above

How many times is row 5 in the training set used for training?

( ) $k$
( ) $\frac{k}{n}$
( ) $\frac{n}{k}$
( ) $\frac{n}{k} \cdot (k - 1)$
( ) $h_1h_2k$
( ) $h_1h_2(k-1)$
( ) $\frac{nh_1h_2}{k}$
( ) None of the above

How many times is row 5 in the training set used for validation?

( ) $k$
( ) $\frac{k}{n}$
( ) $\frac{n}{k}$
( ) $\frac{n}{k} \cdot (k - 1)$
( ) $h_1h_2k$
( ) $h_1h_2(k-1)$
( ) $\frac{nh_1h_2}{k}$
( ) None of the above
    
# BEGIN SOLN
**Answer: ** Option 3, Option 6, Option 8

# END SOLN

# END SUBPROB

# END PROB