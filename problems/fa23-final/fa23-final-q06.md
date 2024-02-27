# BEGIN PROB
Consider three classifiers with the following confusion matrices:
<center><img src='../../assets/images/fa23-final/dsc80_final_models.png' width=65%></center>

# BEGIN SUBPROB

Which model has the highest accuracy?

( ) Model A
( ) Model B
( ) Model C

# BEGIN SOLN
**Answer**: Model B

Accuracy is defined as $\frac{\text{number\;of\;correct\;predictions}}{\text{number\;of\;total\;predictions}}$, so we sum the (Yes, Yes) and (No, No) cells to get the number of correct predictions and divide that by the sum of all cells as the number of total predictions. We see that Model B has the highest accuracy of 0.9 with that formula. (Note that for simplicity, the confusion matrices are such that the sum of all values is 100 in all three cases.)

<average>98</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB

Which model has the highest precision?

( ) Model A
( ) Model B
( ) Model C

# BEGIN SOLN
**Answer**: Model C

Precision is defined as $\frac{\text{number of correctly predicted yes values}}{\text{total number of yes predictions}}$, so the number of correctly predicted yes values is the (Yes, Yes) cell, while the total number of yes predictions is the sum of the Yes column. We see that Model C has the highest precision, $\frac{80}{85}$, with that formula.

<average>86</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB

Which model has the highest recall?

( ) Model A
( ) Model B
( ) Model C

# BEGIN SOLN
**Answer**: Model B

Recall is defined as $\frac{\text{number of correctly predicted yes values}}{\text{total number of values actually yes}}$, so the number of correctly predicted yes values is the (Yes, Yes) cell, while the total number of values that are actually yes is the sum of the Yes row. We see that Model B has the highest recall, $1$, with that formula.

<average>83</average>

# END SOLN
# END SUBPROB
# END PROB