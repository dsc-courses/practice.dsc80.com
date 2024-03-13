# BEGIN PROB

Let's recall Project 1, where the concept of redemption score was introduced. According to this idea, the course could reward for showing improvement in their understanding of the earlier ideas in the course on the final exam.
Suppose the final exam was worth 80 points. A total of 40 points were associated with questions 2, 4, 6, 8, and 9, which were the redemption questions. The class's mean score on just the redemption questions was 0.8, with a standard deviation of 0.2.
Suppose the midterm exam was worth 70 points. The class's mean score on the midterm exam was 0.6, with a standard deviation of 0.5.
Tiffany, a student in the course, earned a $\frac{60}{80}$ on the final exam, including a $\frac{30}{40}$ on the redemption questions, and a $\frac{50}{70}$ on the midterm exam.

# BEGIN SUBPROB
Should her final exam score be replaced using the rule in Project 1?

( ) Yes
( ) No

# BEGIN SOLN
**Answer:** No

Recall that z-score = $\frac{score - mean}{standard\ deviation}$

Tiffany's raw redemption score: $\frac{30}{40}$
Tiffany's redemption z-score:  $\frac{\frac{30}{40} - 0.8}{0.2} = -0.25$ 

Tiffany's raw midterm score: $\frac{50}{70}$
Tiffany's midterm z-score:  $\frac{\frac{50}{70} - 0.6}{0.5} \approx 0.23$ 

Since Tiffany's redemption z-score is lower than her midterm z-score, she 
should not get her final exam score replaced.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Which metric did you use in Project 1 to conclude that?

# BEGIN SOLN
**Answer:** z-score

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Suppose Tony Stark has implemented a decision tree classifier from scratch and trained it using different criteria and maximum depths in a 10-fold cross-validation. Based on the results table below, which row (numbered 1 to 8) should he choose as his final model?

<center><img  src='../assets/images/sp23-final/q9.png'  width=40%>  </center>

# BEGIN SOLN
**Answer:** 7

The decision for the best selection of model hyperparameters in a cross validation 
is based on the how well the model performs on the validation data. the accuracy of the 
models on the test data in irrelevant, since that can only be found after a model is selected.

The model with the best performance on the validation data (highest accuracy on validation data), 
corresponds to the model indicated in row 7.

# END SOLN

# END SUBPROB

# END PROB