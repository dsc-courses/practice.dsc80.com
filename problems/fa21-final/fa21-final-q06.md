# BEGIN PROB

# BEGIN SUBPROB

Suppose you split a data set into a training set and a test set. You train your model on the training set and test it on the test set.

True or False: the training accuracy must be higher than the test accuracy.

( ) True
( ) False

# BEGIN SOLN

**Answer: ** False

There is no direct correlation between the training accuracy of a model and the test accuracy of the model, since the way you decide to split your data set is largely random. Thus there might be a possibility that your test accuracy ends up higher than your training accuracy. To illustrate this, suppose your training data consists of 100 data points and your test data consists of 1 data point. Now suppose your model achieves a training accuracy of 90%, and when you proceed to test it on the test set, your model predicts that singular data point correctly. Clearly youre test accuracy is now higher than your training accuracy.

<average>75</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose you create a 70%/30% train/test split and train a decision tree classifier. You find that the training accuracy is much higher than the test accuracy (90% vs 60%). Which of the following is likely to help significantly improve the test accuracy? Select all that apply. You may assume that the classes are balanced.

[ ] Reduce the number of features
[ ] Increase the number of features
[ ] Decrease the max depth parameter of the decision tree
[ ] Increase the max depth parameter of the decision tree

# BEGIN SOLN

**Answer: ** Option A and Option C

When your training accuracy is significaly higher than your test accuracy, it tells you that your model is perhaps overfitting the data. And thus we wish to reduce the complexity of our model. From the choices given, we can reduce the complexity of our model by reducing the number of features or decreasing the max depth parameter of the decision tree. (Recall that the greater depth the a decision tree model, the more complex the model).

<average>65</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose you are training a decision tree classifier as part of a pipeline with PCA. You will need to choose three parameters: the number of components to use in PCA, the maximum depth of the decision tree, and the minimum number of points needed for a leaf node. You'll do this using sklearn's GridSearchCV which performs a grid search with k-fold cross validation.

Suppose you'll try 3 possibilities for the number of PCA parameters, 5 possibilities for the max depth of the tree, 10 possibilities for the number of points needed for a leaf node, and use k=5 folds for cross-validation.

How many times will the model be trained by GridSearchCV?

# BEGIN SOLN

**Answer: ** 750

Note that our grid search will test every combination of hyperparameters for our model, which gives us a total of 3 * 5 * 10 = 150 combinations of hyperparameters. However, we all perform k-fold cross validation with 5 folds, meaning that our model is trained 5 times for each combination of hyperparameters, giving us a grand total of 5 * 150 = 750.

<average>84</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

The plot below shows the distribution of reported gas mileage for two models of car.

<center><img src='../assets/images/fa21-final/distributions.png' width=30%></center>

What test statistic is the best choice for testing whether the two empirical distributions came from different underlying distributions?

( ) the TVD
( ) the absolute difference in means
( ) the signed difference in means
( ) the Kolmogorov-Smirnov Statistic

# BEGIN SOLN

**Answer: ** Option D

TVD simply doesn't work here since we're not working with categorical data. Any sort of difference in means here wouldn't really tell us much either since both distributions seem to have basically the same mean. Thus to tell whether the two distributions are different, it would be best if we used K-S statistic.

<average>88</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose 1000 people are surveyed. One of the questions asks for the person's age. Upon reviewing the results of the survey, it is discovered that some of the ages are missing -- these people did not respond with their age. What is the most likely type of this missingness?

( ) Missing At Random
( ) Missing Completely At Random
( ) Not Missing At Random
( ) Missing By Design

# BEGIN SOLN

**Answer: ** Option C

The most likely mechanism for this is NMAR becuase there is a good reason why the missingess depends on the values themselves, namely, if one is a baby (like 1 or 2 years old), theres a a high probablility that they literally just aren't aware of their age and hence are less likely to answer. On the other end of the spectrum, older people might also refrain from answering their age. 

MAR doesn't work here because there aren't really any other columns that'll tell us anything about the likelihood of the missigness of the age column. MD clearly doesn't work here since we have no way of determining the missing values through the other columns. Alghough MCAR could be a possibility, it is more approrpiate that this problem illustrates NMAR rather than MCAR. 

<average>76</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider a data set consisting of the height of 1000 people. The data set contains two columns: height, and whether or not the person is an adult.

Suppose that some of the heights are missing. Among those whose heights are observed there are 400 adults and 400 children; among those whose height is missing, 50 are adults and 150 are children.

If the mean height is computed using only the observed data, which of the following will be true?

( ) the mean will be biased low
( ) the mean will be biased high
( ) the mean will be unbiased

# BEGIN SOLN

**Answer: ** Option B

Since there are more missing children heights than missing adult heights, (we will assume that adults are taller than children), the observed mean will be higher than the actual total mean, or the observed mean will be biased high.

<average>94</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

We have built two models which have the following accuracies: Model 1: Train score: 93%, Test score: 67%. Model 2: Train score: 84%, Test score: 80% Which of the following model will you choose to use to make future predictions on unseen data? You may assume that the class labels are balanced.

( ) Model 1
( ) Model 2

# BEGIN SOLN

**Answer: ** Model 2

When testing our models, we only really care about the test scores of our models, and so we'll typically choose the model with the higher test score which is Model 2.

<average>99</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose we retrain a decision tree model, each time increasing the `max_depth` parameter. As we do so, we plot the *test* error. What will we likely see?

( ) The test error will first decrease, then increase.
( ) The test error will decrease.
( ) The test error will first increase, then decrease.
( ) The test error will remain unchanged.

# BEGIN SOLN

**Answer: ** Option A

As we increase our `max_depth` parameter of our model, our model's test error will decrease. It'll keep decreasing until we've reached the optimal `max_depth` parameter of our model, for which after that the test error will start to increase (due to overfitting). Thus the correct answer is Option A. 

<average>87</average>

# END SOLN

# END SUBPROB

# END PROB