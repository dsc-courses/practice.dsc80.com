# BEGIN PROB

Sam Altman has trained a Logistic Regression model to classify emails into "Spam" / "Non-Spam" categories/classes. Here, 'Spam' is the positive class. Once the model is trained, Sam opted to evaluate the model performance on the testing set. The Logistic Regression outputs a value between 0 and 1. When the output of the Logistic Regression model is greater than or equal to the threshold, the email is classified as a 'Spam' email. By varying the threshold, Sam creates the following Precision-Recall graph.

<center><img  src='../assets/images/sp23-final/q2_prgraph.png'  width=40%></center>

# BEGIN SUBPROB

Which point corresponds to the **highest** threshold value?

( ) A
( ) B
( ) C
( ) D

# BEGIN SOLN
**Answer:** B

Remember that precision measures the predicted positive values that were 
actually positive, while recall measures actually positive values that were
predicted as being positive. The highest threshold is 1, and we would expect 
that when the model predicts 1 the email is actually likely Spam, but that the 
model does not predict 1 for every Spam email. This means that at the highest 
threshold, precision is almost perfect while recall is extremely low, 
corresponding to point B on the plot.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider the following confusion matrix with "Spam" and "Not Spam" classes where 'Spam' is the positive class.

<center><img  src='../assets/images/sp23-final/q2b.png'  width=40%></center>

Suppose the recall of Sam's classifier is 0.75 and the precision of Sam's classifier is 0.6. 
What are the values of X and Y? Give your answers as positive integers.

`X` ____

`Y` ____

# BEGIN SOLN
**Answer:** X = 15, Y = 10

We are given that $FN = 5$ and $TN = 50$ \
Remember that $Precision = \frac{TP}{(TP+FP)}$ and $Recall = \frac{TP}{(TP+FN)}$

To calculate TP (X) use the formula for recall: \
$0.75 = \frac{TP}{(TP+5)}$ \
$0.75 \cdot (TP+5)* = TP$ \
$0.75 \cdot TP+ 5 \cdot 0.75  = TP$ \
$0.25 \cdot TP = 3.75$ \
$TP = 15$ \
Therefore X = 15

To calculate FP (Y) use the formula for precision: \
$0.6 = \frac{15}{(15+FP)}$ \
$0.6 \cdot (15+FP)* = 15$ \
$0.6 \cdot 15 + 0.6 \cdot FP = 15$ \
$0.6 \cdot FP = 6$ \
$FP = 10$ \
Therefore Y = 10

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose you want to predict if people are depressed based on their Electrocardiogram ECG signal. To train your model, you sampled ECG data from 100 people, with 80% of them not being depressed. Which of the following metrics is definitely not suitable for evaluating this binary classification model? Select all that apply.

( ) Precision 
( ) Recall 
( ) Accuracy 
( ) F1 Score

# BEGIN SOLN
**Answer:** Accuracy

Because the the data set is imbalanced (80% of the data belongs to one class), 
accuracy is not a suitable metric to evaluate this classification model. This 
is because accuracy does not differentiate between if the accuracy was achieved 
on predictions made for the majority or the minority class, and it is highly 
likely in a biased dataset that a high accuracy is achieved based on making 
correct predictions solely for the majority, but not the minority class.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
For the purposes of such a binary depression classification task, which is more important?

( ) high precision
( ) high recall

# BEGIN SOLN
**Answer:** High recall

High recall is relatively more important for medical tests generally. 
High recall minimizes FN, while high precision minimizes FP. A high recall 
ensures that you are capturing the people who have the condition, and it is 
usually worse in these settings to think someone does not have a condition when 
they actually do, than the other way around. If your system fails to detect 
the condition, the condition goes undiagnosed and unaddressed, so it is more 
important to minimize FN.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
For the purposes of determining whether someone committed a crime, which is more important?

( ) high precision 
( ) high recall

# BEGIN SOLN
**Answer:** High precision

High precision is relatively more important since you do not want to punish 
someone who did not commit the crime (want to minimize FP). See the previous 
explanation for more details about the differences between high recall and 
high precision.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

In the context of a spam detector, an important email from a legitimate source ending up in one's spam folder is an example of what?

( ) True positive 
( ) False positive 
( ) False negative 
( ) True negative

# BEGIN SOLN
**Answer:** False positive

For a spam detector, detetcted an email as Spam is equivalnet to assigning it 
as belonging to the positive class. Since the email was classified by the spam 
detector as spam, it is positive. However, since it was not actually spam, 
it is a false positive.

# END SOLN

# END SUBPROB

# END PROB