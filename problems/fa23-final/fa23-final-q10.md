# BEGIN PROB
# BEGIN SUBPROB
Suppose we fit decision trees of varying depths to predict `'y'` using `'x1'` and `'x2'`. The entire training set is shown in the table below.
<center><img src='../../assets/images/fa23-final/dsc80_final_q10.png' width=65%></center>

For each option below, select **one** answer from the list:
- 0
- 0.5
- 1
- 2

A) The entropy of a node containing all the training points.

B) The lowest possible entropy of a node in a fitted tree with depth $1$ (two leaf nodes)?

C) The lowest possible entropy of a node in a fitted tree with depth $2$ (four leaf nodes)? 

# BEGIN SOLN
**Answer**: 
A) 1 
B) 0
C) 0

# END SOLN

# BEGIN SUBPROB
Suppose we write the following code:
```
hyperparameteres = {
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

i. How many random forests are fit in total? ____
ii. How many decision trees are fit in total? ____
iii. How many times in total is the first point in `X_train` used to train a decision tree?
# BEGIN SOLN
**Answer**:
i. 27
ii. 9990
iii. 6660

i. We perform grid search with $3$-fold cross-validation, and each time we test $3$ `n_estimators` and $3$ `max_depth` values. Therefore we fit $3\times3\times3=27$ random forests.

ii. The number of decision trees is the sum of the `n_estimators`, which is $10+100+1000=1110$. We repeat this process $3$ times for the 3-fold cross-validation, and $3$ times for each cross-validation for each `max_depth`. Therefore we fit $1110\times3\times3=9990$ total decision trees.

iii. Each point in `X_train` belongs to one of $3$ folds for $3$-fold cross validation. Therefore, each points is used once for validation in cross-training, and twice in training. We can then follow the same math as part ii to see that the first point in `X_train` is used to train a decision tree $1110\times3\times2=6660$ times.
# END SOLN
# END SUBPROB
# END PROB