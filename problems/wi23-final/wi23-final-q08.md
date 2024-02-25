# BEGIN PROB

Let's continue with the premise from the previous question. That is, we will aim to build a classifier that takes in demographic information about a state from a particular year and predicts whether or not the state's mean math score is higher than its mean verbal score that year.

In honor of the <a href="https://www.reddit.com/r/UCSD/comments/11o0w9r/chicken_event/">rotisserie chicken event</a> on UCSD's campus a few weeks ago, `sklearn` released a new classifier class called `ChickenClassifier`.

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
**Answer: ** Option 2 depicts training accuracy vs. `height`; Option 3 depicts testing accuract vs. `height`

We are told that as `height` increases, the model variance (complexity) also increases.

As we increase the complexity of our classifier, it will do a better job of fitting to the training set because it's able to "memorize" the patterns in the training set. As such, as `height` increases, training accuracy increases, which we see in Option 2.

However, after a certain point, increasing `height` will make our classifier overfit too closely to our training set and not general enough to match the patterns in other similar datasets, meaning that after a certain point, increasing `height` will actually decrease our classifier's accuracy on our testing set. The only option that shows accuracy increase and then decrease is Option 3.

<average>75</average>

# END SOLN

# END SUBPROB

`ChickenClassifier`s have another hyperparameter, `color`, for which there are four possible values: `"yellow"`, `"brown"`, `"red"`, and `"orange"`. To find the optimal value of `color`, we perform $k$-fold cross-validation with $k=4$. The results are given in the table below.

<center><img src='../assets/images/wi23-final/CV.png' width=30%></center>

# BEGIN SUBPROB

Which value of `color` has the best average validation accuracy?

( ) `"yellow"`
( ) `"brown"`
( ) `"red"`
( ) `"orange"`


# BEGIN SOLN
**Answer: ** `"red"`

From looking at the results of the k-fold cross validation, we see that the color red has the highest, and therefore the best, validation accuracy as it has the highest row mean (across all 4 folds).

<average>91</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

True or False: It is possible for a hyperparameter value to have the best average validation accuracy across all folds, but not have the best validation accuracy in any one particular fold.

( ) True
( ) False

# BEGIN SOLN

**Answer:** True

An example is shown below: 

| color    | Fold 1  | Fold 2  | Fold 3  | Fold 4  | average |
| -------- | ------- | ------- | ------- | ------- | ------- |
| color 1  | 0.8     |  0      |  0      |   0     | 0.2     |
| color 2  | 0       |  0.6    |  0      |   0     | 0.15    |
| color 3  | 0       |  0      |  0.1    |   0     | 0.025   |
| color 4  | 0       |  0      |  0      |   0.2   | 0.05    |
| color 5  | 0.7     |  0.5    |  0.01   |   0.1   | 0.3275  |

In the example, color 5 has the highest average validation accuracy across all folds, but is not the best in any one fold.

<average>94</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Now, instead of finding the best `height` and best `color` individually, we decide to perform a grid search that uses $k$-fold cross-validation to find the combination of `height` and `color` with the best average validation accuracy.

For the purposes of this question, assume that:

-    We are performing $k$-fold cross validation.
-    Our training set contains $n$ rows, where $n$ is greater than 5 and is a multiple of $k$.
-    There are $h_1$ possible values of `height` and $h_2$ possible values of `color`.

Consider the following three subparts:

- A. What is the size of each fold?
- B. How many times is row 5 in the training set used for training?
- C. How many times is row 5 in the training set used for validation?

Choose from the following options.

( ) $k$
( ) $\frac{k}{n}$
( ) $\frac{n}{k}$
( ) $\frac{n}{k} \cdot (k - 1)$
( ) $h_1h_2k$
( ) $h_1h_2(k-1)$
( ) $\frac{nh_1h_2}{k}$
( ) None of the above
    
# BEGIN SOLN
**Answer: ** A: Option 3 ($\frac{n}{k}$), B: Option 6 ($h_1h_2(k-1)$), C: Option 8 (None of the above)

<br>

##### A. What is the size of each fold?

The training set is divided into $k$ folds of equal size, resulting in $k$ folds with size $\frac{n}{k}$.

<average>66</average>

<br>

##### B. How many times is row 5 in the training set used for training?

For each combination of hyperparameters, row 5 is $k - 1$ times for training and $1$ time for validation. There are $h_1 \cdot h_2$ combinations of hyperparameters, so row 5 is used for training $h_1 \cdot h_2 \cdot (k-1)$ times.

<average>76</average>

<br>

##### C. How many times is row 5 in the training set used for validation?

Building off of the explanation for the previous subpart, row 5 is used for validation 1 times for each combination of hyperparameters, so the correct expression would be $h_1 \cdot h_2$, which is not a provided option.

<average>69</average>


# END SOLN

# END SUBPROB

# END PROB