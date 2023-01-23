# BEGIN PROB

Suppose we build a binary classifier that uses a song's `"track_name"`
and `"artist_names"` to predict whether its genre is `"Hip-Hop/Rap"` (1)
or not (0).

For our classifier, we decide to use a brand-new model built into
`sklearn` called the\
`BillyClassifier`. A `BillyClassifier` instance has three
hyperparameters that we'd like to tune. Below, we show a dictionary
containing the values for each hyperparameter that we'd like to try:

    hyp_grid = {
      "radius": [0.1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100], # 12 total
      "inflection": [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], # 10 total
      "color": ["red", "yellow", "green", "blue", "purple"] # 5 total
    }

To find the best combination of hyperparameters for our
`BillyClassifier`, we first conduct a train-test split, which we use to
create a training set with 800 rows. We then use `GridSearchCV` to
conduct $k$-fold cross-validation for each combination of
hyperparameters in `hyp_grid`, with $k=4$.

# BEGIN SUBPROB

When we call `GridSearchCV`, how many times is a `BillyClassifier`
instance trained in total? Give your answer as an integer.

# BEGIN SOLN

**Answer: ** 2400

There are $12 \cdot 10 \cdot 5 = 600$ combinations of hyperparameters.
For each combination of hyperparameters, we will train a
`BillyClassifier` with that combination of hyperparameters $k = 4$
times. So, the total number of `BillyClassifier` instances that will be
trained is $600 \cdot 4 = 2400$.

<average>73</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

In each of the 4 folds of the data, how large is the training set, and
how large is the validation set? Give your answers as integers.

size of training set =

size of validation set =

# BEGIN SOLN

**Answer: ** 600, 200

Since we performed $k=4$ cross-validation, we must divide the training
set into four disjoint groups each of the same size.
$\frac{800}{4} = 200$, so each group is of size 200. Each time we
perform cross validation, one group is used for validation, and the
other three are used for training, so the validation set size is 200 and
the training set size is $200 \cdot 3 = 600$.

<average>77</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose that after fitting a `GridSearchCV` instance, its `best_params_`
attribute is

        {"radius": 8, "inflection": 4, "color": "blue"}

Select all true statements below.

[ ] The specific combination of hyperparameters in `best_params_` had the highest average training accuracy among all combinations of hyperparameters in `hyp_grid`.
[ ] The specific combination of hyperparameters in `best_params_` had the highest average validation accuracy among all combinations of hyperparameters in `hyp_grid`.
[ ] The specific combination of hyperparameters in `best_params_` had the highest training accuracy among all combinations of hyperparameters in `hyp_grid`, in each of the 4 folds of the training data.
[ ] The specific combination of hyperparameters in `best_params_` had the highest validation accuracy among all combinations of hyperparameters in `hyp_grid`, in each of the 4 folds of the training data.
[ ] A `BillyClassifier` that is fit using the specific combination of hyperparameters in `best_params_` is guaranteed to have the best accuracy on unseen testing data among all combinations of hyperparameters in `hyp_grid`.

# BEGIN SOLN

**Answer: ** Option B

When performing cross validation, we select the combination of
hyperparameters that had the highest **average validation accuracy**
across all four folds of the data. That is, by definition, how
`best_params_` came to be. None of the other options are guaranteed to
be true.

<average>82</average>

# END SOLN

# END SUBPROB

# END PROB