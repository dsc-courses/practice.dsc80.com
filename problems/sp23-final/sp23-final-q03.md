# BEGIN PROB

# BEGIN SUBPROB

Suraj is exploring the relationship between the applied voltage and
resulting current of an electrical element called Diode. At first, he
decides to fit a Linear Regression model on some training data stored in
DataFrame `diode`. `diode` has two columns, named `"Voltage"` and
`"Current"`, respectively.

::: center
![image](final_images/q3.pdf){width=".65\\textwidth"}
:::

In the following code, Suraj implements k-fold crossvalidation. He
stores all the validation root mean squared error (RMSE) values of each
fold in `errs_dataframe` Dataframe.

    errs = cross_val_score(LinearRegression(), diode[['voltage']], 
            diode['current'], cv=5, scoring='neg_root_mean_squared_error')
    errs_dataframe = pd.DataFrame(-errs,columns=['rmse'],
                index=[f'Fold {i}' for i in range(1, 6)])
    errs_dataframe

Based on the information in `errs_dataframe`, which one is a true
statement?

( ) The validation RMSE of Fold 5 is the lowest.

( ) The validation RMSE of Fold 5 is the highest.

( ) The validation RMSE of Fold 1 is significantly higher than the
validation RMSE of fold 5.

( ) The validation RMSE of all the folds (i.e., Fold 1-5) are similar to
each other.

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Consider the following piece of code where we implement a hyperparameter
search with GridSearchCV():

    from sklearn.model_selection import GridSearchCV
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split

    diabetes = pd.read_csv('data/diabetes.csv')

    X_train, X_test, y_train, y_test = train_test_split(
    diabetes[['Glucose', 'BMI']], diabetes['Outcome'])

    hyperparameters = {
        'max_depth': [2, 3, 4, 5, 7, 10, 13, 15, 18, None], 
        'min_samples_split': [2, 5, 10, 20, 50],
        'criterion': ['gini', 'entropy']
    }

    searcher = GridSearchCV(DecisionTreeClassifier(), hyperparameters, cv=8)

    searcher.fit(X_train, y_train)

In total, how many decision tree models were trained under the hood for
this hyperparameter search?

( ) 8

( ) 100

( ) 200

( ) 800

( ) 1600

After fitting the searcher, you run the following line of code. What
would this line of code evaluate to?

    searcher.cv_results_['mean_test_score'].shape[0]

( ) 8

( ) 100

( ) 200

( ) 800

( ) 1600

# BEGIN SOLUTION

# END SOLUTION

# END SUBPROB

# END PROB