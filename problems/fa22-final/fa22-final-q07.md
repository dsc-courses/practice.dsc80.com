# BEGIN PROB

# BEGIN SUBPROB

Consider the dataframe shown below:

<center><img src='../assets/images/fa22-final/pts.png' width=30%></center>


Suppose you wish to use this data in a linear regression model. To do so, the `color` column must be encoded numerically.

True or False: a meaningful way to numerically encode the `color` column is to replace each string by its index in the alphabetic ordering of the colors. That is, to replace "blue" by 1, "green" by 2, and "red" by 3.

( ) True
( ) False

# BEGIN SOLN
**Answer: ** False

Note that `color` is a nominal categorical varaible, meaning that there is no inherent ordering to the categories. Thus encoding the `color` variables by 1, 2, and 3 doesn't make any meaningful sense. I.e. it doesn't make sense to think of the color "red" as being "greater" than the color "blue" in any meaningful way.

<average>88</average>

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Suppose you perform a one-hot encoding of a Series containing the following strings:

`["red", "blue", "red", "green", "green", "purple", "orange", "blue"]}`

Assume that the encoding is created using the `OneHotEncoder(drop='first')` from `sklearn`. Note the `drop='first'` keyword argument: `skearn`'s
documentation says that this will "drop the first category in each feature."

How many columns will the resulting one-hot encoding table have?

# BEGIN SOLN
**Answer: ** 4

Recall that One-Hot Encoding will create a new column for each unique term in the group of strings. Thus "normal" One-Hot Encoding will create 5 columns, since there are 5 distinct words in the list of strings: "red", "blue", "green", "purple" and "orange". However, setting `drop='first'` will drop one of the columns, leaving us with 4 columns.

<average>88</average>

# END SOLN

# END SUBPROB

# END PROB