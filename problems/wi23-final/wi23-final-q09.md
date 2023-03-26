# BEGIN PROB
One piece of information that may be useful as a feature is the proportion of SAT test takers in a state in a given year that qualify for free lunches in school. The Series `lunch_props` contains 8 values, each of which are either `"low"`, `"medium"`, or `"high"`. Since we can't use strings as features in a model, we decide to encode these strings using the following `Pipeline`:

```py
# Note: The FunctionTransformer is only needed to change the result
# of the OneHotEncoder from a "sparse" matrix to a regular matrix
# so that it can be used with StandardScaler;
# it doesn't change anything mathematically.
pl = Pipeline([
    ("ohe", OneHotEncoder(drop="first")),
    ("ft", FunctionTransformer(lambda X: X.toarray())),
    ("ss", StandardScaler())
])
```

After calling `pl.fit(lunch_props)`, `pl.transform(lunch_props)` evaluates to the following array:

```py
array([[ 1.29099445, -0.37796447],
       [-0.77459667, -0.37796447],
       [-0.77459667, -0.37796447],
       [-0.77459667,  2.64575131],
       [ 1.29099445, -0.37796447],
       [ 1.29099445, -0.37796447],
       [-0.77459667, -0.37796447],
       [-0.77459667, -0.37796447]])
```

and `pl.named_steps["ohe"].get_feature_names()` evaluates to the following array:

```py
array(["x0_low", "x0_med"], dtype=object)
```

Fill in the blanks: Given the above information, we can conclude that `lunch_props` has __(a)__ value(s) equal to `"low"`, __(b)__ value(s) equal to `"medium"`, and __(c)__ value(s) equal to `"high"`. *(Note: You should write one positive integer in each box such that the numbers add up to 8.)*


What goes in blank (a)?

What goes in blank (b)?

What goes in blank (c)?

# BEGIN SOLN
**Answer: ** 3, 1, 4

# END SOLN

# END PROB