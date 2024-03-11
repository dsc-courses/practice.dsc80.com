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

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
For the purposes of such a binary depression classification task, which is more important?

( ) high precision
( ) high recall

# BEGIN SOLN
**Answer:** High recall

High recall is relatively more important for medical tests generally. A high recall ensures that you are capturing the people who have the conditions. If your system fails to detect the conditions, the condition goes undiagnosed and unaddressed.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
For the purposes of determining whether someone committed a crime, which is more important?

( ) high precision 
( ) high recall

# BEGIN SOLN
**Answer:** High precision

High precision is relatively more important since you don't want to punish someone who did not commit the crime.

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

Since the email was classified by the spam detector as spam, it is "positive". However, since it was not actually spam, it's a "false" positive.

# END SOLN

# END SUBPROB

# END PROB