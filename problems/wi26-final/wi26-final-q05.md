# BEGIN PROB

In Lab 9, you learned about $k$-nearest neighbors regression. A related machine learning algorithm is $k$-nearest neighbors classification, in which predictions are made by finding the $k$ points in the training data that are nearest to the point we are trying to classify. We predict the class that the majority of those $k$ points belong to (similar to the way in which decision trees in a random forest vote on a prediction). In this problem, we'll use the standard Euclidean ($L_2$) distance to measure the distance between points.

In this problem, we'll try to predict `"Wait"` based on `"Age"` and `"AppointmentHour"`, where `"AppointmentHour"` is the hour from the `"AppointmentTime"` column.

# BEGIN SUBPROB

Suppose the training data consists only of the 25 points shown below. Determine the accuracy, precision, and recall of a 3-nearest neighbors classifier on this data.

<center><img src="../../assets/images/wi26-final/scatter1.png" width=450></center>

1. Accuracy:

2. Precision:

3. Recall:

# BEGIN SOLUTION

**Answers:** $0.8$, $0.8$, $1$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Now suppose the training data consists only of the 25 points shown below. Determine the accuracy, precision, and recall of a 3-nearest neighbors classifier on this data.

<center><img src="../../assets/images/wi26-final/scatter2.png" width=450></center>

1. Accuracy:

2. Precision:

3. Recall:

# BEGIN SOLUTION

**Answers:** $1$, $1$, $1$

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Finally, consider a 15-nearest neighbor classifier, which has the same accuracy on both datasets. What is that accuracy?

# BEGIN SOLUTION

**Answer:** $0.8$

# END SOLUTION

# END SUBPROB

# END PROB
