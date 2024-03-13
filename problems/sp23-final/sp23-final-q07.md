# BEGIN PROB

# BEGIN SUBPROB

Consider a DataFrame `df` containing sales data for a company with the following columns: `"Year"`, `"Month"`, `"Product"`, `"Region"`, and `"Revenue"`. The `"Revenue"` column represents the sales revenue for each product in a specific region during a particular month of a year. You want to create a pivot table to summarize the total revenue for each product in each year. Which of the following options correctly achieve this? Select all that apply.

[ ] 
```py
pd.pivot_table(df, values='Revenue', index='Product',
columns='Year', aggfunc=np.sum)
```
[ ]
```py
pd.pivot_table(df, values='Revenue', index=['Year', 'Product'],
columns='Region', aggfunc=np.sum)
```
[ ]
```py
pd.pivot_table(df, values='Revenue', index=['Product', 'Year'],
columns='Month', aggfunc=np.sum)
```
[ ]
```py
pd.pivot_table(df, values='Revenue', index='Year',
columns='Product', aggfunc=np.sum)
```

# BEGIN SOLN
**Answer:** Options 1 and 4

Options 1 and 4 have the same behavior, in that they create pivot tables that 
display the sum of revenue for each product in each year (`index` and `column` are interchangeable). 
Options 3 and 4 are incorrect because they use columns such as `Region` and `Month` that are not 
necessary to generate the information that is desired in the pivot table.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

Let's consider the two DataFrames: `timeuse1` and `timeuse2`. Both DataFrames have 10 rows in it.

<center><img  src='../assets/images/sp23-final/q7.png'  width=40%></center>

**1** The following code uses `pd.concat` to combine the two DataFrames.
```py
	pd.concat([timeuse1.set_index('Country'),
		timeuse2.set_index('Country_name')], axis=1)
```

How many NaN values would the resulting DataFame have?

# BEGIN SOLN
**Answer: ** 20

The values in the index of `timeuse1` that are not in `timeuse2` are Estonia, 
Spain, France, and Italy. These 4 indices contribute to $4 \cdot 3 = 12$ NaN values 
in the concatenated DataFrame, since `timeuse2` has 3 non-index columns.

The values in the index of `timeuse2` that are not in `timeuse1` are Slovenia, 
Finland, United Kingdom, and Norway. These 4 indices contribute to $4 \cdot 2 = 8$ NaN values 
in the concatenated DataFrame, since `timeuse1` has 2 non-index columns.

So the total number of NaN values in the concatenated DataFrame is $12 + 8 = 20$

# END SOLN

# END SUBPROB

# BEGIN SUBPROB

**2** The following code uses `merge()` to combine the two DataFrames from the question above.

```py
	timeuse1.merge(timeuse2, left_on='Country', 
		right_on='Country_name', how='inner')
```

How many NaN values would the resulting DataFame have?

# BEGIN SOLN
**Answer:** 0

The resulting DataFrame would have no NaN values. This is because the merged 
DataFrame used an inner merge, and would only contain rows with the same country 
name in both DataFrames, contributing non Nans, and none of the rows in either 
unmerged DataFrame starts off with NaN values.

# END SOLN

# END SUBPROB

# BEGIN SUBPROB
 
**3** What would the following code evaluate to?

```py
	timeuse1.merge(timeuse2, left_on='Country',
		right_on='Country_name', how='outer').shape[0]
```

# BEGIN SOLN
**Answer:** 14

Using an outer join results in a row for each unique country name across both datasets. 
This number is equal to 14, so the code above, which returns the number of rows in 
the outer joined DataFrame, would evaluate to 14.

# END SOLN

# END SUBPROB

# END PROB