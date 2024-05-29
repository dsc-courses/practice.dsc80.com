# BEGIN PROB

Diego also wants to build a model that predicts the number of open rooms a hotel has, given various other features. He has a training set with 1200 rows available to him for the purposes of training his model.

# BEGIN SUBPROB

Diego fits a regression model using the `GPTRegression` class. `GPTRegression` models have several hyperparameters that can be tuned, including `context_length` and `sentience`.

To choose between 5 possible values of the hyperparameter `context_length`, Diego performs $k$-fold cross-validation.

1. How many total times is a `GPTRegression` model fit?

( ) $4k$
( ) $5k$
( ) $240k$
( ) $6000k$
( ) $4(k − 1)$
( ) $5(k − 1)$
( ) $240(k − 1)$
( ) $6000(k − 1)$

2. Suppose that every time a `GPTRegression` model is fit, it appends the number of points in its training set to the list `sizes`. Note that after performing cross- validation, `len(sizes)` is equal to your answer to the previous subpart.

What is `sum(sizes)`?

( ) $4k$
( ) $5k$
( ) $240k$
( ) $6000k$
( ) $4(k − 1)$
( ) $5(k − 1)$
( ) $240(k − 1)$
( ) $6000(k − 1)$

# BEGIN SOLUTION

**Answers:**

1. $5k$
2. $6000(k-1)$

When we do $k$-fold cross-validation for one single hyperparameter value, we split the dataset into $k$ folds, and in each iteration $i$, train the model on the remaining $k-1$ folds and evaluate on fold $i$. Since every fold is left out and evaluated on once, the model is fit in total $k$ times. We do this once for every hyperparameter value we want to test, so the total number of model fits required is $5k$.

In part 2, we can note that each model fit is performed on the same size of data -- the size of the remaining $k-1$ folds when we hold out a single fold. This size is $1 - \frac{1}{k} = \frac{k-1}{k}$ times the size of the entire dataset, in this case, $1200 \cdot \frac{k-1}{k}$, and we fit a model on a dataset of this size $5k$ times. So, the sum of the training sizes for each model fit is:

$$5k \cdot \frac{k-1}{k} \cdot 1200 = 6000(k-1)$$

<average>66</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

The average training error and validation error for all 5 candidate values of `context_length` are given below.

<center><img src="../../assets/images/wi24-final/validation.png" width=600></center>

Fill in the blanks: As `context_length` increases, model complexity `__(i)__`. The optimal choice of `context_length` is `__(ii)__`; if we choose a `context_length` any higher than that, our model will `__(iii)__`.

1. What goes in blank (i)?

( ) increases
( ) decreases

2. What goes in blank (ii)?

( ) 0.1
( ) 1
( ) 10
( ) 100
( ) 1000

3. What goes in blank (iii)?

( ) overfit the training data and have high bias
( ) underfit the training data and have high bias
( ) overfit the training data and have low bias
( ) underfit the training data and have low bias

# BEGIN SOLUTION

**Answers:**

1. decreases
2. 100
3. underfit the training data and have high bias

In part 1, we can see that as `context_length` increases, the training error increases, and the model performs worse. In general, higher model complexity leads to better model performance, so here, increasing `context_length` is *reducing* model complexity.

In part 2, we will choose a `context_length` of 100, since this parameterization leads to the best validation performance. If we increase `context_length` further, the validation error increases.

In part 3, since increased `context_length` indicates *less* complexity and worse training performance, increasing the `context_length` further would lead to underfitting, as the model would lack the expressiveness or number of parameters required to capture the data. Since training error represents model bias, and since high variance is associated with *over*fitting, a further increase in `context_length` would mean a more biased model.

<average>65</average>

# END SOLUTION

# END SUBPROB

# END PROB
