# BEGIN PROB
Suppose incomplete data is collected on three new penguins, shown below:

<center><img src='../assets/images/fa21-midterm/incomplete.png' width=35%></center>

Call this DataFrame `df_incomplete`, and note that there are fewer columns than in `df` and that the columns which do appear are in a different order.

Suppose `df_incomplete` is appended to the end of `df` with the code `pd.concat([df, df_incomplete])`. What will be the values in the *last* line of the resulting DataFrame?

( ) `[197, 19.5, 'Adelie', nan, nan, nan, nan]` with row label (index) 2
( ) `[nan, 19.5, 197.0, nan, nan, nan, 'Adelie']` with row label (index) 2
( ) `[0, 19.5, 197.0, nan, nan, nan, 'Adelie']`  with row label (index) 2
( ) `[197, 19.5, 'Adelie', 0, 0, 0, 0]`  with row label (index) 2
( ) `[197, 19.5, 'Adelie', nan, nan, nan, nan]` with row label (index) 332
( ) `[nan, 19.5, 197.0, nan, nan, nan, 'Adelie']` with row label (index) 332
( ) `[0, 19.5, 197.0, 0, 0, 0, 'Adelie']`  with row label (index) 332
( ) `[197, 19.5, 'Adelie', 0, 0, 0, 0]`  with row label (index) 332

# BEGIN SOLN
**Answer: ** Option B

Concatting the incomplete DataFrame to `df` will essentially "match" the columns of the incomplete DataFrame to the corresponding columnd in `df`. (So 'Species' in the incomplete DataFrame will be matched to the 'Species' column in `df`). For the values that don't exist in the incomplete DataFrame, python will just fill the missing values with `nan`. Finally, the index row label still stays as 2. 

<average>97</average>

# END SOLN

# END PROB