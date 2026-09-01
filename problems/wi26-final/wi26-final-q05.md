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

For each point, the 3 nearest neighbors are found using Euclidean distance in the `"Age"`–`"AppointmentHour"` plane. Four of the five positive-class points are correctly classified; one positive point is misclassified. That gives accuracy $\frac{20}{25} = 0.8$. Precision is $\frac{4}{5} = 0.8$ (4 true positives out of 5 predicted positives), and recall is $\frac{4}{4} = 1$ (all actual positives were found).

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

On this dataset, every point is correctly classified by its 3 nearest neighbors, so accuracy, precision, and recall are all 1.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Finally, consider a 15-nearest neighbor classifier, which has the same accuracy on both datasets. What is that accuracy?

# BEGIN SOLUTION

**Answer:** $0.8$

With $k = 15$, the classifier uses a majority vote over nearly the entire dataset (25 points). This yields accuracy $0.8$ on both scatter plots.

# END SOLUTION

# END SUBPROB

# END PROB
