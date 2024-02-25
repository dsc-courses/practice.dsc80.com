# BEGN PROB
Consider three classifiers with the following confusion matrices:
<center><img src='../../assets/images/fa23-final/dsc80_final_models.png' width=65%></center>

# BEGN SUBPROB
Which model has the highest accuracy?

- Model A
- Model B
- Model C

# BEGN SOLN
**Answer**: Model B

Accuracy is defined as $\frac{number\;of\;correct\;predictions}{number\;of\;total\;predictions}$, so we sum the [Yes, Yes] and [No, No] cells to get the number of correct predictions and divide that by the sum of all cells as the number of total predictions. We see that Model B has the highest accuracy of 0.9 with that formula.

<average>98</average>

# END SOLN
# END SUBPROB

# BEGN SUBPROB
Which model has the highest precision?

- Model A
- Model B
- Model C

# BEGN SOLN
**Answer**: Model C

Precision is defined as $\frac{number\;of\;correct\;yes\;predictions}{number\;of\;total\;yes\;predictions}$, so the number of correct yes predictions is the [Yes, Yes] cell, while the number of total yes predictions is the sum of the [Yes] column. We see that Model C has the highest precision of $\frac{80}{85}$ with that formula.

<average>86</average>

# END SOLN
# END SUBPROB

# BEGN SUBPROB
Which model has the highest recall?

- Model A
- Model B
- Model C

# BEGN SOLN
**Answer**: Model B

Recall is defined as $\frac{number\;of\;correct\;yes\;predictions}{number\;of\;total\;yes\;actual}$, so the number of correct yes actual is the [Yes, Yes] cell, while the number of total yes actual is the sum of the [Yes] row. We see that Model B has the highest recall of $1$ with that formula.

<average>83</average>

# END SOLN
# END SUBPROB
# END PROB