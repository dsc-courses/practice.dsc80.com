# BEGIN PROB

# BEGIN SUBPROB
Suppose you split a data set into a training set and a test set. You train a classifier on the training set and test it on the test set.

True or False: the training accuracy must be higher than the test accuracy.

( ) True
( ) False

# BEGIN SOLN
**Answer: ** False

There is no direct correlation between the training accuracy of a model and the test accuracy of the model, since the way you decide to split your data set is largely random. Thus there might be a possibility that your test accuracy ends up higher than your training accuracy. To illustrate this, suppose your training data consists of 100 data points and your test data consists of 1 data point. Now suppose your model achieves a training accuracy of 90%, and when you proceed to test it on the test set, your model predicts that singular data point correctly. Clearly your test accuracy is now higher than your training accuracy.

<average>97</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose you are using `sklearn` to train a decision tree model to predict whether a data science student is enrolled in DSC 80 or not based on several pieces of information, including their hours spent coding per week and whether or not they have heard of the Kolmogorov-Smirnov test statistic.

Suppose you train your model, but achieve much lower training and test
accuracies than you expect. When you look at the data and make predictions
yourself, you are easily able to achieve higher train and test accuracies.

What should be done to improve the performance of the model?

( ) Decrease the `max_depth` hyperparameter; the model is "overfitting".
( ) Increase the `max_depth` hyperparameter; the model is "underfitting".

# BEGIN SOLN
**Answer: ** Option A

The fact that your model has a low training accuracy means that your model is not complex enough to capture the trends that are present in the data and thus likely "underfitting". This means that you should increase the `max_depth` parameter.

<average>73</average>

# END SOLN

# END SUBPROB

# END PROB