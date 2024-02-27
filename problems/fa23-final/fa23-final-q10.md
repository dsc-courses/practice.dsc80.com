# BEGIN PROB
# BEGIN SUBPROB

Suppose we fit decision trees of varying depths to predict `'y'` using `'x1'` and `'x2'`. The entire training set is shown in the table below.
<center><img src='../../assets/images/fa23-final/dsc_80_final_q10.png' width=15%></center>

For each option below, select **one** answer from the list:

( ) 0
( ) 0.5
( ) 1
( ) 2

i. The entropy of a node containing all the training points.
ii. The lowest possible entropy of a node in a fitted tree with depth $1$ (two leaf nodes).
iii. The lowest possible entropy of a node in a fitted tree with depth $2$ (four leaf nodes). 

# BEGIN SOLN

- i. **Answer: 1**. Remember, the entropy of a node is $- \sum_{C} p_C \log_2 p_C$, where $C$ represents a class (that is, a `'y'` value) and $p_C$ represents the proportion of points in that node belonging to class $C$. In our training set, there are two classes, 0 and 1, each contaning a proportion $p_0 = p_1 = \frac{1}{2}$ of the values. So, the entropy of a node that contains our entire training set is $$-\frac{1}{2} \log_2 \left( \frac{1}{2} \right) - \frac{1}{2} \log_2 \left( \frac{1}{2} \right) = - \log_2  \left( \frac{1}{2} \right) = \log_2 2 = 1$$
- ii. **Answer: 0**. The lowest possible entropy of a node is achieved when the node is "pure" – that is, when it only contains points from a single class (a single `'y'` value). In such a node, the one class $C$ has a proportion $p_C = 1$ of the points, and the corresponding entropy is $$-p_C \log_2 p_C = -1 \log_2 1 = - 1 \cdot 0 = 0$$
- iii. **Answer: 0**. The reasoning from ii applies here, too.

<average>52</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Suppose we write the following code:
```py
hyperparameters = {
	'n_estimators': [10, 100, 1000], # number of trees per forest
	'max_depth': [None, 100, 10]     # max depth of each tree
}
grids = GridSearchCV(
	RandomForestClassifier(), param_grid=hyperparameters,
	cv=3, # 3-fold cross-validation
)
grids.fit(X_train, y_train)
```
Answer the following questions with a single number. 

i. How many random forests are fit in total?
ii. How many decision trees are fit in total?
iii. How many times in total is the first point in `X_train` used to train a decision tree?

# BEGIN SOLN

- i. **Answer: 27**. Since we're performing 3-fold cross-validation, a random forest with each combination of hyperparameters is fit 3 times. There are $3 \cdot 3 = 9$ combinations of hyperparameters, because there are 3 values for `n_estimators` and 3 values for `max_depth`. So, the total number of random forests fit is $3 \cdot 3 \cdot 3 = 27$.
- ii. **Answer: 9990**. The number of decision trees fit in a particular random forest comes from the `n_estimators` hyperparameter. For instance, a random forest that has `n_estimators=10` is made up of 10 decision trees. The question is, then, how many times do we fit a random forest with 10 decision trees (10 because it's the first value in `n_estimators`)? The answer is 9, which is the value of $k$ (3) multiplied by the number of values for `max_depth` that are being tested – remember, $k$ times, we fit a random forest with each combination of `n_estimators` and `max_depth`. So, 9 times, a random forest with 10 decision trees is fit – but also, 9 times, a random forest with 100 decision trees is fit, and 9 times, a random forest with 1000 decision trees is fit. So, how many total decision trees are fit? $$9 \cdot (10 + 100 + 1000) = 9 \cdot 1110 = 9990$$
- iii. **Answer: 6660**. Since we're performing $k$-fold cross-validation, our training set is split into 3 "folds". For each combination of hyperparameters, we fit a random forest 3 times – once using fold 1 as a training set and folds 2 and 3 to validate, once using fold 2 as a training set and folds 2 and 3 to validate, and once using fold 3 as a training set and folds 1 and 2 to validate. The first point in `X_train` belongs to just one of these three folds, meaning for every combination of hyperparameters it's used for training twice (and validation once). For `n_estimators=10`, `X_train` is used for training a random forest $3 \cdot 2$ times, which means it's used for training a decision tree $10 \cdot 3 \cdot 2$ times. Following this logic for `n_estimators=100` and `n_estimators=1000` and summing the results gives us
	$$(10 + 100 + 1000) (3 \cdot 2) = 1110 \cdot 6 = 6660$$
	So, the first point in `X_train` is used to train a decision tree 6660 times.

<average>41</average>

# END SOLN

# END SUBPROB

# END PROB