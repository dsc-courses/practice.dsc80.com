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

When `min_entropy = 0`, nodes are always allowed to split (as long as other stopping criteria permit), so the tree can fit the training data as well as possible. This gives the highest training accuracy among the candidates, and the function breaks ties by choosing the first value that achieves the highest score.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Circle one word in each box: If we train a decision tree with the value selected in part (a) for `min_entropy`, the test accuracy will likely be ____ than the train accuracy due to ____.

1. higher / lower
2. underfitting / overfitting

# BEGIN SOLUTION

**Answer:** lower; overfitting

With `min_entropy = 0`, the tree can grow until it fits the training data very closely, which typically leads to overfitting and lower test accuracy than training accuracy.

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Circle one word in each box: In general, increasing the value of `min_entropy` ____ bias and ____ variance.

1. increases / decreases
2. increases / decreases

# BEGIN SOLUTION

**Answer:** increases; decreases

A larger `min_entropy` prevents splits on low-entropy nodes, producing a simpler tree. Simpler models have higher bias and lower variance.

# END SOLUTION

# END SUBPROB

# END PROB
