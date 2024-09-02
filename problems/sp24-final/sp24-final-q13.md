# BEGIN PROB

Suppose you fit a logistic regression classifier. The classifier's predictions
on a test set of 5 points are shown below, along with the actual labels.

<center><img src="../../assets/images/sp24-final/eval.png" style="width: 30%; height: auto;"></center>


Recall that for logistic regression, we must also choose a threshold `$ \tau $` to convert the predicted probabilities to predicted labels. For this question, assume that `$ 0 < \tau < 1 $`. Precision is undefined when the classifier doesn't make any positive predictions (since `$\frac{0}{0}$` is undefined). For each question, show your work and draw a box around your final answer in the space provided. Each of your final answers should be a single number.


# BEGIN SUBPROB

What is the **lowest** possible precision for any threshold `$ \tau $`?

# BEGIN SOLN

**Answer:**

The lowest precision happens when `$ \tau $` is less than 0.3. In this case, the classifier predicts all points are 1, which gives a precision of `$ \frac{3}{5} $`.


# END SOLN

# END SUBPROB



# BEGIN SUBPROB

What is the **lowest** possible recall for any threshold `$ \tau $`?

# BEGIN SOLN

**Answer:**

The lowest recall happens when `$ \tau $` is greater than 0.7. In this case, the classifier predicts all points are 0, which gives a recall of 0.


# END SOLN

# END SUBPROB



# BEGIN SUBPROB

What is the **highest** possible recall if the classifier achieves a precision of 1?


# BEGIN SOLN

**Answer:**

If precision is 1, the threshold must be greater than 0.4. Of these thresholds, the recall is greatest when the threshold is between 0.4 and 0.6. In this case, the recall is $\frac{2}{3}$.


# END SOLN

# END SUBPROB

# END PROB
