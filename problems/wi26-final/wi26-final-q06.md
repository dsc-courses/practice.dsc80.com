# BEGIN PROB

We want to use linear regression to predict `"WaitTime"` based on

- `"NumProviders"`,
- `"Credentials"` (from Question 2),
- `"Department"`,
- and whether `"AppointmentTime"` is in the morning (before 12:00) or afternoon (12:00 or later).

We want to ensure that the coefficients are interpretable and can be used to determine the most impactful single feature in the model's predictions.

Fill in the code below to fit an appropriate `Pipeline` to the data in `med`, which we will think of as our training data for this problem.

```py
def hour(df):
    df.iloc[:, 0] = df.iloc[:, 0].dt.hour
    return df
X = med[["NumProviders", "Credentials", "Department", "AppointmentTime"]]
y = med["WaitTime"]
pl = ____
pl.fit(X, y)
```

There is only one blank in the code above, which should be filled with a capital letter corresponding to one of the answer choice options given below. This answer choice will have blanks of its own, which you should also fill in. Every time you use an answer choice, fill in the blanks in that answer choice with one of the following:

- a capital letter corresponding to an answer choice option,
- a string, or
- an integer.

Some answer choices will be unused. You should leave any blanks in those answer choices empty.

**Answer choice options:**

A. `drop = 'first'`

B. `remainder = 'drop'`

C. `remainder = 'passthrough'`

D. `PolynomialFeatures(___)`

E. `StandardScaler()`

F. `Binarizer(threshold = ___)`

G. `CountVectorizer()`

H. `FunctionTransformer(hour)`

I. `OneHotEncoder(___)`

J. `LinearRegression()`

K. `ColumnTransformer([("one", ___, ["AppointmentTime"]), ("two", ___, ["Department"])], ___)`

L. `ColumnTransformer([("one", ___, [___]), ("two", ___, [___]), ("three", ___, [___])], ___)`

M. `make_pipeline(___, ___)`

N. `make_pipeline(___, ___, ___)`

# BEGIN SOLUTION

**Answer:** `pl = N` where `N = make_pipeline(K, E, J)` and:

- `K = ColumnTransformer([("one", M, ["AppointmentTime"]), ("two", I, ["Department"])], C)`
- `M = make_pipeline(H, F)` with `H = FunctionTransformer(hour)` and `F = Binarizer(threshold=11)`
- `I = OneHotEncoder(A)` i.e. `OneHotEncoder(drop='first')`
- `C = remainder='passthrough'`
- `E = StandardScaler()`
- `J = LinearRegression()`

`FunctionTransformer(hour)` extracts the hour from `"AppointmentTime"`. `Binarizer(threshold=11)` encodes afternoon appointments (hour $\geq 12$) as 1 and morning as 0. `OneHotEncoder(drop='first')` encodes `"Department"` without creating a redundant dummy column. `remainder='passthrough'` keeps `"NumProviders"` and `"Credentials"` as numeric features. `StandardScaler()` puts all features on a comparable scale so that coefficient magnitudes reflect relative impact on `"WaitTime"`. `LinearRegression()` is the final estimator.

# END SOLUTION

# END PROB
