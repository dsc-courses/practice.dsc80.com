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

We are told that as height increases, the model variance (complexity) also increases.

For the first subpart with the correct answer being `Option 2`: \
As we increase the complexity of the model, the Classifier is more closely fit to the training data. This means that the Classifier essentially 'memorizes' more of the training data as height increases, meaning that accuracy on the training data will also increase.

<average>84</average>

For the second subpart with the correct answer being `Option 3`:
Through similar reasoning for the subpart above, the Classifier becomes more closely fit to the training data as height increases, causing overfitting as values of height get higher and higher. This means that the accuracy of the Classifier will increase to a certain point alongside height, but will start to reduce after.

<average>71</average>

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

For the first subpart with the correct answer being `"red"`: \
From looking at the results of the k-fold cross validation, we see that the color red has the highest, and therefore the best, validation accuracy as it has the highest row mean (across all 4 folds).

<average>91</average>

For the second subpart with the correct answer being `True`: \
An example is shown below: 

| color    | Fold 1  | Fold 2  | Fold 3  | Fold 4  | average |
| -------- | ------- | ------- | ------- | ------- | ------- |
| color 1  | 0.8     |  0      |  0      |   0     | 0.2     |
| color 2  | 0       |  0.6    |  0      |   0     | 0.15    |
| color 3  | 0       |  0      |  0.1    |   0     | 0.025   |
| color 4  | 0       |  0      |  0      |   0.2   | 0.05    |
| color 5  | 0.7     |  0.5    |  0.01   |   0.1   | 0.3275  |

Where color 5 has the highest average validation accuracy across all folds, but is not the best in any one fold.

<average>94</average>

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

For the first subpart with the correct answer being `Option 3`: \
The training set is divided into k folds of equal size, resulting in k folds with size $\frac{n}{k}$.

<average>66</average>

For the second subpart with the correct answer being `Option 6`: \
For each combination of hyperparameters, row 5 is k - 1 times for training, and 1 time for validation. There are $h_1 * h_2$ combinations of hyperparameters, so row 5 is used for training $h_1 * h_2 * (k-1)$ times.

<average>76</average>

For the third subpart with the correct answer being `Option 8`: \
Building off of the explanation fo rthe previous subpart, row 5 is used for validation 1 times for each combination of hyperparameters, so the correct expression would be $h_1 * h_2$, which is not a provided option.

<average>69</average>


# END SOLN

# END SUBPROB

# END PROB