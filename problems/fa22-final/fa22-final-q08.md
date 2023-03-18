# BEGIN PROB

The next four questions concern the following example.

A Silicon Valley startup candy company buys a factory from a lightbulb company and repurposes some of the existing equipment to make chocolate bars with the goal of disrupting the candy industry. Their IPO is delayed, however, when they discover that some of their chocolate bars contain broken glass.

The company's engineers quickly build an AI which looks at the chocolate
bars coming off of the conveyor belt and predicts which bars contain broken glass ("yes") and which don't ("no"). The results are shown in the
following confusion matrix:

<center><img src='../assets/images/fa22-final/confusion.png' width=30%></center>

# BEGIN SUBPROB

What is the accuracy of their model as a percentage (between 0% and 100%)?

# BEGIN SOLN
**Answer: ** 91%

The accuracy of a model is given by the number of correct predictions divided by the total number of predictions. To tell if a prediction is correct, we simply see if the predicted value matches the actual value. In this case, our model's accuracy is just $\frac{87+4}{87+6+3+4} = \frac{91}{100}$ which is just 91%.

<average>95</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
What is the recall of their model as a percentage (between 0% and 100%)?

# BEGIN SOLN
**Answer: ** 40%

The recall of a model is given by the number of True Positives divided by the sum of True Positives and False Negatives. A True Positive is when the model correctly predicts a Positive value (in this case, a Positive value is "Yes"), and a False Negative is when a model incorrectly predicts a Negative value. Thus the answer is just $\frac{4}{6+4} = \frac{4}{10}$ which is just 40%.

<average>92</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
From a safety perspective, which metric should be maximized in this situation?

( ) Precision
( ) Recall

# BEGIN SOLN
**Answer: ** Recall

From a safetly perspective, it makes sense that we should maximize catching broken glass in the chocolate bars. This means that we should minimize False Negative values, which means maximizing Recall.

<average>100</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose the company's investors wish to improve the model's precision.
Which should they do (besides hire better data scientists)?

( ) Lower their model's threshold for predicting that a bar contains glass, thus throwing out more candy.
( ) Raise their model's threshold for predicting that a bar contains glass, thus throwing out less candy.

# BEGIN SOLN
**Answer: ** Option B

The precision of a model is given by the number of True Positives divided by the sum of True Positives and False Positives. Thus to maximumize the precision of a model, we should minimize the number of False Positives. To do this, simply raising the model's threshold for predicting Positive values would result in less False Positives. Thus the answer is Option B.

<average>97</average>

# END SOLN

# END SUBPROB

# END PROB