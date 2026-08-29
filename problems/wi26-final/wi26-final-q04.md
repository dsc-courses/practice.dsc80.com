# BEGIN PROB

`sklearn` is considering adding a new hyperparameter to its `DecisionTreeClassifier` class. The new hyperparameter, `min_entropy`, is used to determine when a node should be split. A node will be split when its entropy is greater than or equal to `min_entropy`. Otherwise, the node will be a leaf node.

Suppose we create training and testing datasets as follows.

```py
X = med.drop(columns=["Wait"])
y = med["Wait"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

# BEGIN SUBPROB

The function below selects a value for `min_entropy` based on an input list of candidate values.

```py
def find_min_entropy(candidates):
    highest_score = -1
    out = -1
    for min_e in candidates:
        dt = DecisionTreeClassifier(min_entropy=min_e)
        dt.fit(X_train, y_train)
        if dt.score(X_train, y_train) >= highest_score:
            highest_score = dt.score(X_train, y_train)
            out = min_e
    return out
```

What should the function return on an input list of `[0, 0.2, 0.4, 0.6, 0.8, 1]`?

# BEGIN SOLUTION

**Answer:** `0`

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Circle one word in each box: If we train a decision tree with the value selected in part (a) for `min_entropy`, the test accuracy will likely be ____ than the train accuracy due to ____.

1. higher / lower
2. underfitting / overfitting

# BEGIN SOLUTION

**Answer:** lower; overfitting

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Circle one word in each box: In general, increasing the value of `min_entropy` ____ bias and ____ variance.

1. increases / decreases
2. increases / decreases

# BEGIN SOLUTION

**Answer:** increases; decreases

# END SOLUTION

# END SUBPROB

# END PROB
