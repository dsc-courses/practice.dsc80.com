# BEGIN PROB 
Every week, Lauren goes to her local grocery store and buys a varying amount of vegetable but always buys exactly one pound of meat (either beef, fish, or chicken). We use a linear regression model to predict her total grocery bill. We've collected a dataset containing the pounds of vegetables bought, the type of meat bought, and the total bill. Below we display the first few rows of the dataset and two plots generated using the entire training set.

<center><img src='../../assets/images/fa23-final/dsc80_final_q9.png' width=65%></center>

# BEGIN SUBPROB
Suppose we fit the following linear regression models to predict `'total'`. Based on the data and visualizations shown above, determine whether the fitted model weights are positive ($+$), negative ($-$), or exactly 0. The notation `meat=beef` refers to the one-hot encoded `'meat'` column with value $1$ if the original value in the `'meat'` column was `beef` and $0$ otherwise. Likewise, `meat=chicken` and `meat=fish` are the one-hot encoded `'meat'` columns for `chicken` and `fish`, respectively.

i.   $H(x) = w_0$
$\;\;\;\;w_0: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
ii.  $H(x) = w_0 + w_1  \cdot$ `veg`
$\;\;\;\;w_0: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
$\;\;\;\;w_1: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
iii. $H(x) = w_0 + w_1  \cdot$ `(meat=chicken)`
$\;\;\;\;w_0: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
$\;\;\;\;w_1: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
iv. $H(x) = w_0 + w_1  \cdot$ `(meat=beef)` $+\:w_2\:\cdot$ `(meat=chicken)`
$\;\;\;\;w_0: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
$\;\;\;\;w_1: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
$\;\;\;\;w_2: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
v. $H(x) = w_0 + w_1  \cdot$ `(meat=beef)` $+\:w_2\:\cdot$ `(meat=chicken)`$+\:w_3\:\cdot$ `(meat=fish)`
$\;\;\;\;w_0: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
$\;\;\;\;w_1: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
$\;\;\;\;w_2: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
$\;\;\;\;w_3: +\;\;,\;\;-\;\;,\;\;0\;\;,\;\;$Not enough info
# BEGIN SOLN
**Answer**: 
i. $w_0: +$
ii. $w_0: +\;\;,\;\; w_1:+$
iii. $w_0: +\;\;,\;\; w_1:-$
iv. $w_0: +\;\;,\;\; w_1:-\;\;,\;\;w_2: -$
v. $w_0:$ Not enough info $\;\;,\;\; w_1:$ Not enough info$\;\;,\;\;w_2:$ Not enough info$\;\;,\;\; w_3:$ Not enough info

i. We know $w_0$ must be $+$ because `'total'` is always positive and nothing else is predicing it.

ii. We can see from the graph of `'total'` and `'veg'` that the y-intercept $w_0$  is $+$, and that veg increases `'total'` so it also $+$.

iii. We know $w_0$ is positive because the total is  positive even when there is no chicken. We then also see from the boxplots on the right that samples that are `meat=chicken` are associated with a lower `'total'`. Therefore, $w_1$ is $-$.

iv. We know $w_0$ is positive because the total is  positive even when there is no chicken or beef. We then also see from the boxplots on the right that samples that are `meat=beef` or `meat=chicken` are associated with a lower `'total'` than `meat=fish`. Therefore, $w_1$ is $-$ since when we have no `beef` or `chicken` we have a higher `'total'`.

v. We cannot know any of the weights with the given data. For example, $w_0$ could be positive or negative depending on the scale of the other weights, since we know at least one of the other weights $w_1$, $w_2$, or $w_3$ will be nonzero as Lauren always buys a pound of meat.

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Suppose we fit the model: $H(x) = w_0 + w_1 \cdot$`veg`$+\:w_2\:\cdot$`(meat=beef)`$+\:w_3\:\cdot$`(meat=fish)`
After fitting, we find that $\vec{w}=[-3, 5, 8, 12]$

What is the prediction of this model on the **first** point in our dataset?
- -3
- 2
- 5
- 10
- 13
- 22
- 25
# BEGIN SOLN
**Answer**: 10

Plugging in our weights to the model $H(x)$ and filling in data from the row 
| veg | meat | total |
|-----|------|-------|
| 1   | beef | 13    |
We get: $-3 + 5(1) + 8(1) + 12(0) = 10$

<average>93</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Following the same model $H(x)$ and weights from the previous problem, what is the loss of this model on the **second** point in our dataset, using squared error loss?

- 0
- 1
- 5
- 6
- 8
- 24
- 25
- 169
# BEGIN SOLN
**Answer**: 25

Squared error loss is defined as 
$$\frac{1}{N}\sum^N_{i=1}(y_i-\hat{y}_i)^2$$
Our equation gives us:
$$-3 + 5(3) + 8(0) + 12(1) = 24$$
We can plug in our predicted value to the squared error loss equation to get:
$$\frac{1}{1}\sum^1_{i=1}(19-24)^2$$
$$(19-24)^2 = 25$$

<average>84</average>

# END SOLN
# END SUBPROB

# BEGIN SUBPROB
Determine how each change below affects model bias and variance compared to the model $H(x)$ described at the top of this page. **For each change (i., ii., iii., iv.), choose all the options below that apply.**
- Increase bias
- Decrease bias
- Increase variance
- Decrease variance

i. Add degree $3$ polynomial features.
ii. Add a feature of numbers chose at random between $0$ and $1$.
iii. Collect $100$ more points for the training set.
iv. Don't use the `veg` feature.
# BEGIN SOLN
**Answer**:
i. Decrease bias, Increase variance
ii. Increase variance
iii. Decrease variance
iv. Increase bias, decrease variance

i. We can see that our `'total'` is likely best fit by a second or third degree polynomial from the second graph above. Therefore, adding a higher degree polynomial feature will decrease bias as it fits better, but will increase variance as the higher degree exaggerates possible value ranges.

ii. Random numbers will not change bias since they are random,  but it will increase the variance as possible values can now be $1$ greater.

iii. Assuming our dataset is already a fair representation of all samples, adding more data will not change bias, but it will decrease variance as outliers become less impactful.

iv. Ignoring a feature that has a correlation to the output will increase bias as the model will be missing key information, but it would decrease variance as it removes a range of values that would have been summed to the total.
# END SOLN
# END SUBPROB

# BEGN SUBPROB
Suppose we predict `'total'` from `'veg'` using $8$ models with different degree polynomial features (degrees $0$ through $7$). Which of the following plots display the training and validation errors of these models? Assume that we plot the degree of the polynomial features on the x-axis, mean squared error loss on the y-axis, and the plots share y-axes limits.

<center><img src='../../assets/images/fa23-final/dsc80_final_plots.png' width=65%></center>

Training error:
- A
- B
- C
- D

Validation Error
- A
- B
- C
- D

# BEGN SOLN
**Answer**: Training error: C), validation error B).

Training error: As we get higher and higher degree polynomial features, we start to overfit. This means that our training accuracy increases, so our MSE gets very low the higher our degree is.

Validation error: We can see from the data that our data is likely best fit to degree $2$ polynomial features, so we see MSE decrease to the lowest at that point. However, further past that point the accuracy gets worse as we are overfit on training data, so MSE increases.

<average>88</average>

# END SOLN
# END SUBPROB
# END PROB