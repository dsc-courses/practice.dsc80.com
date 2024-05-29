# BEGIN PROB

Jasmine and Aritra are trying to build models that predict the number of open rooms a hotel room has. To do so, they use `price`, the average listing price of rooms at the hotel, along with a one hot encoded version of the hotel’s `chain`. **For the purposes of this question, assume the only possible hotel chains are Marriott, Hilton, and Other.**

# BEGIN SUBPROB

First, Jasmine fits a linear model *without* an intercept term. Her prediction rule, $H_1$, looks like:

$$H_{1}(x) = w_1 \cdot \texttt{price} + w_2 \cdot \texttt{is\_Marriott} + w_3 \cdot \texttt{is\_Hilton} + w_4 \cdot \texttt{is\_Other}$$

After fitting her model, $\vec{w}^* = \begin{bmatrix}−0.5 \\ 200 \\ 300 \\ 50 \end{bmatrix}$.

1. The Marriott Marquis San Diego Marina, a hotel in the Marriott chain, has an average listing price of $250.  How many open rooms does $H_1$ predict it has? Give your answer as a number with no variables.
2. The Marriott Marquis San Diego Marina actually has 45 open rooms. What’s the squared loss of your prediction above? Give your answer as a number with no variables.
3. True or False: Because your answer to (ii) above is not 0, it means there were no hotels in the Marriott chain with an average listing price of $250 in the training set.
 d
( ) True
( ) False

# BEGIN SOLUTION

**Answers:**

1. 75
2. 900
3. False

If we plug in the weights from $\vec{w}^*$ into the equation for $H_1(x)$, noting that the values of the one-hot variables are either 0 or 1, we get $-0.5 \cdot 250 + 200 \cdot 1 + 300 \cdot 0 + 50 \cdot 0$, or $-125 + 200$, or 75.

For part 2, the difference between predicted and actual number of rooms is $75 - 45 = 30$, and the squared loss is simply $30^2 = 900$.

For part 3, the answer is False, since the fact that our best-fit line has an error at a given input does not mean that this input was not seen in the training data. In other words, the line of best fit does not always have to pass through all of the training points (and due to overfitting, in most cases you don't want it to).

<average>87</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Then, on the same training set, Aritra fits a linear model, *with* an intercept term but without the `is_Other` feature. His new prediction rule, $H_2$, now looks like:

$$H_2(x) = \beta_0 + \beta_1 \cdot \texttt{price} + \beta_2 \cdot \texttt{is\_Marriott} + \beta_3 \cdot \texttt{is\_Hilton}$$

After fitting his model, Aritra finds optimal coefficients $\beta_{0}^{*}$, $\beta_{1}^{*}$, $\beta_{2}^{*}$, and $\beta_{3}^{*}$.

1. The training RMSE of $H_2$ is equal to the training RMSE of $H_1$.

( ) True
( ) False

2. Assuming we use the same test set, the test RMSE of $H_2$ is equal to the test RMSE of $H_1$.

( ) True
( ) False

# BEGIN SOLUTION

**Answers:**

1. True
2. True

In model $H_1$, there is redundant information in the one-hot encoded features, creating multicollinearity. The second model $H_2$ removes the `is_Other` feature, but the intercept term it is replaced with serves a similar function. When `is_Other` is true, the prediction of $H_1$ is $w_1 \cdot \texttt{price} + w_4$, and the prediction of $H_2$ is $\beta_1 \cdot \texttt{price} + \beta_0$. The multicollinearity in $H_1$ doesn't affect model performance relative to model 2, but it will yield different parameter estimates since there will be multiple solutions, unlike with $H_2$. However, the models will have equivalent best solutions, even if the parameters differ, so both parts are True.

<average>53</average>

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

As a reminder, 

$$H_{1}(x) = w_1 \cdot \texttt{price} + w_2 \cdot \texttt{is\_Marriott} + w_3 \cdot \texttt{is\_Hilton} + w_4 \cdot \texttt{is\_Other}$$

$$\vec{w}^* = \begin{bmatrix}−0.5 \\ 200 \\ 300 \\ 50 \end{bmatrix}$$

$$H_2(x) = \beta_0 + \beta_1 \cdot \texttt{price} + \beta_2 \cdot \texttt{is\_Marriott} + \beta_3 \cdot \texttt{is\_Hilton}$$

After fitting his model, Aritra finds $\beta_{0}^{*} = 50.$ Given that, what are $\beta_{1}^{*}$, $\beta_{2}^{*}$, and $\beta_{3}^{*}$? Give your answers as numbers with no variables.

# BEGIN SOLUTION

**Answers:**

1. -0.5
2. 150
3. 250

As we saw in the previous question, these models should yield an equivalent best-fit line. The relationship between `price` and predicted outcome will be the same, so $\beta_{1}^{*}$ will be $-0.5$, the same weight as in $H_1$.

If $\beta_{0}^{*} = 50$, this means we are adding 50 to all predictions, and that the "adjustments" we make to the prediction for `is_Marriott` and `is_Hilton` should therefore be reduced to compensate for this; therefore, the new weights $\beta_{2}^{*}$ and $\beta_{3}^{*}$ will be 150 and 250.

<average>69</average>

# END SOLUTION

# END SUBPROB

# END PROB