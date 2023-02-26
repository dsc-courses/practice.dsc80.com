# BEGIN PROB

A credit card company wants to develop a fraud detector model which can flag transactions as fraudulent or not using a set of user and platform features. Note that fraud is a rare event (about 1 in 1000 transactions are fraudulent).

Suppose the model provided the following confusion matrix on the test set. Here, 1 (a positive result) indicates fraud and 0 (a negative result) indicates otherwise. Let's evaluate it to understand the model performance better.

<center><img src='../assets/images/fa21-final/confusion_matrix.png' width=30%></center>

Use this confusion matrix to answer the following questions.

# BEGIN SUBPROB

What is the accuracy of the model shown above? Your answer should be a number between 0 and 1.

# BEGIN SOLN

**Answer: ** 0.809

Accuracy is just calculated as the number of correct predictions divided by total predictions. From the table, we could see that there are 34 + 989 = 1023 correct predictions, and 34 + 153 + 87 + 989 = 1263, giving us a 1023/1263 or 0.809 accuracy.

<average>94</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

How many false negatives were produced by the model shown above?

# BEGIN SOLN

**Answer: ** 153

A false negative is when the model predicts a negative result  when the actual value is positive. So in the case of this model, a false negative would be when the model predicts 0 when the actual value should be 1. Simply looking at the table shows that there are 153 false negatives.

<average>91</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What is the precision of the model shown above?

# BEGIN SOLN

**Answer: ** 0.281

The precision of the model is given by the number of True Positives (TP), divided by the sum of the number of True Positives (TP) and False Positives (FP) or $\frac{TP}{TP + FP}$. Plugging the appropriate values in the formula gives us 34/(34 + 87) = 34/121 or 0.281.

<average>85</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What is the recall of the model shown above?

# BEGIN SOLN

**Answer: ** 0.18

The precision of the model is given by the number of True Positives (TP), divided by the sum of the number of True Positives (TP) and False Negatives (FN) or $\frac{TP}{TP + FN}$. Plugging the appropriate values in the formula gives us 34/(34 + 153) = 34/187 or 0.18.

<average>82</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

What is the accuracy of a "naive" model that always predicts that the transaction is not fraudulent? Your answer should be a number between 0 and 1.

# BEGIN SOLN

**Answer: ** 0.852

If our model always predicts not fraudulent or 0, then we will get an accuracy of $\frac{87+989}{34+153+87+989}$ or 0.852

<average>78</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Describe a simple model that will achieve 100% recall despite it being a poor  classifier.

# BEGIN SOLN

**Answer: ** A model that always guesses fraudulent.

Recall that the formula for recall (no pun intended) is given by $\frac{TP}{TP + FN}$. Thus we reason that if we want to achieve 100% recall, we should simply achieve no False Negatives (or FN = 0), since that will gives us $\frac{TP}{TP + 0}$, which is obviously just 1. Therefore, if we never guess 0 or non-fraudulent, we'll never get any False Negatives (b/c getting any FN requires our model to predict negatives for some values). Hence a mmodel that always guesses fraudulent will achieve 100% recall, despite obviously being a bad model.

<average>86</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose you consider false negatives to be more costly than false positives, where a "positive" prediction is one for fraud. Assuming that precision and recall are both high, which is better for your purposes:

( ) A model with higher recall than precision.
( ) A model with higher precision than recall.

# BEGIN SOLN

**Answer: ** Option A

Since we consider false negatives to be more costly, it would therefore make sense to favor on a model that puts more emphasis on recall because, again, the formula for recall is given by $\frac{TP}{TP + FN}$. O the other hand, precision doesn't care about false negatives, so the answer here is Option A.

<average>85</average>

# END SOLN

# END SUBPROB

# END PROB