# BEGIN PROB

Suppose Yutian builds a classifier that predicts whether or not a hotel provides free parking. The confusion matrix for her classifier, when evaluated on our training set, is given below.

<center><img src="../../assets/images/wi24-final/confusion.png" width=550></center>

# BEGIN SUBPROB

What is the precision of Yutian’s classifier? Give your answer as a simplified fraction.

# BEGIN SOLUTION

**Answer:** $\frac{8}{13}$

Precision is the proportion of predicted positives that actually were positives. So, given this confusion matrix, that value is $\frac{8}{8 + 5}$, or $\frac{8}{13}$.

<average>89</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Fill in the blanks: In order for Yutian’s classifier’s recall to be equal to its precision, `__(i)__` must be equal to `__(ii)__`.

1. What goes in blank (i)?

( ) $A$
( ) $B$

2. What goes in blank (ii)?

( ) 2
( ) 3
( ) 4
( ) 5
( ) 6
( ) 8
( ) 13
( ) 14
( ) 20 
( ) 40
( ) 50
( ) 80

# BEGIN SOLUTION

**Answer:** 

1. $B$
2. 5

We already know that the precision is $\frac{8}{13}$. Recall is the proportion of true positives that were indeed classified positives, which in this matrix is $\frac{8}{B + 8}$. So, in order for precision to equal recall, $B$ must be 5.

<average>96</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Now, suppose both $A$ and $B$ are unknown. Fill in the blanks: In order for Yutian’s classifier’s recall to be equal to its accuracy, `__(i)__` must be equal to `__(ii)__`.

1. What goes in blank (i)?

( ) $A + B$
( ) $A - B$
( ) $B - A$
( ) $A \cdot B$
( ) $\frac{A}{B}$
( ) $\frac{B}{A}$

2. What goes in blank (ii)?

( ) 2
( ) 3
( ) 4
( ) 5
( ) 6
( ) 8
( ) 13
( ) 14
( ) 20 
( ) 40
( ) 50
( ) 80

*Hint: To verify your answer, pick an arbitrary value of A, like A = 10, and solve for the B that sets the model’s recall equal to its accuracy. Do the specific A and B you find satisfy your answer above?*

# BEGIN SOLUTION

**Answer:** 

1. $A \cdot B$
2. 40

We can solve this problem by simply stating recall and accuracy in terms of the values in the confusion matrix. As we already found, recall is $\frac{8}{B+8}$. Accuracy is the sum of correct predictions over total number of predictions, or $\frac{A + 8}{A + B + 13}$. Then, we simply set these equal to each other, and solve.

$$\frac{8}{B+8} = \frac{A + 8}{A + B + 13}$$
$$8(A + B + 13) = (A + 8)(B + 8)$$
$$8A + 8B + 104 = AB + 8A + 8B + 64$$
$$104 = AB + 64$$
$$AB = 40$$

<average>79</average>

# END SOLUTION

# END SUBPROB

# END PROB







