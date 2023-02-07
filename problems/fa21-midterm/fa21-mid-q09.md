# BEGIN PROB

You have a second dataframe, `personalities`, that contains the disposition and intelligence of several species of penguin:

<center><img src='../assets/images/fa21-midterm/personalities.png' width=35%></center>

Note that `personalities` is missing some of the species that are in `df`, and it contains species that are *not* in `df`.

You'd like to use the table to add columns to `df` for the disposition and intelligence of each of the penguins in the data set. If a species in `df` is not listed in `personalities`, you're OK with having their disposition and Intelligence be `NaN`. And if a species in `personalities` is not in `df`, it should not be added. Therefore, the result of your merge should have exactly 330 rows -- the same as `df`.

Which of the below will perform this?

( ) `pd.merge(df, personalities, how='outer')`
( ) `pd.merge(df, personalities, how='inner')`
( ) `pd.merge(df, personalities, how='left')`
( ) `pd.merge(df, personalities, how='right')`

# BEGIN SOLN
**Answer: ** Option C

Since we want our resulting DataFrame to have the same number of rows as `df`, which is our left dataframe, we simply just perform a left merge which is Option C. Right merge and outer merge are wrong since there are some species in `personalities` not in `df`, and inner merge wouldn't work since there are some species in `df` not in `personalities`.

<average>93</average>

# END SOLN

# END PROB