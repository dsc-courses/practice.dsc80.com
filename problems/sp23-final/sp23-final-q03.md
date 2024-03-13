# BEGIN PROB

Suraj is exploring the relationship between the applied voltage and resulting current of an electrical element called Diode. At first, he decides to fit a Linear Regression model on some training data stored in DataFrame `diode`. `diode` has two columns, named `"Voltage"` and `"Current"`, respectively.

<center><img  src='../assets/images/sp23-final/q3.png'  width=40%></center>

# BEGIN SUBPROB

In the following code, Suraj implements k-fold cross validation. He stores all the validation root mean squared error (RMSE) values of each fold in `errs_dataframe` Dataframe.

```py
errs = cross_val_score(LinearRegression(), diode[['voltage']], diode['current'], cv=5, scoring='neg_root_mean_squared_error')

errs_dataframe = pd.DataFrame(-errs,columns=['rmse'], index=[f'Fold {i}' for i in range(1, 6)])

errs_dataframe
```

Based on the information in `errs_dataframe`, which one is a true statement? 

( ) The validation RMSE of Fold 5 is the lowest.
( ) The validation RMSE of Fold 5 is the highest.
( ) The validation RMSE of Fold 1 is significantly higher than the validation RMSE of fold 5.
( ) The validation RMSE of all the folds (i.e., Fold 1-5) are similar to each other.

  

# BEGIN SOLN
**Answer:** B - The validation RMSE of Fold 5 is the highest.

To answer this question, we can use the plot showing the actual data in each fold, 
along with the fact that we are fitting a linear regression model. We can see 
that a line fitted on all the folds would likely fit datapoints from the fifth 
fold worse than points from the first four folds. This is because the first four 
folds appear to fall along a relatively linear pattern amongst themselves, compared 
to when the fifth fold is included in our considerations. Thus the validation 
RMSE would be highest for the fifth fold.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Consider the following piece of code where we implement a hyperparameter search with GridSearchCV():
```py
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

diabetes = pd.read_csv('data/diabetes.csv')

X_train, X_test, y_train, y_test = train_test_split(diabetes[['Glucose', 'BMI']], diabetes['Outcome'])

hyperparameters = {
'max_depth': [2, 3, 4, 5, 7, 10, 13, 15, 18, None],
'min_samples_split': [2, 5, 10, 20, 50],
'criterion': ['gini', 'entropy']
}

searcher = GridSearchCV(DecisionTreeClassifier(), hyperparameters, cv=8)
searcher.fit(X_train, y_train)
```

In total, how many decision tree models were trained under the hood for this hyperparameter search?

( ) 8
( ) 100
( ) 200
( ) 800
( ) 1600

# BEGIN SOLN
**Answer:** 800

The code specifies 10 options for `max_depth`, 5 options for `max_depth`, 
2 options for `criterion`, and the cross validation parameter in GridSearchCV is 
set to 8. Therefore the total number of trained models is equal to the total
number of combinations of `max_depth`, `max_depth`, and `criterion`, times 8 for 
the number of cross validation folds:

$10 \cdot 5  \cdot 2  \cdot 8 = 800$

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
Consider the same piece of code from the previous problem.

After fitting the searcher, you run the following line of code. What would this line of code evaluate to?

```py
searcher.cv_results_['mean_test_score'].shape[0]
```

( ) 8
( ) 100
( ) 200
( ) 800
( ) 1600

# BEGIN SOLN
**Answer:** 100

Taking the mean test score from all 8 cross validation folds for the models 
gives 1 value for each combination of `max_depth`, `max_depth`, and `criterion`. 
Therefore the code will evaluate to the total number of combinations of `max_depth`, 
`max_depth`, and `criterion`:

$10 \cdot 5  \cdot 2  = 100$

# END SOLN

# END SUBPROB

# END PROB